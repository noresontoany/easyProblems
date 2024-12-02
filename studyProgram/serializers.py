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
    def create(self, validated_data): 
        # когда в api создается сериалайзер, 
        # то заполняется специальное поле сериалайзера которое называется context
        # в него добавляется инфомрация по запросе, и доступна эта инфа
        # через self.context['request'], в частности там есть информация о пользовате
        if 'request' in self.context:
            # заполняем validated_data который используется для создания сущности в БД
            # данными из запроса
            validated_data['user'] = self.context['request'].user
            
        return super().create(validated_data)
    class  Meta:
        model = Student
        fields = ['id', 'name', 'description', 'user']
        
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
        
