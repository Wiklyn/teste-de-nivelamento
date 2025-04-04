from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import get_db
from models import Provider
from schemas import HealthInsuranceProviderSchema


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {
        'detail': 'Nothing implemented here.', 'endpoints': ['/api/providers']
    }


@app.get("/api/providers", response_model=List[HealthInsuranceProviderSchema])
def get_providers(db: Session = Depends(get_db)):
    providers = db.query(Provider).all()
    return providers
