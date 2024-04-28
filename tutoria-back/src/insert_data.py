import database.database as db
from models import Students

stud1 = Students(first_name = "Stud", last_name = "One", adress = "55 av de test", cp = "75000", mail = "test@test.com")
db.session.add(stud1)
db.session.commit()