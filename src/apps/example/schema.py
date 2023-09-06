from ninja.orm import create_schema
from apps.example.models import Name


OutputNameSchema = create_schema(Name)
InputNameSchema = create_schema(Name, exclude=['id'])
