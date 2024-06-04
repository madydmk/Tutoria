import models.database as db
from models.models import Documents, Students, Base

Base.metadata.create_all(db.engine)

stud1 = Students(first_name = "Stud", last_name = "One", address = "55 av de test", cp = "75000", mail = "test@test.com")

doc = Documents(name="test_file", path="/",idStudent="1")

# add company, course, certif to test
db.session.add(stud1)
db.session.commit()
db.session.add(doc)
db.session.commit()