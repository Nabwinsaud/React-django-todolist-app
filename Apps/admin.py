from django.contrib import admin

# Register your models here.
from.models import Todos

class TodoAdmin(admin.ModelAdmin):
      display=('title','description','completed')

admin.site.register(Todos,TodoAdmin)


    
