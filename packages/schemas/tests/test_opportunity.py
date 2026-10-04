import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from reach_ai_schemas import Deadline, OpportunityExtraction

FIXTURE = Path(__file__).parent / "fixtures" / "valid_hackathon.json"


def load_fixture() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def test_valid_opportunity_fixture() -> None:
    opportunity = OpportunityExtraction.model_validate(load_fixture())

    assert opportunity.schema_version == "1.0"
    assert opportunity.deadline.timezone == "Africa/Lagos"
    assert opportunity.model_run.provider == "mock"


def test_unknown_evidence_reference_is_rejected() -> None:
    payload = load_fixture()
    payload["requirements"][0]["evidence_ids"] = ["missing_evidence"]

    with pytest.raises(ValidationError, match="unknown evidence references"):
        OpportunityExtraction.model_validate(payload)


def test_duplicate_evidence_ids_are_rejected() -> None:
    payload = load_fixture()
    payload["evidence"].append(payload["evidence"][0])

    with pytest.raises(ValidationError, match="evidence ids must be unique"):
        OpportunityExtraction.model_validate(payload)


def test_deadline_time_requires_date() -> None:
    with pytest.raises(ValidationError, match="deadline time cannot be set"):
        Deadline(date=None, time="18:00:00", confidence=0.0)


def test_missing_deadline_keeps_unknown_information_explicit() -> None:
    payload = load_fixture()
    payload["deadline"] = {
        "date": None,
        "time": None,
        "timezone": None,
        "original_text": None,
        "confidence": 0.0,
        "evidence_ids": [],
    }
    payload["missing_information"] = ["deadline.date", "deadline.time", "deadline.timezone"]

    opportunity = OpportunityExtraction.model_validate(payload)

    assert opportunity.deadline.date is None
    assert "deadline.date" in opportunity.missing_information


def test_extra_model_fields_are_rejected() -> None:
    payload = load_fixture()
    payload["invented_field"] = "must not be silently accepted"

    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        OpportunityExtraction.model_validate(payload)
