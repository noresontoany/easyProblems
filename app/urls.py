"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from studyProgram import views   
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from studyProgram.api import StudentViewSet
from studyProgram.api import ProblemViewSet
from studyProgram.api import LessonNameViewSet
from studyProgram.api import ProgramingLanguageViewSet
from studyProgram.api import SubmissionViewSet
from studyProgram.api import UserProfileViewSet

router = DefaultRouter()
router.register("students", StudentViewSet, basename="students")
router.register("problems", ProblemViewSet, basename="problems")
router.register("lessonNames", LessonNameViewSet, basename="lessonNames")
router.register("programingLanguages", ProgramingLanguageViewSet, basename="programingLanguages")
router.register("submissions", SubmissionViewSet, basename="submissions")
router.register("user", UserProfileViewSet, basename="user")

urlpatterns = [
    path('students/', views.ShowStudentView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
