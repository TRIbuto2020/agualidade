from django.contrib import admin
from .models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "type")
    list_filter = ("title", "type", "tech")
    fields = ["title", "summary", ("type", "tech"), "link", ("thumb", "color")]
