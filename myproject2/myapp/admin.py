from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'description','price','expire','image')

admin.site.register(Item, ItemAdmin)