from django.contrib import admin

# Register your models here.

from .models import Dashboard

# admin.site.register([Dashboard])


@admin.register(Dashboard)
class DashboardsModelAdmin(admin.ModelAdmin):
    list_display = ['ds_dashboard', 'grupo_usuario']
    ordering = ['grupo_usuario']
    search_fields = ['ds_dashboard__icontains', 'grupo_usuario__name']
