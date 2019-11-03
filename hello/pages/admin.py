from django.contrib import admin

# Register your models here.
from . models import registeringo,logtable,proregisteringo,feedadd

#admin.site.register(listdb)
class registeringo_details(admin.ModelAdmin):
    fields = ['name', 'username','address','email']
    list_display = ['name', 'username','address','email']

admin.site.register(registeringo,registeringo_details)
admin.site.register(logtable)
admin.site.register(proregisteringo)
admin.site.register(feedadd)
