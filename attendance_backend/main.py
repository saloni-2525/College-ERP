from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import select
from typing import List, Optional
from datetime import date

from models import Attendance
from database import get_session

app = FastAPI()

@app.post("/attendance/", response_model=Attendance)
def add_attendance(record: Attendance, session=Depends(get_session)):
    session.add(record)
    session.commit()
    session.refresh(record)
    return record

@app.get("/attendance/{student_id}", response_model=List[Attendance])
def get_attendance(
    student_id: int,
    from_date: Optional[date] = None,
    to_date: Optional[date] = None,
    session=Depends(get_session)
):
    query = select(Attendance).where(Attendance.student_id == student_id)
    if from_date:
        query = query.where(Attendance.attendance_date >= from_date)
    if to_date:
        query = query.where(Attendance.attendance_date <= to_date)
    records = session.exec(query).all()
    if not records:
        raise HTTPException(status_code=404, detail="No attendance records found")
    return records

@app.put("/attendance/{attendance_id}", response_model=Attendance)
def update_attendance(attendance_id: int, status: str, session=Depends(get_session)):
    record = session.get(Attendance, attendance_id)
    if not record:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    record.status = status
    session.commit()
    session.refresh(record)
    return record
