from django.test import TestCase
from model_bakery import baker
from studyProgram.models import Student, Problem, LessonName, ProgramingLanguage, Submission

# Create your tests here.
class StudentViewTestCase(TestCase):
    def test_list(self):
        self.assertEqual(2, 2)

    def test_get_list(self):
        student = baker.make("studyProgram.Student")
        r = self.client.get('/api/StudentViewSet/')
        data = r.json()
        print(data)
        print(data[0]['name'])
        print(data[0]['id'])
        print("====================")
        print(student.name)
        print(student.id)
        print(len(data))
        assert student.name == data[0]['name']
        assert student.id == data[0]['id']
        assert len(data) == 1


    def test_create_student(self):
        r = self.client.post("/api/StudentViewSet/", {"name": "qwerty", "description": "Петр Петров"})

        new_student_id = r.json()['id']

        students = Student.objects.all()
        assert len(students) == 1

        new_student = Student.objects.filter(id=new_student_id).first()
        print("=======================================================================")

        print(f"new_student.name = {new_student.name} ")
        print(f"new_student.description = {new_student.description} ")

        print("=======================================================================")
        
        assert new_student.name == 'qwerty'
        assert new_student.description == 'Петр Петров'

    def test_delete_student(self):
        students = baker.make("Student", 10)
        r = self.client.get('/api/StudentViewSet/')
        data = r.json()
        assert len(data) == 10 

        student_id_delete = students[3].id
        self.client.delete(f'/api/StudentViewSet/{student_id_delete}/')
        r = self.client.get('/api/StudentViewSet/')
        assert r.status_code == 200
        
        data = r.json()
        assert len(data) == 9
        assert student_id_delete not in [i['id']for i in data]



    def test_update_student(self):
        student = baker.make("Student", 10)
        student: Student = student[0]
        print(student.id, "===========")
        print(student.name, "===========")
        r = self.client.get(f'/api/StudentViewSet/{student.id}/')
        data = r.json()
        assert data['name'] == student.name

        r = self.client.put(f'/api/StudentViewSet/{student.id}/' , {"name": "qwerty", "description": "Петр Петров"}, content_type='application/json')
        assert r.status_code == 200

        r = self.client.get(f'/api/StudentViewSet/{student.id}/' , {"name": "qwerty", "description": "Петр Петров"},  content_type='application/json')
        data = r.json()
        assert data['name'] == "qwerty"

        student.refresh_from_db()
        assert data['name'] == student.name

class ProgramingLanguageViewSetCase(TestCase):
    def test_get_list(self):
        programing_language = baker.make("studyProgram.ProgramingLanguage")
        r = self.client.get('/api/ProgramingLanguageViewSet/')
        data = r.json()
        assert programing_language.name == data[0]['name']
        assert programing_language.id == data[0]['id']
        assert len(data) == 1

        

    def test_create_programing_language(self):
        r = self.client.post("/api/ProgramingLanguageViewSet/", {"name": "R"})

        programing_language_id = r.json()['id']
        programing_languages = ProgramingLanguage.objects.all()
        assert len(programing_languages) == 1

        programing_language = ProgramingLanguage.objects.filter(id=programing_language_id).first()
        assert programing_language.name == 'R'

    def test_delete_student(self):
        programing_languages = baker.make("ProgramingLanguage", 10)
        r = self.client.get('/api/ProgramingLanguageViewSet/')
        data = r.json()
        assert len(data) == 10 

        programing_language_id_delete = programing_languages[3].id
        self.client.delete(f'/api/ProgramingLanguageViewSet/{programing_language_id_delete}/')
        r = self.client.get('/api/ProgramingLanguageViewSet/')
        assert r.status_code == 200
        
        data = r.json()
        assert len(data) == 9
        assert programing_language_id_delete not in [i['id']for i in data]


    def test_update_student(self):
        programing_languages = baker.make("ProgramingLanguage", 10)
        programing_language = programing_languages[0]
        r = self.client.get(f'/api/ProgramingLanguageViewSet/{programing_language.id}/')
        data = r.json()
        assert data['name'] == programing_language.name

        r = self.client.put(f'/api/ProgramingLanguageViewSet/{programing_language.id}/' , {"name": "qwerty"}, content_type='application/json')
        assert r.status_code == 200

        r = self.client.get(f'/api/ProgramingLanguageViewSet/{programing_language.id}/' , {"name": "qwerty"},  content_type='application/json')
        data = r.json()
        assert data['name'] == "qwerty"

        programing_language.refresh_from_db()
        assert data['name'] == programing_language.name
    
    

class LessonNameViewSetCase(TestCase):
    def test_get_list(self):
        lesson_name = baker.make("studyProgram.LessonName")
        r = self.client.get("/api/LessonNameViewSet/")
        data = r.json()
        assert len(data) == 1
    
    def test_create_lesson_name(self):
        pr_language = baker.make("ProgramingLanguage")
        lesson_name = LessonName.objects.create(name='R',  description='123', programing_language=pr_language)
        
        r = self.client.get('/api/LessonNameViewSet/')
        data = r.json()
        assert lesson_name.name == data[0]['name']
        assert lesson_name.description == data[0]['description']
        assert lesson_name.id == data[0]['id']
        assert lesson_name.programing_language.id == data[0]['programing_language']['id']
        assert len(data) == 1
    
    def test_delete_lesson_name(self):
        lesson_names = []
        for i in range(10):
            pr_language = baker.make("ProgramingLanguage")
            lesson_name = LessonName.objects.create(name='R' + str(i),  description='A'+ str(i), programing_language=pr_language.id)
            lesson_names.append(lesson_name)
        r = self.client.get("/api/LessonNameViewSet/")
        data = r.json()
        assert len(data) == 10
        
        lesson_name_id_to_delete = lesson_names[0].id
        self.client.delete(f"/api/LessonNameViewSet/{lesson_name_id_to_delete}/")
        r = self.client.get("/api/LessonNameViewSet/")
        assert r.status_code == 200

        data = r.json()
        print(data)
        assert len(data) == 9
        assert lesson_name_id_to_delete not in [i['id']for i in data]    
    
    def test_update_lesson_name(self):
        lesson_names = []
        for i in range(10):
            pr_language = baker.make("ProgramingLanguage")
            lesson_name = LessonName.objects.create(name='R' + str(i),  description='A'+ str(i), programing_language=pr_language.id)
            lesson_names.append(lesson_name)
        
        lesson_name = lesson_names[0]

        r = self.client.get(f'/api/LessonNameViewSet/{lesson_name.id}/')
        data = r.json()
        assert data['name'] == lesson_name.name
        assert r.status_code == 200
        
        r = self.client.put(f'/api/LessonNameViewSet/{lesson_name.id}/' , {"name": "qwerty"} , content_type='application/json')
        assert r.status_code == 200
        
        # r = self.client.get(f'/api/LessonNameSet/{lesson_name.id}/' , content_type='application/json')
        # data = r.json()
        # assert data['name'] == "qwerty"

        # lesson_name.refresh_from_db()
        # assert data['name'] == lesson_name.name





class ProblemViewSetCase(TestCase):
    def test_get_list(self):
        problem = baker.make(Problem)
        r = self.client.get("/api/ProblemViewSet/")
        data = r.json()
        assert problem.name == data[0]['name']
        assert problem.description == data[0]['description']
        assert problem.lesson_name == data[0]['lesson_name']
        assert len(data) == 1

        
        