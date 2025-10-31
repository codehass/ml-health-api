from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models.model import Patient, PatientCreate, PatientResponse
import pandas as pd
import joblib


app = FastAPI()


Base.metadata.create_all(bind=engine)
model = joblib.load("./ml/random_forest_model.dump")


# Create a new patient
@app.post("/patients/", response_model=PatientResponse)
async def create_(patient: PatientCreate, db: Session = Depends(get_db)):

    patient_features = pd.DataFrame(
        [
            [
                patient.age,
                patient.gender,
                patient.pressurehight,
                patient.pressurelow,
                patient.glucose,
                patient.kcm,
                patient.troponin,
                patient.impluse,
            ]
        ],
        columns=[
            "age",
            "gender",
            "pressurehight",
            "pressurelow",
            "glucose",
            "kcm",
            "troponin",
            "impluse",
        ],
    )

    status = model.predict(patient_features)
    status = int(status[0])

    print("Predicted status:", type(status))

    db_patient = Patient(
        gender=patient.gender,
        age=patient.age,
        pressurehight=patient.pressurehight,
        pressurelow=patient.pressurelow,
        glucose=patient.glucose,
        kcm=patient.kcm,
        troponin=patient.troponin,
        impluse=patient.impluse,
        status=status,
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


# Get a patient by ID
@app.get("/patients/{patient_id}", response_model=PatientResponse)
async def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient


# Get all patients
@app.get("/patients/")
async def read_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return {"patients": patients}


# Predict risk for a patient
@app.get("/patients/{patient_id}/predict_risk")
async def predict_risk(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    if db_patient.status == 0:
        risk = "Negatif"
    elif db_patient.status == 1:
        risk = "Psitif"
    else:
        risk = "not found"

    return {"patient_id": patient_id, "status": risk}


@app.get("/")
async def root():
    return {"message": "Hello to Cardio Risk Prediction API"}
