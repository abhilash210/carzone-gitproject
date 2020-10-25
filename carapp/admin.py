from django.contrib import admin

from .models import Team
class Teamadmin(admin.ModelAdmin):
    list_display = ('id','fristname','designation')
    search_fields = ('fristname',)
admin.site.register(Team,Teamadmin)
