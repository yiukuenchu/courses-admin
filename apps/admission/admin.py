from django.contrib import admin
from .models import Course, Intake

# Register your models here.
class IntakeInline(admin.TabularInline):
    model = Intake
    extra = 1
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [IntakeInline]

@admin.register(Intake)
class IntakeAdmin(admin.ModelAdmin):
    list_display = ('course', 'start_date', 'end_date')