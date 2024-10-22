from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from studyProgram.models import Student, Problem, LessonName, ProgramingLanguage, Submission
from studyProgram.serializers import StudentSerializer, ProblemSerializer, LessonNameSerializer, ProgramingLanguageSerializer, SubmissionSerializer



class StudentViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ProblemViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet,mixins.DestroyModelMixin):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class LessonNameViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet,
                        mixins.DestroyModelMixin):
    queryset = LessonName.objects.all()
    serializer_class = LessonNameSerializer
    
class ProgramingLanguageViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet,mixins.DestroyModelMixin):
    queryset = ProgramingLanguage.objects.all()
    serializer_class = ProgramingLanguageSerializer

class SubmissionViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet,mixins.DestroyModelMixin):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer