from django.contrib import admin

from .models import Brand, Car


@admin.register(Car)
class AdminCarView(admin.ModelAdmin):
    list_display = ('title', 'maker', 'price', )
    list_editable = ('maker', )
    list_per_page = 15
    list_filter = ('maker', )
    ordering = ('title', )

@admin.register(Brand)
class AdminBrandView(admin.ModelAdmin):
    list_display = ('title', )
    list_per_page = 15
    ordering = ('title', )
    