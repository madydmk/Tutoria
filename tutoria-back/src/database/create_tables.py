from database import engine
from models.models import Base

# Création de toutes les tables
Base.metadata.create_all(engine)
