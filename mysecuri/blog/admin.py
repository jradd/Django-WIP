from django.contrib import admin
from mysecuri.blog.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    
class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'pub_date')}

admin.site.register(Category, CategoryAdmin)

admin.site.register(Entry, EntryAdmin)

