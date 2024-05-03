from models.models import Course, Documents
import database.database as db

def get_all_courses():
    Course.query.all()

def get_course_by_id(id):
    if id != None:
        return Course.query.get(Course.id==id)
    return None

def get_course_by_company(companyId):
    if companyId != None:
        return Course.query.get(Course.companyId==companyId)
    return None

def get_course_document(courseId):
    Documents.query.get(Documents.idCourse == courseId)

# Ajoute l'id d'un document préalablement ajouté en db en tant qu'annexe de la formation
def add_document(idCourse, idDoc):
    course = Course.query.get(Course.id == idCourse)
    course.annexe = idDoc
    db.session.commit()

def create_course(course):
    if type(course) == Course:
        db.session.add(course)
        return True
    return False

def update_course(id, updated_course):

    if type(id) == int:
        course = Course.query.get(id)
        #course.intitle = updated_course.intitle
        course.descr = updated_course.descr
        course.course = updated_course.course
        course.annexe = updated_course.annexe
        #course.idCompany 
        db.session.commit()
        return True
    return False

def delete_course(id):
    if type(id) == int:
        db.session.delete(id)
        db.session.commit()
        return True
    return False