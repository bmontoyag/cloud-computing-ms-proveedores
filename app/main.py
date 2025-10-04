from fastapi import FastAPI
from mangum import Mangum
from app.routes.proveedores import router as prov_router

app = FastAPI(title="MS Proveedores", version="1.0.0")
app.include_router(prov_router, prefix="/api/proveedores", tags=["Proveedores"])
handler = Mangum(app)
