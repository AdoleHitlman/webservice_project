from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
# Create your views here.
@require_http_methods(["GET"])
def hello(request):
    name = request.GET.get('name', '')
    message = request.GET.get('message', '')
    return HttpResponse(f'Hello {name}! {message}!')