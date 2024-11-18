from django.test import TestCase
from model_bakery import baker
from studyProgram.models import Student, Problem, LessonName, ProgramingLanguage, Submission

# Create your tests here.
class StudentViewTestCase(TestCase):
    def test_get_list_of_students(self):
        student = baker.make("studyProgram.Student")
        r = self.client.get('/api/students/')
        data = r.json()
        assert student.name == data[0]['name']
        assert student.id == data[0]['id']
        assert len(data) == 1

    def test_create_student(self):
        r = self.client.post("/api/students/", {"name": "qwerty", "description": "Петр Петров"})

        new_student_id = r.json()['id']
        students = Student.objects.all()
        assert len(students) == 1

        new_student = Student.objects.filter(id=new_student_id).first()
        assert new_student.name == 'qwerty'
        assert new_student.description == 'Петр Петров'

    def test_delete_student(self):
        students = baker.make("Student", 10)
        r = self.client.get('/api/students/')
        data = r.json()
        assert len(data) == 10 

        student_id_delete = students[3].id
        self.client.delete(f'/api/students/{student_id_delete}/')
        r = self.client.get('/api/students/')
        assert r.status_code == 200
        
        data = r.json()
        assert len(data) == 9
        assert student_id_delete not in [i['id']for i in data]

    def test_update_student(self):
        student = baker.make("Student", 10)
        student: Student = student[0]

        r = self.client.get(f'/api/students/{student.id}/')

        data = r.json()
        assert data['name'] == student.name

        r = self.client.put(
            f'/api/students/{student.id}/',
            {"name": "qwerty", "description": "Петр Петров"},
            content_type='application/json'
        )
        
        assert r.status_code == 200

        r = self.client.get(f'/api/students/{student.id}/' , {"name": "qwerty", "description": "Петр Петров"},  content_type='application/json')
        data = r.json()
        assert data['name'] == "qwerty"

        student.refresh_from_db()
        assert data['name'] == student.name

class ProgramingLanguageViewSetCase(TestCase):
    def test_get_list_programing_languages(self):
        programing_language = baker.make("studyProgram.ProgramingLanguage")
        
        r = self.client.get('/api/programingLanguages/')
        data = r.json()
        
        assert programing_language.name == data[0]['name']
        assert programing_language.id == data[0]['id']
        assert len(data) == 1

    def test_create_programing_language(self):
        r = self.client.post("/api/programingLanguages/", {"name": "R"})

        programing_language_id = r.json()['id']
        programing_languages = ProgramingLanguage.objects.all()
        assert len(programing_languages) == 1

        programing_language = ProgramingLanguage.objects.filter(id=programing_language_id).first()
        assert programing_language.name == 'R'

    def test_delete_programing_language(self):
        programing_languages = baker.make("programingLanguages", 10)
        r = self.client.get('/api/programingLanguages/')
        data = r.json()
        assert len(data) == 10 

        programing_language_id_delete = programing_languages[3].id
        self.client.delete(f'/api/programingLanguages/{programing_language_id_delete}/')
        r = self.client.get('/api/programingLanguages/')
        assert r.status_code == 200
        
        data = r.json()
        assert len(data) == 9
        assert programing_language_id_delete not in [i['id']for i in data]

    def test_update_programing_language(self):
        programing_languages = baker.make("ProgramingLanguage", 10)
        programing_language = programing_languages[0]
        r = self.client.get(f'/api/programingLanguages/{programing_language.id}/')
        data = r.json()
        assert data['name'] == programing_language.name

        r = self.client.put(
            f'/api/programingLanguages/{programing_language.id}/',
            {"name": "qwerty"},
            content_type='application/json'
        )
        assert r.status_code == 200

        r = self.client.get(
            f'/api/programingLanguages/{programing_language.id}/',
            {"name": "qwerty"},
            content_type='application/json'
        )
        data = r.json()
        assert data['name'] == "qwerty"

        programing_language.refresh_from_db()
        assert data['name'] == programing_language.name
    
