from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from studyProgram.models import Student
from studyProgram.serializers import StudentSerializer



class StudentViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    