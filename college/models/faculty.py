from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
