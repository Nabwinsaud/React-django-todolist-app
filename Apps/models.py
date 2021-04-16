from django.db import models

# Create your models here.


class Todos(models.Model):
    title=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)
    completed=models.BooleanField(default=False)

    def _str_(self):
        self.title



# class Names(models.Model):
#       title=models.CharField(max_length=1000)
#       product=models.CharField(max_length=1000)
#       price=models.IntegerField()
#       description=models.CharField(max_length=1000)

    