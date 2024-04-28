from src.models.models import Students, Company
def get_company_by_id(company_id):
    company = Company.query.get(company_id)
    return company