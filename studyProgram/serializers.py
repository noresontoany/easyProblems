from rest_framework import serializers

from studyProgram.models import Student, Problem, Submission, LessonName, ProgramingLanguage

class StudentSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Student
        fields = ['id', 'name', 'description']

class ProgramingLanguageSerializer(serializers.ModelSerializer):
    class  Meta:
        model = ProgramingLanguage
        fields = ['id', 'name']

class LessonNameSerializer(serializers.ModelSerializer):
    programing_language = ProgramingLanguageSerializer()
    class  Meta:
        model = LessonName
        fields = ['id', 'name','description','programing_language']
        
class  SubmissionSerializer(serializers.ModelSerializer):
    class  Meta:
        model =  Submission
        fields = ['id', 'status']
class ProblemSerializer(serializers.ModelSerializer):
    lesson_name = LessonNameSerializer()
    class  Meta:
        model = Problem
        fields = ['id', 'name','description', 'lesson_name']