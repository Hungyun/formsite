from django.db import models

# Create your models here.



class Verb(models.Model):
    name = models.CharField(max_length=20)
    type = models.PositiveSmallIntegerField()

    def callname(self):
        return self.name
