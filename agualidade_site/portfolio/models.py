from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Project(models.Model):
    """Model representing a project (but not a specific copy of a project)."""

    title = models.CharField(max_length=200)

    tech = models.CharField(
        max_length=30,
        help_text="Enter a summary of the technologies used in the project",
    )

    smdesc = models.CharField(max_length=100, default="Um site feito por mim...")

    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the project"
    )

    link = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
        help_text="Link to project",
    )

    TYPE_OF_PROJECT = [
        (0, "Website"),
        (1, "Design"),
    ]

    type = models.IntegerField(choices=TYPE_OF_PROJECT)

    thumb = models.ImageField(help_text="Select a thumb for this project")

    color = models.CharField(
        max_length=7,
        default="#21b0c9",
        validators=[RegexValidator("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")],
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this project."""
        return reverse("project-detail", args=[str(self.id)])
