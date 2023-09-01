from django.shortcuts import render
from django.views import generic
from .models import Project


# Create your views here.
def index(request):
    num_projects = Project.objects.count()

    context = {"num_projects": num_projects}

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


class ProjectListView(generic.ListView):
    model = Project


class ProjectDetailView(generic.DetailView):
    model = Project
