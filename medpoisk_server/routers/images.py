from fastapi import APIRouter, Depends, HTTPException, UploadFile
from ..schemas import Doctor, Doctor, DoctorCreate
from uuid import UUID
from .. import crud
from ..dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoResultFound
from typing import Annotated
import os

router = APIRouter(
    prefix="/images",
    tags=["images"],
)

@router.post("/{id}")
async def create_file(id: UUID, file: UploadFile, db: Session = Depends(get_db)) -> str:
    file_path = f'./pictures/{id}.{file.filename.split(".")[-1]}'
    try:
        with open(file_path, 'wb') as f:
            content = await file.read()
            f.write(content)
        crud.set_product_picture_url(db, id, f"http://медпоиск.рф/pictures/{id}.{file.filename.split('.')[-1]}")
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
    db.commit()
    return f"http://медпоиск.рф/pictures/{id}.{file.filename.split('.')[-1]}"
