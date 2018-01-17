"""Core functionality module. Defines Project and
all auxilary models.
"""
from django.conf import settings
from django.db import models


class Trackable(models.Model):
    """Mixin for tracking updates and changes by time and user."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_%(class)s',
        on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='updated_%(class)s',
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class Project(Trackable):
    """Core model, union."""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"<Project: {self.name}>"


class Story(Trackable):
    """Actually text for <Project>. Could consist of
    <substories>."""
    title = models.CharField(max_length=140)
    slug = models.SlugField()
    text = models.TextField(blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Story: {self.slug}>"


class Artifact(Trackable):
    """Audio/Video/Picture -- raw result of interview."""
    name = models.CharField(max_length=140)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file = models.FileField(upload_to='multimedia/%Y/%m/%d')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"<Artifact: {self.name}>"


class Note(Trackable):
    """A brief record/idea, auxilary entity."""
    name = models.CharField(max_length=70)
    text = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Note: {self.name}>"


class Map(Trackable):
    """Stores map for plan, Could consist of <places>."""
    name = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Map: {self.name}>"


class Place(Trackable):
    """Globe location."""
    name = models.CharField(max_length=70)
    # TODO: change to lat/lon
    location = models.CharField(max_length=140)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Place: {self.name}, {self.location}>"



class List(Trackable):
    """Todo list for investigation."""
    name = models.CharField(max_length=70)
    slug = models.SlugField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"<TodoList: {self.name}>"


class Item(Trackable):
    """Task of Todo list."""
    title = models.CharField(max_length=70)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    completed = models.BooleanField(default=None)
    completed_date = models.DateField(blank=True, null=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='todo_assigned_to'
    )
    note = models.TextField(blank=True, null=True)
    priority = models.PositiveIntegerField()

    def __str__(self):
        return f"<TodoItem: {self.title}>"


# TOBEDEFINED

class Event:
    """Something what happend or gonna happen. Incorporate
    <place>, <person>/<collective> into <map>."""
    

class Calendar:
    """<Events> are placed into calendar."""


class Book:
    """Result of <project>."""
    # TODO: ToBeDefined
