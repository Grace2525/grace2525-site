from django.contrib import admin

from .models import Blog,Topic

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['about']}),
        ('Date information', {'fields': ['date_added'], 'classes': ['collapse']}),
        ('Topics', {'fields': ['topics'], 'classes': ['collapse']}),
        ('Content', {'fields': ['content']}),
    ]
    
    list_display = ('title', 'about', 'date_added')
    list_filter = ['date_added','topics']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Topic)
