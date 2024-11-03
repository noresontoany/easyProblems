from django.db import models

# Create your models here.
class ProgramingLanguage(models.Model): 
    name = models.TextField("Название языка")
    class Meta:
        verbose_name = "Язык программирования"
        verbose_name_plural = "Языки программирования"
    def __str__(self) -> str:
        return self.name
    
class LessonName(models.Model):
    name = models.TextField("Название темы")
    description = models.TextField("Теория")
    programing_language = models.ForeignKey("ProgramingLanguage", on_delete=models.CASCADE, null=True)
    picture = models.ImageField("Изображение", null=True, upload_to="students")
    class Meta:
        verbose_name = "Название урока"
        verbose_name_plural = "Названия уроков"
    def __str__(self) -> str:
        return f"{self.programing_language.name} / {self.name}"

class Problem(models.Model):
    name  = models.TextField("Название задачи")
    description = models.TextField("Условие")
    lesson_name = models.ForeignKey("LessonName", on_delete=models.CASCADE, null=True)  
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
    def __str__(self) -> str:
        return self.name
    # def __str__(self) -> str:
    #     return f"{self.lesson_name.programing_language.name} /  {self.lesson_name.name} / {self.name}"

class Student(models.Model):
    name  = models.TextField("Ник")
    description = models.TextField("Имя Фамилия")
    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"
    def __str__(self) -> str:
        return self.name
    
class Submission(models.Model):
    status_code = [
    ("2", "WAIT"),
    ("1", "OK"),
    ("0", "FAIL"),
]
    status = models.CharField("Статус", max_length=1, choices=status_code, default='2')
    code = models.TextField()
    problem  = models.ForeignKey("Problem", on_delete=models.CASCADE, null=True)
    user_name = models.ForeignKey("Student", on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"
    def __str__(self) -> str:
        return self.status
