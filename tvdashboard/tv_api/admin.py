from django.contrib import admin
from .models import *

# Register your models here.

class LineAdmin(admin.ModelAdmin):
    list_display = ['id', 'line']

admin.site.register(Line,LineAdmin)

class ShiftAdmin(admin.ModelAdmin):
    search_fields = ['shift']
    list_display =  ['id', 'shift', 'start', 'end']
    
admin.site.register(ShiftsTv, ShiftAdmin)

class ShiftTargetsTvAdmin(admin.ModelAdmin):
    list_display = ['id', 'shift', 'target', 'actual', 'variance', 'line']

admin.site.register(ShiftTargetsTv, ShiftTargetsTvAdmin)

class WipTvAdmin(admin.ModelAdmin):
    list_display = ['id', 'shift', 'process', 'wip', 'line']
    
admin.site.register(WipTv, WipTvAdmin)