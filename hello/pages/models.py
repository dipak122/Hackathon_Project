from django.db import models
import datetime

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
    brand =models.CharField(max_length=20)
    service =models.CharField(max_length=20)
    email =models.EmailField(max_length=20)
    address=models.TextField(max_length=8)
    des = models.TextField(max_length=50)
    date = models.TextField(max_length=10)
    time = models.TextField(max_length=10)
    #date = models.DateField(_("Date"),default=datetime.date.today)
    #time = models.TimeField(_(u"conversation time"),auto_now_add=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'logtable'




class registeringo(models.Model):
    name = models.CharField(max_length=10)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=8)
    email=models.TextField(max_length=8)
    address=models.TextField(max_length=8)


    def __str__(self):
        return self.username

    class Meta:
        db_table = 'registeringo'

