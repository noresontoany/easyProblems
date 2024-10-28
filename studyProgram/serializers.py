from rest_framework import serializers

from studyProgram.models import Student, Problem, Submission, LessonName, ProgramingLanguage

class StudentSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Student
        fields = ['id', 'name', 'description']
class StudentFieldSerializer(serializers.Serializer):
    verbose = serializers.CharField()
    name = serializers.CharField()
    type = serializers.CharField()
    
class ProgramingLanguageSerializer(serializers.ModelSerializer):
    class  Meta:
        model = ProgramingLanguage
        fields = ['id', 'name']

class LessonNameSerializer(serializers.ModelSerializer):
    programing_language = ProgramingLanguageSerializer(read_only=True)
    programing_language_id = serializers.PrimaryKeyRelatedField(
        queryset=ProgramingLanguage.objects.all(),
        source='programing_language',
        write_only=True
    )

    class Meta:
        model = LessonName
        fields = ['id', 'name', 'description', 'programing_language', 'programing_language_id']
    
# class LessonNameSerializer(serializers.ModelSerializer):
#     programing_language = ProgramingLanguageSerializer()
#     class  Meta:
#         model = LessonName
#         fields = ['id', 'name','description','programing_language']
        

class ProblemSerializer(serializers.ModelSerializer):
    lesson_name = LessonNameSerializer(read_only=True)
    lesson_name_id = serializers.PrimaryKeyRelatedField(
        queryset = LessonName.objects.all(),
        source='lesson_name',
        write_only=True
    )
    class Meta:
        model = Problem
        fields = ['id', 'name', 'description','lesson_name','lesson_name_id']
        
# class ProblemSerializer(serializers.ModelSerializer):
#     lesson_name = LessonNameSerializer()
#     class  Meta:
#         model = Problem
#         fields = ['id', 'name','description', 'lesson_name']
class SubmissionSerializer(serializers.ModelSerializer):
    problem = ProblemSerializer(read_only=True)
    user_name = StudentSerializer(read_only=True)
    problem_id = serializers.PrimaryKeyRelatedField(
        queryset = Problem.objects.all(),
        source='problem',
        write_only=True
    )
    user_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Student.objects.all(),
        source='student',
        write_only=True
    )
    class  Meta:
        model =  Submission
        fields = ['id', 'status', 'code', 'problem', 'problem_id', 'user_name', 'user_name_id']                
