from django.db import models
class food(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)


    def __str__(self):
        return self.name 