from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio/", views.ProjectListView.as_view(), name="portfolio"),
    path("project/<int:pk>", views.ProjectDetailView.as_view(), name="project-detail"),
]
