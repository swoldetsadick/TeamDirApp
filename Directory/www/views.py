# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Person
from django.shortcuts import render

# Create your views here.
def index(request):
    """
    This function takes a request and renders an html in templates for main page.
    :param request: A request
    :return: a render
    """
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})
