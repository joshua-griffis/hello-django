from django.http.response import HttpResponse
from django.http.request import HttpRequest
import random


def hello_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Hello World!")
