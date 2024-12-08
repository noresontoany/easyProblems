from django.apps import AppConfig


class StudyprogramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studyProgram'
    def ready(self):
        import studyProgram.signals