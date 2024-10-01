from rest_framework import serializers

from studyProgram.models import Student, Problem, Submission, LessonName, ProgramingLanguage

class StudentSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Student
        fields = ['id', 'name']

class ProblemSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Problem
        fields = ['id', 'name']

class LessonNameSerializer(serializers.ModelSerializer):
    class  Meta:
        model = LessonName
        fields = ['id', 'name']

class ProgramingLanguageSerializer(serializers.ModelSerializer):
    class  Meta:
        model = ProgramingLanguage
        fields = ['id', 'name']

class  SubmissionSerializer(serializers.ModelSerializer):
    class  Meta:
        model =  Submission
        fields = ['id', 'status']