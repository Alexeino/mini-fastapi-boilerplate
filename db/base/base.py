from sqlmodel import SQLModel,Field
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, DateTime, func

class TimeStampModel(SQLModel):
    id: Optional[int] = Field(default=None,primary_key=True)
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=True
        )
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True), onupdate=func.now(), server_default=func.now(), nullable=True
        )
    )