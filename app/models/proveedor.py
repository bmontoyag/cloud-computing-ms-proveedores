
from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Proveedor(Base):
    __tablename__ = "proveedores"
    __table_args__ = {"schema": "proveedores"}
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(160), unique=True, index=True)
    contacto: Mapped[str] = mapped_column(String(160), nullable=True)
    precio_referencia: Mapped[float] = mapped_column(Float, default=0.0)
