from django.db import models

# Create your models here.
class ProgramingLanguage(models.Model): 
    name = models.TextField("Название языка")
    def __str__(self) -> str:
        return self.name
    
class LessonName(models.Model):
    name = models.TextField("Название темы")
    description = models.TextField("Теория")
    programing_language = models.ForeignKey("ProgramingLanguage", on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return self.name

class Problem(models.Model):
    name  = models.TextField("Название задачи")
    description = models.TextField("Условие")
    lesson_name = models.ForeignKey("LessonName", on_delete=models.CASCADE, null=True)
    programing_language = models.ForeignKey("ProgramingLanguage", on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    name  = models.TextField("Ник")
    description = models.TextField("Имя Фамилия")
    def __str__(self) -> str:
        return self.name
    
class Submission(models.Model):
    status_code = [
    ("2", "WAIT"),
    ("1", "OK"),
    ("0", "FAIL"),
]
    status = models.CharField(max_length=1, choices=status_code, default='2')
    code = models.TextField()
    problem  = models.ForeignKey("Problem", on_delete=models.CASCADE, null=True)
    user_name = models.ForeignKey("Student", on_delete=models.CASCADE, null=True)
    