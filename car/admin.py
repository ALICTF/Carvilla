from django.contrib import admin

from .models import Brand, Car


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ('title', 'maker', 'price', )
    list_editable = ('maker', )
    list_per_page = 15
    list_filter = ('maker', )
    ordering = ('title', )


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    list_display = ('title', )
    list_per_page = 15
    ordering = ('title', )
    fields = ('title', 'description', 'datetime_created', 'datatime_modified')
    readonly_fields = ('datetime_created', 'datatime_modified')
    