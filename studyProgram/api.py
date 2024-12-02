from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.contrib.auth.models import User

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
from studyProgram.serializers import ProblemSerializer, ProblemGetSerializer

from studyProgram.serializers import LessonNameSerializer, LessonNameGetSerializer

from studyProgram.serializers import ProgramingLanguageSerializer

from studyProgram.serializers import SubmissionSerializer, SubmissionGetSerializer

from studyProgram.serializers import RelatedInfoFieldSerializer



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
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     # фильтруем по текущему юзеру
    #     qs = qs.filter(user=self.request.user)
    @action(detail=False, methods=['get'], url_path='fields')
    def fields(self, request, *args, **kwargs):        
        fields_info = get_model_fields_info(Student)
        serializer = RelatedInfoFieldSerializer(data=fields_info, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    # def get(self, request):
    #     fields_info = []
    #     private_fields = ["BigAutoField", "ForeignKey"]
    #     for field in Student._meta.get_fields():
    #         if field.get_internal_type() not in private_fields :
    #             fields_info.append({
    #                 "verbose": field.verbose_name,
    #                 "name": field.name,
    #                 "type" : field.get_internal_type()
    #             })
    #     serializer = RelatedInfoFieldSerializer(data=fields_info, many=True)
    #     serializer.is_valid()  # Просто для проверки структуры
    #     return Response(serializer.data)
        
        
        
class UserProfileViewSet(GenericViewSet):
    @action(url_path="info", detail=False, methods=["GET"])
    def get_url(self, request, *args, **kwargs):
        user = request.user
        data ={
            "is_authenticated" : user.is_authenticated
        }
        if user.is_authenticated:
            data.update({
                "is_super": user.is_superuser,
                "name": user.username
            })
        return Response(data)
    
class ProblemViewSet(ViewSet):
    queryset = Problem.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProblemGetSerializer   
        return ProblemSerializer
    @action(detail=False, methods=['get'], url_path='fields')
    def fields(self, request, *args, **kwargs):        
        fields_info = get_model_fields_info(Problem)
        serializer = RelatedInfoFieldSerializer(data=fields_info, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    

class LessonNameViewSet(ViewSet):
    queryset = LessonName.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LessonNameGetSerializer   
        return LessonNameSerializer
    
    @action(detail=False, methods=['get'], url_path='fields')
    def fields(self, request, *args, **kwargs):        
        fields_info = get_model_fields_info(LessonName)
        serializer = RelatedInfoFieldSerializer(data=fields_info, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    
class ProgramingLanguageViewSet(ViewSet):
    queryset = ProgramingLanguage.objects.all()
    serializer_class = ProgramingLanguageSerializer
    @action(detail=False, methods=['get'], url_path='fields')
    def fields(self, request, *args, **kwargs):        
        fields_info = get_model_fields_info(ProgramingLanguage)
        serializer = RelatedInfoFieldSerializer(data=fields_info, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class SubmissionViewSet(ViewSet):
    queryset = Submission.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return SubmissionGetSerializer
        return SubmissionSerializer
    
    @action(detail=False, methods=['get'], url_path='fields')
    def fields(self, request, *args, **kwargs):        
        fields_info = get_model_fields_info(Submission)
        serializer = RelatedInfoFieldSerializer(data=fields_info, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)




def get_model_fields_info(model):
    fields_info = []
    private_fields = ["BigAutoField"]

    for field in model._meta.get_fields():
        if not field.auto_created and field.get_internal_type() not in private_fields and field.verbose_name != "Пользователь":
            field_data = {
                "verbose": field.verbose_name,
                "name": field.name,
                "type": field.get_internal_type()
            }
            if field.choices:
                field_data["type"] = "choiceList"
                related_info = {
                    "related_verbose_name": field.verbose_name,
                    "related_model_id": field.name,
                    "options": [
                        {"id": ch[0], "verbose": ch[1]}
                        for ch in field.choices
                    ]
                }
                field_data["related_info"] = related_info
            elif field.get_internal_type() == "ForeignKey": 
                field_data["type"] = "choice"
                related_model = field.related_model
                related_field = related_model._meta.get_field("name")
                field_data["verbose"] = related_field.verbose_name

                related_info = {
                    "related_verbose_name": related_field.verbose_name,
                    "related_model_id": field.name,
                    "options": [
                        {"id": related_instance.id, "verbose": str(related_instance)}
                        for related_instance in related_model.objects.all()
                    ]
                }
                field_data["related_info"] = related_info

            fields_info.append(field_data)
    
    return fields_info
                        
                    
