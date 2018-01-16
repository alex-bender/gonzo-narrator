from django.db import models


class Person(models.Model):
    """Main character."""


class Collective(models.Model):
    """A group of persons, band."""


class Contact(models.Model):
    """Mainly information for contacting band/person."""
