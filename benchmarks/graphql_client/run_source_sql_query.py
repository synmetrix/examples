# Generated by ariadne-codegen
# Source: queries.graphql

from typing import Any, Optional

from .base_model import BaseModel


class RunSourceSQLQuery(BaseModel):
    run_query: Optional["RunSourceSQLQueryRunQuery"]


class RunSourceSQLQueryRunQuery(BaseModel):
    result: Optional[Any]