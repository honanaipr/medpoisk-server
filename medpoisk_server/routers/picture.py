from fastapi import APIRouter, Depends, UploadFile
from uuid import UUID
from .. import crud
from ..dependencies import get_db
from sqlalchemy.orm import Session
from ..config import config
from urllib.parse import urljoin
import os

router = APIRouter(
    prefix="/pictures",
    tags=["pictures"],
)


@router.post("/{id}")
async def create_file(id: UUID, file: UploadFile, db: Session = Depends(get_db)) -> str:
    if not file.filename:
        return "filename not specified"
    file_name = f"{id}.{file.filename.split('.')[-1]}"
    file_path = f"{config.pictures_dir}/{file_name}"
    try:
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        crud.set_product_picture_url(db, id, urljoin("/pictures/", file_name))
    except Exception:
        if os.path.exists(file_path):
            os.remove(file_path)
    db.commit()
    return f"{config.pictures_dir}{id}.{file.filename.split('.')[-1]}"
