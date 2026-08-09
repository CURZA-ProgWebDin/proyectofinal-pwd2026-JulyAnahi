from app.database import db
from app.models.base_model import BaseModel

class Producto(BaseModel):
    __tablename__ = 'Productos'

    name = db.Column(db.String(130), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.float, nullable=False)
    category = db.Column(db.String(64), nullable= False)
    is_available = db.Column(db.Boolean, default=True, nullable=False)
    image_url = db.Column(db.String(512),nullable=True)

    # def to_dict(self):
    #     return{
    #         'id':self.id,
    #         'name':self.name,
    #         'description':self.description,
    #         'is_available': self.is_available,
    #         'image_url': self.image_url
    #     }

