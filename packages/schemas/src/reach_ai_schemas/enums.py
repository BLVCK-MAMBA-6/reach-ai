"""Controlled vocabularies used by extraction and validation."""

from enum import StrEnum


class OpportunityType(StrEnum):
    FELLOWSHIP = "fellowship"
    GRANT = "grant"
    INTERNSHIP = "internship"
    RESEARCH_PROGRAM = "research_program"
    HACKATHON = "hackathon"
    SCHOLARSHIP = "scholarship"
    ACCELERATOR = "accelerator"
    COMPETITION = "competition"
    JOB = "job"
    OTHER = "other"


class ApplicationStatus(StrEnum):
    UPCOMING = "upcoming"
    OPEN = "open"
    CLOSED = "closed"
    ROLLING = "rolling"
    UNKNOWN = "unknown"


class RequirementCategory(StrEnum):
    AGE = "age"
    CITIZENSHIP = "citizenship"
    RESIDENCY = "residency"
    EDUCATION = "education"
    EXPERIENCE = "experience"
    LOCATION = "location"
    LANGUAGE = "language"
    AFFILIATION = "affiliation"
    SKILL = "skill"
    DOCUMENT = "document"
    OTHER = "other"


class RequirementStrength(StrEnum):
    HARD = "hard"
    SOFT = "soft"


class EvidenceKind(StrEnum):
    OFFICIAL_PAGE = "official_page"
    OFFICIAL_RULES = "official_rules"
    SECONDARY_SOURCE = "secondary_source"
    EMAIL = "email"
    USER_PROVIDED = "user_provided"


class MissingField(StrEnum):
    TITLE = "title"
    ORGANIZATION = "organization"
    OFFICIAL_URL = "official_url"
    APPLICATION_STATUS = "application_status"
    DEADLINE_DATE = "deadline.date"
    DEADLINE_TIME = "deadline.time"
    DEADLINE_TIMEZONE = "deadline.timezone"
    ELIGIBILITY = "eligibility"
    FUNDING = "funding"
    REQUIRED_DOCUMENTS = "required_documents"
    SELECTION_CRITERIA = "selection_criteria"
