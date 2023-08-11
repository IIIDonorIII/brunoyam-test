import unittest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database import Student, Course, Base

class TestStudentDatabase(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)
        self.session = self.Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_add_student(self):
        student = Student(name="John", surname="Doe", age=25, city="New York")
        self.session.add(student)
        self.session.commit()

        retrieved_student = self.session.query(Student).filter_by(name="John").first()
        self.assertEqual(retrieved_student.name, "John")

    def test_add_course(self):
        course = Course(name="python")
        self.session.add(course)
        self.session.commit()

        retrieved_course = self.session.query(Course).filter_by(name="python").first()
        self.assertEqual(retrieved_course.name, "python")

    def test_delete_student(self):
        student = Student(name="Alice", surname="Smith", age=28, city="Los Angeles")
        self.session.add(student)
        self.session.commit()

        self.session.delete(student)
        self.session.commit()

        deleted_student = self.session.query(Student).filter_by(name="Alice").first()
        self.assertIsNone(deleted_student)

    def test_add_and_remove_course(self):
        student = Student(name="Bob", surname="Johnson", age=30, city="Chicago")
        course = Course(name="math")
        self.session.add(student)
        self.session.add(course)
        self.session.commit()

        student.add_course(course)
        self.session.commit()

        retrieved_student = self.session.query(Student).filter_by(name="Bob").first()
        self.assertIn(course, retrieved_student.courses)

        student.remove_course(course)
        self.session.commit()

        retrieved_student = self.session.query(Student).filter_by(name="Bob").first()
        self.assertNotIn(course, retrieved_student.courses)

if __name__ == '__main__':
    unittest.main()
