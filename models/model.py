from sqlalchemy import Column, Integer, Float
from pydantic import BaseModel,  Field
from database import Base
from typing import Literal


class Patient(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True, index=True)
    gender = Column(Integer) 
    age = Column(Integer)
    status = Column(Integer, default=None)
    pressurehight = Column(Integer) 
    pressurelow = Column(Integer)
    glucose = Column(Float)
    kcm = Column(Float)
    troponin = Column(Float)
    impluse = Column(Integer)

class PatientCreate(BaseModel):
    
    gender :  Literal[0, 1]
    age : int =Field(..., ge=1, le=120)
    pressurehight : int =Field(..., ge=0)
    pressurelow : int =Field(..., ge=0)
    glucose : float =Field(..., ge=0)
    kcm : float =Field(..., ge=0)
    troponin : float =Field(..., ge=0)
    impluse : int =Field(..., ge=0)


class PatientResponse(BaseModel):
    id: int
    status : int = Literal[0, 1]

   
