from django.shortcuts import render
from django.views import generic
from datetime import datetime
from .models import Project


# Create your views here.
def index(request):
    num_projects = Project.objects.count()

    context = {"num_projects": num_projects, "year": datetime.now().year}

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


class ProjectListView(generic.ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context["year"] = datetime.now().year
        return context


class ProjectDetailView(generic.DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context["year"] = datetime.now().year
        return context
