from fastapi import FastAPI

from src.lab6_intelligent_search.models.route_models import RouteRequest
from src.lab6_intelligent_search.services.search_service import find_route

app = FastAPI()


@app.post('/find-route')
def search_route(request: RouteRequest):
    return find_route(request.start, request.goal)