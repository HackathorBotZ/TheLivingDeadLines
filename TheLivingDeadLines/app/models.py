"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    # ...


class MainModel(models.Model):
    title = models.CharField(max_length=42)
    document = models.ForeignKey(Document)
    #...