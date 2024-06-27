from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1/")
auth = Blueprint("auth", __name__, url_prefix="/auth")


from api.v1.views.students import *
from api.v1.views.admin import *
from api.v1.views.users import *
from api.v1.views.parent import *
from api.v1.views.teacher import *
from api.v1.views.results import *


from models.student_models import Student
from models.teacher_models import Teacher
from models.subject_models import Subject
from models.result_models import Result
from models.parent_models import Parent
from models.base_model import Base, BaseClass
from models.admin_models import Administrator
