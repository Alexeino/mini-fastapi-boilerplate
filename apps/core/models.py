from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

from db.base.base import TimeStampModel

class RequestLog(TimeStampModel,table=True):
    method: str
    url: str
    status_code: str