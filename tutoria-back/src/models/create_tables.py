from database import engine
from models import Base

# Création de toutes les tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
