from django.db import models

# class listdb(models.Model):
#     image = models.ImageField(upload_to='list/image',default="")
#     name = models.CharField(max_length=10,default="")
#     city = models.CharField(max_length=10,default="")
#     street = models.CharField(max_length=10,default="")
#
#     def __str__(self):
#         return self.name


class logtable(models.Model):
    name =models.CharField(max_length=20)
    service =models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'logtable'




class registeringo(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=8)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'registeringo'