class LessonNameViewSetCase(TestCase):
    def test_get_list(self):
        lesson_name = baker.make("studyProgram.LessonName")
        r = self.client.get("/api/lessonNames/")
        data = r.json()
        assert lesson_name.name == data[0]["name"]
        assert lesson_name.programing_language == data[0]["programing_language"]
        assert len(data) == 1
    
    def test_create_lesson_name(self):
        pr_language = baker.make("ProgramingLanguage")
        # lesson_name = LessonName.objects.create(name='R',  description='123', programing_language=pr_language)
        r = self.client.post('/api/lessonNames/', {
            "name":'R',
            "description":'123',
            "programing_language":pr_language.id,
        }, content_type='application/json')
        
        assert r.status_code == 201
        new_lesson_name_id = r.json()['id']
        
        lesson_names = LessonName.objects.all()
        assert len(lesson_names) == 1
        
        new_lesson_name = LessonName.objects.filter(id=new_lesson_name_id).first()
        assert new_lesson_name.name == "R"
        assert new_lesson_name.description == '123'
        assert new_lesson_name.programing_language == pr_language
        
         
        r = self.client.get('/api/lessonNames/')
        data = r.json()
        print(data)
        assert 'R' == data[0]['name']
        assert '123' == data[0]['description']
        assert pr_language.id == data[0]['programing_language']['id']
        assert pr_language.name == data[0]['programing_language']["name"]
        assert len(data) == 1
        
    def test_delete_lesson_name(self):
        lesson_names = []
        for i in range(10):
            pr_language = baker.make("ProgramingLanguage")
            lesson_name = LessonName.objects.create(
                name='R' + str(i),
                description='A'+ str(i),
                programing_language=pr_language
            )
            lesson_names.append(lesson_name)
        r = self.client.get("/api/lessonNames/")
        data = r.json()
        assert len(data) == 10
        
        lesson_name_id_to_delete = lesson_names[0].id
        self.client.delete(f"/api/lessonNames/{lesson_name_id_to_delete}/")
        r = self.client.get("/api/lessonNames/")
        assert r.status_code == 200

        data = r.json()
        print(data)
        assert len(data) == 9
        assert lesson_name_id_to_delete not in [i['id']for i in data]    
    
    def test_update_lesson_name(self):
        lesson_names = []
        for i in range(10):
            pr_language = baker.make("ProgramingLanguage")
            lesson_name = LessonName.objects.create(name='R' + str(i), description='A' + str(i), programing_language=pr_language)
            lesson_names.append(lesson_name)

        lesson_name = lesson_names[0]

        # Проверка получения данных
        r = self.client.get(f'/api/lessonNames/{lesson_name.id}/')
        data = r.json()
        assert data['name'] == lesson_name.name
        assert r.status_code == 200

        # Обновление данных с использованием programing_language_id
        r = self.client.put(
            f'/api/lessonNames/{lesson_name.id}/',
            {
                "name": "qwerty",
                "description": lesson_name.description,
                "programing_language_id": lesson_name.programing_language.id,
            },
            content_type='application/json'
        )

        assert r.status_code == 200

        # Проверка, что данные обновились
        data = r.json()
        assert data['name'] == "qwerty"
 
        
        r = self.client.get(f'/api/lessonNames/{lesson_name.id}/')
        data = r.json()
        assert data['name'] == "qwerty"

        lesson_name.refresh_from_db()
        assert data['name'] == lesson_name.name

class ProblemViewSetCase(TestCase):
    def test_get_list(self):
        problem = baker.make(Problem)
        r = self.client.get("/api/problems/")
        data = r.json()
        assert problem.name == data[0]['name']
        assert problem.description == data[0]['description']
        assert problem.lesson_name == data[0]['lesson_name']
        assert len(data) == 1
        
    def test_create_problem(self):
        
        lesson = baker.make(LessonName)
        r = self.client.post("/api/problems/", {
            "name":"name",
            "description":"description",
            "lesson_name":lesson.id
            })
       
        r = self.client.get("/api/problems/")
        data = r.json()
        print(data)
        assert data[0]['name'] =="name"
        assert data[0]['description'] == "description"
        assert data[0]['lesson_name']['id'] == lesson.id
        assert len(data) == 1
        
    def test_delet_problem(self):
        problems = []
        for _ in range(10):
            lesson = baker.make(LessonName)
            problem = Problem.objects.create(
                name="name",
                description="description",
                lesson_name=lesson
            )
            problems.append(problem)
        r = self.client.get("/api/problems/")
        data = r.json()
        assert len(data) == len(problems)
        
        problem_to_delete_id = problems[0].id 
        r = self.client.delete(f"/api/problems/{problem_to_delete_id}/")
        assert r.status_code == 204
        
        r = self.client.get("/api/problems/")
        data = r.json()
        
        assert len(data) == 9
        assert problem_to_delete_id not in [i['id']for i in data]   
         
    def test_update_problem(self):
        problems = []
        for _ in range(10):
            lesson = baker.make(LessonName)
            problem = Problem.objects.create(
                name="name",
                description="description",
                lesson_name=lesson
            )
            problems.append(problem)
        r = self.client.get("/api/problems/")
        data = r.json()
        assert len(data) == len(problems)
        
        problem_to_update = problems[0]
        
        
        updated_data = {
           "name": "qwerty",
            "description": "zxc",
            "lesson_name_id": problem_to_update.lesson_name.id     
        }
                
        r = self.client.put(f"/api/problems/{problem_to_update.id}/", updated_data, content_type='application/json')
        assert r.status_code == 200
        
        
        r = self.client.get(f"/api/problems/{problem_to_update.id}/")        
        assert r.status_code == 200
        data = r.json()
        
        assert data["name"] == updated_data['name']
        assert data["description"] == updated_data['description']
        
        
                
        
class SubmissionViewSetCase(TestCase):
    def test_get_list(self):
        submission = baker.make(Submission)
        r = self.client.get("/api/submissions/")
        data = r.json()
        assert r.status_code == 200
        assert data[0]['status'] == submission.status
        assert data[0]['code'] == submission.code
        # assert data[0]['problem']['id'] == submission.problem.id
        # assert data[0]['user_name']['id'] == submission.user_name.id
    
    def test_create_submission(self):
        student = baker.make(Student)
        problem = baker.make(Problem)
        
        submission = {
            "status":"1",
            "code": "code",
            "problem": problem.id,
            "user_name": student.id
        }
        
        r = self.client.post("/api/submissions/", submission, content_type='application/json')
        assert r.status_code == 201
        
        r = self.client.get("/api/submissions/")
        data = r.json()
        print(data)
        assert r.status_code == 200
        assert data[0]["status"] == submission["status"]
        assert data[0]["code"] == submission["code"]
        assert data[0]["problem"]["id"] == problem.id
        assert data[0]["user_name"]["id"] == student.id
        
    def test_delete_submission(self):
        submissions = []
        for _ in range(10):
            student = baker.make(Student)
            problem = baker.make(Problem)
        
            submission = Submission.objects.create(
                status="1",
                code = "print()",
                problem = problem,
                user_name = student
            )
            submissions.append(submission)
        
        submissions_to_delete_id = submissions[0].id        
        r = self.client.delete(f"/api/submissions/{submissions_to_delete_id}/")
        assert r.status_code == 204
        
        r = self.client.get(f"/api/submissions/{submissions_to_delete_id}/")
        assert r.status_code == 404
        
        r = self.client.get(f"/api/submissions/")
        assert r.status_code == 200
        
        data = r.json()
        assert submissions_to_delete_id not in [i['id']for i in data]
        
    def test_update_submission(self):
        submissions = []
        for _ in range(10):
            student = baker.make(Student)
            problem = baker.make(Problem)
        
            submission = Submission.objects.create(
                status="1",
                code = "print()",
                problem = problem,
                user_name = student
            )
            submissions.append(submission)
        
        submission_to_update = submissions[0]
        
        
        r = self.client.get(f'/api/submissions/{submission_to_update.id}/')
        data = r.json()
        assert data['code'] == submission_to_update.code
        assert r.status_code == 200


        r = self.client.put(
            f'/api/submissions/{submission_to_update.id}/',
            {
                "status": "0",
                "code": submission_to_update.code,
                "problem_id": submission_to_update.problem.id,
                "user_name_id":submission_to_update.user_name.id
            },
            content_type='application/json'
        )
        assert r.status_code == 200
        
        r = self.client.get(f"/api/submissions/{submission_to_update.id}/")
        data = r.json()
        assert r.status_code == 200
        assert data["id"] == submission_to_update.id
        assert data["status"] == "0"
        assert data["code"] == submission_to_update.code
        assert data["problem"]["id"] == submission_to_update.problem.id
        assert data["user_name"]["id"] == submission_to_update.user_name.id
                

        
        