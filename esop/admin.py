from django.contrib import admin

from esop.models import Department, Line, Station


class EsopAdminSite(admin.AdminSite):
    site_header = 'ESOP管理系统'
    site_title = 'ESOP管理系统'


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    list_display = ['id', 'line_no', 'department']

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'line']
    fieldsets = (
        ('线别', {
            'fields': ('line',)
        }),
        ('工作站', 
            {'fields': ('name',)
        }),
    )


# admin_site = EsopAdminSite()

# admin_site.register(Department, DepartmentAdmin)
# admin_site.register(Line, LineAdmin)
# admin_site.register(Station, StationAdmin)
