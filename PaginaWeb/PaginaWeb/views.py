from django.http import HttpResponse
from django.template import Template, Context, loader

def login(response):
    index = loader.get_template("login.html")
    documento = index.render()
    return HttpResponse(documento)