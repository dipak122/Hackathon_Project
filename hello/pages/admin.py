from django.contrib import admin

# Register your models here.
from . models import registeringo,logtable,proregisteringo,feedadd

#admin.site.register(listdb)


admin.site.register(registeringo)
admin.site.register(logtable)
admin.site.register(proregisteringo)
admin.site.register(feedadd)
