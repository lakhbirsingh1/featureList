from django.db import models

class Feature(models.Model):
    title = models.CharField(max_length=200, default='Hello Python, Django, NextJs, My First Fullstack Project')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
