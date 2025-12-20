"""Compatibility re-export for model imports.

This project defines models in split modules:
- `database.public_schema` for public tables
- `database.ingest_schema` for ingest-state tables

Importing this module keeps existing tooling (and any external callers)
working without needing to know the module split.
"""

from .base import Base

# Public schema models
from .public_schema import (  # noqa: F401
    Candidate,
    Committee,
    ScheduleAContribution,
    ScheduleBDisbursement,
    ScheduleEExpenditure,
    VendorNameKeyword,
    PurposeKeyword,
    VendorCategoryManual,
    VendorCategoryMap,
    Totals,
)

# Ingest schema models
from .ingest_schema import (  # noqa: F401
    IngestState,
    IngestCheckpoints,
    CommitteeRunState,
)

__all__ = [
    "Base",
    # public
    "Candidate",
    "Committee",
    "ScheduleAContribution",
    "ScheduleBDisbursement",
    "ScheduleEExpenditure",
    "VendorNameKeyword",
    "PurposeKeyword",
    "VendorCategoryManual",
    "VendorCategoryMap",
    "Totals",
    # ingest
    "IngestState",
    "IngestCheckpoints",
    "CommitteeRunState",
]
