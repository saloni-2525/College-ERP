from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Attendance(SQLModel, table=True):
    attendance_id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(index=True)
    attendance_date: date = Field(index=True)
    status: str
