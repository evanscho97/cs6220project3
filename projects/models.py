from django.db import models

class Project(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    item_category = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    item_added = models.IntegerField()
