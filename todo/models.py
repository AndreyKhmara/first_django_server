from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
