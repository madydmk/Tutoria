import models.database as db
from models.models import Documents, Students, Base

Base.metadata.create_all(db.engine)

stud1 = Students(firstName = "Stud", lastName = "One", address = "55 av de test", cp = "75000", mail = "test@test.com")

doc = Documents(name="test_file", path="/",idStudent="1")

# add company, course, certif to test
db.session.add(stud1)
db.session.commit()
db.session.add(doc)
db.session.commit()

# {
#     "firstName": "test1",
#     "lastName": "New",
#     "address": "dqzdqdz",
#     "cp": "12345",
#     "mail": "john.doe@example.com",
#     "tel": "555-1234",
#     "schoolId": 1,
#     "cfaId": 1,
#     "enterpriseId": 1,
#     "password": "null"
#   }