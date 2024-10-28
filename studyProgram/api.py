from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView

from rest_framework import mixins, viewsets
from rest_framework.response import  Response
#models
from studyProgram.models import Student
from studyProgram.models import Problem
from studyProgram.models import LessonName
from studyProgram.models import ProgramingLanguage
from studyProgram.models import Submission
#serializers
from studyProgram.serializers import StudentSerializer
from studyProgram.serializers import ProblemSerializer
from studyProgram.serializers import LessonNameSerializer
from studyProgram.serializers import ProgramingLanguageSerializer
from studyProgram.serializers import SubmissionSerializer
from studyProgram.serializers import StudentFieldSerializer


class ViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet,
                        mixins.DestroyModelMixin):
    pass

class StudentViewSet(ViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentFieldsView(APIView):
    def get(self, request):
        fields_info = []
        private_fields = ["BigAutoField", "ForeignKey"]
        for field in Student._meta.get_fields():
            if field.get_internal_type() not in private_fields :
                fields_info.append({
                    "verbose": field.verbose_name,
                    "name": field.name,
                    "type" : field.get_internal_type()
                })
        serializer = StudentFieldSerializer(data=fields_info, many=True)
        serializer.is_valid()  # Просто для проверки структуры
        return Response(serializer.data)
        
class ProblemViewSet(ViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class LessonNameViewSet(ViewSet):
    queryset = LessonName.objects.all()
    serializer_class = LessonNameSerializer
    
class ProgramingLanguageViewSet(ViewSet):
    queryset = ProgramingLanguage.objects.all()
    serializer_class = ProgramingLanguageSerializer

class SubmissionViewSet(ViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer