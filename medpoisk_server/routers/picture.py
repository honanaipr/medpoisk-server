import os
from urllib.parse import urljoin
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session

from .. import crud
from ..config import config
from ..dependencies import get_db

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
