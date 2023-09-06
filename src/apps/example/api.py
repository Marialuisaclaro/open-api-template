from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from apps.example.models import Name
from apps.example.schema import OutputNameSchema, InputNameSchema

router = Router(tags=['Example'])


@router.get('/names', response={200: List[OutputNameSchema]})
def get_names(request):
    return 200, Name.objects.all()


@router.post('/names/new', response={201: OutputNameSchema, 409: None})
def new_name(request, name: InputNameSchema):
    new_name = name.name
    if not Name.objects.filter(name=new_name).exists():
        return 201, Name.objects.create(name=new_name)
    return 409, None


@router.delete('/names/delete', response={204: None, 404: None})
def delete_name(request, name_id: int):
    name = get_object_or_404(Name, id=name_id)
    name.delete()
    return 204, None
