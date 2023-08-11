import curses
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///students_courses.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

student_courses = Table('student_courses', Base.metadata,
    Column('student_id', ForeignKey('Students.id'), primary_key=True),
    Column('course_id', ForeignKey('Courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'Students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    city = Column(String, nullable=False)

    courses = relationship("Course", secondary="student_courses")

    def __repr__(self):
        return f"<Student(name='{self.name}', surname='{self.surname}', age='{self.age}', city='{self.city}')>"
    
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
    
    def get_students_over_30():
        session = Session()
        students = session.query(Student).filter(Student.age > 30).all()
        session.close()
        return students

    def get_students_on_python_course():
        session = Session()
        students = session.query(Student).join(Student.courses).filter(curses.name == 'python').all()
        session.close()
        return students

    def get_students_on_python_course_in_spb():
        session = Session()
        students = session.query(Student).join(Student.courses).filter(Course.name == 'python', Student.city == 'Spb').all()
        session.close()
        return students
