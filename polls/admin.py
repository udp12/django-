from django.contrib import admin

# Register your models here.

from polls.models import Contact,Address,Login,Entry,Files_Upload_Model

admin.site.register(Contact)


admin.site.register(Address)


admin.site.register(Login)


admin.site.register(Entry)

admin.site.register(Files_Upload_Model)