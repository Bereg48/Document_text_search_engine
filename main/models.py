from django.db import models


class Document(models.Model):
    id = models.IntegerField(primary_key=True)
    rubrics = models.JSONField()
    text = models.TextField()
    created_date = models.DateTimeField()
