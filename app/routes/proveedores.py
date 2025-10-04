from fastapi import APIRouter, HTTPException
import os
import boto3
from pydantic import BaseModel

router = APIRouter()
dynamodb = boto3.resource('dynamodb', region_name=os.getenv('AWS_REGION','us-east-1'))
TABLE = os.getenv('DDB_TABLE','Proveedores')

table = dynamodb.Table(TABLE)

class Proveedor(BaseModel):
    provider_id: str
    nombre: str
    material_tipo: str | None = None
    material_codigo: str | None = None
    precio_unitario: float | None = None

@router.get('/')
def listar():
    resp = table.scan()
    return resp.get('Items', [])

@router.post('/')
def crear(p: Proveedor):
    try:
        table.put_item(Item=p.dict())
        return {"mensaje":"Proveedor creado"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
