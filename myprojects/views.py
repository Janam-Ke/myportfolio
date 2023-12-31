from django.shortcuts import render
from myprojects.models import Project

def project_index(request):
    myprojects = Project.objects.all()
    context = {
        'myprojects' : myprojects
    }
    return render(request, 'project_index.html', context)



def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
