from django.contrib import admin
from first_page.models import AccessRecord, Topic, Webpage

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage) #Registered and ready to be used with administrative interface. BUt need super user
# Register your models here.
