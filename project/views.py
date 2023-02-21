from django.shortcuts import render
from .models import *


def  index_of_project(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'index_of_project.html', context)


def details_of_projects(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project' : project
    }
    return render(request, 'details_of_projects.html', context)
