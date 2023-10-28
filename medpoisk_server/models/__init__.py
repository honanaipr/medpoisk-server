from .doctor import *
from .place import *
from .position import *
from .product import *

from ..database import Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
