"""Core functionality module. Defines Project and
all auxilary models.
"""
from django.db import models


class Project(models.Model):
    """Core model, union."""


class Story(models.Model):
    """Actually text for <Project>. Could consist of
    <substories>."""


class Artifact(models.Model):
    """Audio/Video/Picture -- raw result of interview."""


class Note(models.Model):
    """A brief record/idea, auxilary entity."""


class Map(models.Model):
    """Stores map for plan, Could consist of <places>."""


class Place(models.Model):
    """Globe location."""


class Book(models.Model):
    """Result of <project>."""


class Plan(models.Model):
    """Todo list for investigation."""


class Event(models.Model):
    """Something what happend or gonna happen. Incorporate
    <place>, <person>/<collective> into <map>."""


class Calendar(models.Model):
    """<Events> are placed into calendar."""
