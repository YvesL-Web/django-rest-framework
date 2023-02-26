from django.contrib import admin

from .models import Agent

# Register your models here.
@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date','is_mvp')
    list_display_links = ('id','name')
    list_editable = ('is_mvp',)
    search_fields = ('name',)
    list_per_page = 10
