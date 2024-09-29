from typing import Any
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from studyProgram.models import Student, Problem, Submission, LessonName, ProgramingLanguage


# Create your views here.

class ShowStudentView(TemplateView):
    template_name = "show_students.html"

    def get_context_data(request, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()

        return context

# class ShowProblemView(View):
#     def get(request, *args, **kwargs):
#         problems = Problem.objects.all()
#         result = ""
#         for s in problems:
#             result  += s.name + "<br>"

#         return HttpResponse(result)

# class ShowSubmissionView(View):
#     def get(request, *args, **kwargs):
#         submissions = Submission.objects.all()
#         result = ""
#         for s in submissions:
#             result  += str(s.status) + " " + s.problem + "<br>"

#         return HttpResponse(result)


# class ShowLessonNameView(View):
#     def get(request, *args, **kwargs):
#         lesson_names = LessonName.objects.all()
#         result = ""
#         for s in lesson_names:
#             result  += s.name + "<br>"

#         return HttpResponse(result)

# class ShowProgramingLanguageView(View):
#     def get(request, *args, **kwargs):
#         programing_languages = ProgramingLanguage.objects.all()
#         result = ""
#         for s in programing_languages:
#             result  += s.name + "<br>"

#         return HttpResponse(result)



# def show_students(request):
#     return HttpResponse("Привет !!")