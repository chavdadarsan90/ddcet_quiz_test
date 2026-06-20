from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import DDCETQuestion

@admin.register(DDCETQuestion)
class DDCETQuestionAdmin(ImportExportModelAdmin):
    pass