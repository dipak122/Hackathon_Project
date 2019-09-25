from django.db import models

class listdb(models.Model):
    image = models.ImageField(upload_to='list/image',default="")
    name = models.TextField(max_length=10)
    city = models.TextField(max_length=10)


    def __str__(self):
        return self.name
