from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def project_shopping_cart(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_shopping_cart.html', context)

def project_remove(request, pk):
    project = Project.objects.get(pk=pk)
    cur = project.item_added - 1
    Project.objects.filter(pk=pk).update(item_added=cur)
    context = {
        'project': project
    }
    return render(request, 'remove_successful.html', context)

def project_add(request, pk):
    project = Project.objects.get(pk=pk)
    cur = project.item_added + 1
    Project.objects.filter(pk=pk).update(item_added=cur)
    context = {
        'project': project
    }
    return render(request, 'add_successful.html', context)