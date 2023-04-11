from django.contrib import admin
from .models import CarBrand,CarModel,CarOrders,CarType


class CarBranDisplay(admin.ModelAdmin):
    cols = ('name','status')
    list_display = cols
    search_fields = cols
    list_filter = cols

class CarModelDisplay(admin.ModelAdmin):
    cols = ('name','brand','status')
    list_display = cols
    search_fields = cols
    list_filter = cols

class CarOrdersDisplay(admin.ModelAdmin):
    cols = ('brand','model','status','type','date_request','date_from','date_to')
    list_display = cols
    search_fields = cols
    list_filter = cols

class CarTypeDisplay(admin.ModelAdmin):
    cols = ('type','model','status')
    list_display = cols
    search_fields = cols
    list_filter = cols


# Register your models here.
admin.site.register(CarBrand,CarBranDisplay)
admin.site.register(CarModel,CarModelDisplay)
admin.site.register(CarOrders,CarOrdersDisplay)
admin.site.register(CarType,CarTypeDisplay)