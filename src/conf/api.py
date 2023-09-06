from ninja import NinjaAPI
from apps.example.api import router as example_router

api = NinjaAPI(auth=None)
api.add_router("/example/", example_router)
