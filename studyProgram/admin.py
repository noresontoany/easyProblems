from django.contrib import admin
from studyProgram.models import ProgramingLanguage, LessonName, Problem
from studyProgram.models import Student, Submission

# Register your models here.
@admin.register(ProgramingLanguage)
class ProgramingLanguageAdmin(admin.ModelAdmin):
    pass
@admin.register(LessonName)
class LessonNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'programing_language']

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'lesson_name']
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['status', 'code', 'problem', 'user_name']