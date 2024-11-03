from rest_framework import serializers

from studyProgram.models import Student, Problem, Submission, LessonName, ProgramingLanguage



class RelatedInfoSerializer(serializers.Serializer):
    # related_verbose_name = serializers.CharField()
    # related_model_id = serializers.CharField()
    options = serializers.ListField(child=serializers.DictField())


class RelatedInfoFieldSerializer(serializers.Serializer):
    verbose = serializers.CharField()
    name = serializers.CharField()
    type = serializers.CharField()
    related_info = RelatedInfoSerializer(required=False) 




#student
#================================================================

class StudentSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Student
        fields = ['id', 'name', 'description']
        
#ProgramingLanguage
#================================================================
    
class ProgramingLanguageSerializer(serializers.ModelSerializer):
    class  Meta:
        model = ProgramingLanguage
        fields = ['id', 'name']
#lessonNames
#================================================================

class LessonNameGetSerializer(serializers.ModelSerializer):
    programing_language = ProgramingLanguageSerializer(read_only=True)
    class Meta:
        model = LessonName
        fields = ['id', 'name', 'description', 'programing_language','picture']

class LessonNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonName
        fields = ['id', 'name', 'description', 'programing_language', 'picture']
        
#Problem
#================================================================    
    
class ProblemGetSerializer(serializers.ModelSerializer):
    lesson_name = LessonNameGetSerializer(read_only=True)
    class Meta:
        model = Problem
        fields = ['id', 'name', 'description','lesson_name']

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id', 'name', 'description','lesson_name']

#Submission
#================================================================    

class SubmissionGetSerializer(serializers.ModelSerializer):
    problem = ProblemGetSerializer(read_only=True)
    user_name = StudentSerializer(read_only=True)
    class  Meta:
        model =  Submission
        fields = ['id', 'status', 'code', 'problem', 'user_name']
        
                
class SubmissionSerializer(serializers.ModelSerializer):
    class  Meta:
        model =  Submission
        fields = ['id', 'status', 'code', 'problem', 'user_name']
        
