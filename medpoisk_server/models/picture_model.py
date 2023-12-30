from sqlalchemy import ForeignKey, event
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..config import BASE_PATH
from ..database import Base


class Picture(Base):
    __tablename__ = "picture"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    url: Mapped[str]

    product = relationship("Product", back_populates="pictures")


@event.listens_for(Picture, "after_delete")
def after_delete_picture(mapper, connection, target: Picture):
    test_path = BASE_PATH / "pictures" / target.url
    test_path.unlink()
