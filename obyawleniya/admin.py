from django.contrib import admin
from .models  import *

class AdsAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    list_editable = ('user',)

admin.site.register(CategoryAd)
admin.site.register(Ad,AdsAdmin)
admin.site.register(Locations)


