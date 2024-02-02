from sqlalchemy import ForeignKey
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base
from .division_model import Division
from .product_model import Product


class Balance(Base):
    __tablename__ = "balance"

    id: Mapped[int] = mapped_column(primary_key=True)
    division_id: Mapped[int] = mapped_column(ForeignKey("division.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    avg_price: Mapped[str] = mapped_column(postgresql.MONEY)
    amount: Mapped[int]

    @hybrid_property
    def price_in_rub(self) -> int:
        return int(self.avg_price.replace("$", ""))

    @price_in_rub.setter
    def price_in_rub_setter(self, value: int) -> None:
        self.avg_price = f"{value}+$"

    division: Mapped[Division] = relationship(back_populates="balance")
    product: Mapped[Product] = relationship("Product")
