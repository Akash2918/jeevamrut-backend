from django.contrib import admin

# Register your models here.
from .models import Data

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'name')

