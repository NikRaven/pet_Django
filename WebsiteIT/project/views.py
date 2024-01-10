from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectFrom


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project/project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project/project_detail.html', context)


def create_Pro(request):
    error = ''
    if request.method == 'POST':
        form = ProjectFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'
    form = ProjectFrom()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'project/project_create.html', data)
