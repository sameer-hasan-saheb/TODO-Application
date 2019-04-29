from django.contrib import admin
from django.http import HttpResponse
from .models import Task
import csv

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Export selected as CSV"

class TaskAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('title', 'slug', 'description', 'date_time', 'created', 'modified', 'is_deleted', 'status')
    list_filter = ('created', 'status', 'is_deleted')
    search_fields = ('title', 'status')
    actions = ["export_as_csv"]

admin.site.register(Task, TaskAdmin)
