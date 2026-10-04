"""Pydantic models for evidence-grounded opportunity extraction."""

from datetime import UTC, datetime
from datetime import date as Date
from datetime import time as Time
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, model_validator

from reach_ai_schemas.enums import (
    ApplicationStatus,
    EvidenceKind,
    MissingField,
    OpportunityType,
    RequirementCategory,
    RequirementStrength,
)


class StrictModel(BaseModel):
    """Base model that rejects unrecognized model output."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class EvidenceSpan(StrictModel):
    """A verbatim source span supporting an extracted claim."""

    id: str = Field(min_length=1, pattern=r"^[a-zA-Z0-9_-]+$")
    kind: EvidenceKind
    source_url: HttpUrl | None = None
    source_title: str | None = Field(default=None, min_length=1)
    quote: str = Field(min_length=1, max_length=2_000)
    retrieved_at: datetime | None = None


class Deadline(StrictModel):
    """Deadline components without silently inventing missing precision."""

    date: Date | None = None
    time: Time | None = None
    timezone: str | None = Field(default=None, min_length=1, max_length=100)
    original_text: str | None = Field(default=None, min_length=1, max_length=500)
    confidence: float = Field(ge=0.0, le=1.0)
    evidence_ids: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_precision(self) -> "Deadline":
        if self.time is not None and self.date is None:
            raise ValueError("deadline time cannot be set when deadline date is missing")
        if self.timezone is not None and self.time is None:
            raise ValueError("deadline timezone cannot be set when deadline time is missing")
        if self.date is None and self.confidence > 0.0:
            raise ValueError("deadline confidence must be 0 when no date is known")
        return self


class Requirement(StrictModel):
    """A hard or soft opportunity requirement supported by evidence."""

    id: str = Field(min_length=1, pattern=r"^[a-zA-Z0-9_-]+$")
    category: RequirementCategory
    strength: RequirementStrength
    description: str = Field(min_length=1, max_length=2_000)
    operator: str | None = Field(default=None, max_length=100)
    expected_value: Any | None = None
    evidence_ids: list[str] = Field(min_length=1)


class Funding(StrictModel):
    """Funding details exactly as stated by the source."""

    available: bool | None = None
    amount: str | None = Field(default=None, max_length=500)
    currency: str | None = Field(default=None, max_length=20)
    coverage: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)


class Conflict(StrictModel):
    """Two or more incompatible source claims requiring review."""

    field: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1, max_length=2_000)
    evidence_ids: list[str] = Field(min_length=2)


class ModelRunMetadata(StrictModel):
    """Trace information for the extraction call."""

    provider: str = Field(min_length=1, max_length=100)
    model: str = Field(min_length=1, max_length=200)
    prompt_version: str = Field(min_length=1, max_length=50)
    started_at: datetime
    completed_at: datetime
    input_tokens: int | None = Field(default=None, ge=0)
    output_tokens: int | None = Field(default=None, ge=0)

    @model_validator(mode="after")
    def validate_timestamps(self) -> "ModelRunMetadata":
        if self.completed_at < self.started_at:
            raise ValueError("completed_at cannot be earlier than started_at")
        return self


class OpportunityExtraction(StrictModel):
    """Versioned extraction result before canonical database insertion."""

    schema_version: Literal["1.0"] = "1.0"
    title: str = Field(min_length=1, max_length=500)
    title_evidence_ids: list[str] = Field(min_length=1)
    organization: str = Field(min_length=1, max_length=500)
    organization_evidence_ids: list[str] = Field(min_length=1)
    opportunity_type: OpportunityType
    official_url: HttpUrl | None = None
    application_status: ApplicationStatus
    deadline: Deadline
    requirements: list[Requirement] = Field(default_factory=list)
    funding: Funding | None = None
    benefits: list[str] = Field(default_factory=list)
    required_documents: list[str] = Field(default_factory=list)
    selection_criteria: list[str] = Field(default_factory=list)
    evidence: list[EvidenceSpan] = Field(min_length=1)
    missing_information: list[MissingField] = Field(default_factory=list)
    conflicts: list[Conflict] = Field(default_factory=list)
    model_run: ModelRunMetadata
    extracted_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @model_validator(mode="after")
    def validate_evidence_references(self) -> "OpportunityExtraction":
        evidence_ids = [item.id for item in self.evidence]
        if len(evidence_ids) != len(set(evidence_ids)):
            raise ValueError("evidence ids must be unique")

        referenced = set(self.title_evidence_ids)
        referenced.update(self.organization_evidence_ids)
        referenced.update(self.deadline.evidence_ids)

        for requirement in self.requirements:
            referenced.update(requirement.evidence_ids)
        if self.funding is not None:
            referenced.update(self.funding.evidence_ids)
        for conflict in self.conflicts:
            referenced.update(conflict.evidence_ids)

        unknown = sorted(referenced - set(evidence_ids))
        if unknown:
            raise ValueError(f"unknown evidence references: {', '.join(unknown)}")
        return self
