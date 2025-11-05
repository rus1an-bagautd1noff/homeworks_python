import pytest
from db_connection import session
from sqlalchemy import delete
from models import Student


@pytest.fixture(autouse=True)
def clear_data():
    yield
    session.execute(delete(Student))
    session.commit()


def test_add_student():
    new_student = Student(name="Test Student", age=20)
    session.add(new_student)
    session.commit()

    student = session.query(Student).filter_by(name="Test Student").first()
    assert student is not None
    assert student.age == 20


def test_update_student():
    new_student = Student(name="Update Test", age=21)
    session.add(new_student)
    session.commit()

    student_id = new_student.id

    student = session.query(Student).get(student_id)
    student.age = 22
    session.commit()

    updated_student = session.query(Student).get(student_id)
    assert updated_student.age == 22


def test_delete_student():
    new_student = Student(name="Delete Test", age=23)
    session.add(new_student)
    session.commit()

    student_id = new_student.id

    student = session.query(Student).get(student_id)
    session.delete(student)
    session.commit()

    deleted_student = session.query(Student).get(student_id)
    assert deleted_student is None
