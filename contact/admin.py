from django.contrib import admin
from contact import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('id',)
    
    
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name', 'phone',)
    ordering = ('id',)
    search_fields = ('id', 'first_name',)
    list_display_links = ('id', 'first_name',)
    list_per_page = 20
    list_max_show_all = 100
