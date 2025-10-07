
from pydantic import BaseModel

class ProveedorCreate(BaseModel):
    nombre: str
    contacto: str | None = None
    precio_referencia: float = 0.0

class ProveedorOut(ProveedorCreate):
    id: int
    class Config:
        from_attributes = True
