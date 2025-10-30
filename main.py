from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models.model import Patient, PatientCreate, PatientResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/patients/", response_model=PatientResponse)
async def create_item(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = Patient( 
        gender = patient. gender,
        age = patient.age,
        status = patient.status,
        pressurehight = patient.pressurehight ,
        pressurelow = patient.pressurelow,
        glucose = patient.glucose,
        kcm = patient.kcm,
        troponin = patient.troponin,
        impluse = patient.impluse,
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


@app.get("/patients/{patient_id}", response_model=PatientResponse)
async def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient