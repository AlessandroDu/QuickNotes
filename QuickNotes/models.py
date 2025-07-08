from django.db import models

class Note(models.Model):
    name = models.CharField(max_length=1024, null=True, blank=True)
    content = models.CharField(max_length=10240, null=True, blank=True)

    def __str__(self):
        return self.name