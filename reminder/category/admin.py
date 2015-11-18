from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category

# Register your models here.
class CategoryAdmin(MPTTModelAdmin):
    tree_title_field = 'name'
    tree_display = ('title',)


admin.site.register(Category, CategoryAdmin)