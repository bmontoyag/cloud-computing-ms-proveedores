
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.proveedor import Proveedor
from app.schemas.proveedor import ProveedorCreate, ProveedorOut

router = APIRouter(prefix="/proveedores", tags=["proveedores"])

@router.get("/", response_model=list[ProveedorOut])
def list_proveedores(db: Session = Depends(get_db)):
    return db.query(Proveedor).all()

@router.post("/", response_model=ProveedorOut)
def create_proveedor(payload: ProveedorCreate, db: Session = Depends(get_db)):
    exists = db.query(Proveedor).filter_by(nombre=payload.nombre).first()
    if exists:
        raise HTTPException(status_code=409, detail="Proveedor ya existe")
    prov = Proveedor(**payload.dict())
    db.add(prov)
    db.commit()
    db.refresh(prov)
    return prov
