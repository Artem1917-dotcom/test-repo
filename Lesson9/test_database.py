import pytest
from sqlalchemy.exc import IntegrityError
from models import Student, Subject

class TestDatabaseOperations:
    """Тесты для операций с базой данных"""
    
    
    def test_create_student(self, db_session, test_student_data):
        """Тест добавления студента в БД"""
        new_student = Student(**test_student_data)
        db_session.add(new_student)
        db_session.commit()
        student_from_db = db_session.query(Student).filter_by(
            email=test_student_data["email"]
        ).first()
        
        assert student_from_db is not None
        assert student_from_db.name == test_student_data["name"]
        assert student_from_db.email == test_student_data["email"]
        assert student_from_db.is_deleted == False
        assert student_from_db.deleted_at is None
        
        db_session.delete(student_from_db)
        db_session.commit()
    def test_create_student_duplicate_email(self, db_session, test_student_data):
        """Негативный тест: попытка создания студента с дублирующимся email"""
        student1 = Student(**test_student_data)
        db_session.add(student1)
        db_session.commit()
        student2 = Student(**test_student_data)
        db_session.add(student2)
        with pytest.raises(IntegrityError):
            db_session.commit()
        db_session.rollback()
        db_session.delete(student1)
        db_session.commit()
    def test_update_student(self, db_session, test_student_data):
        """Тест изменения данных студента"""
        student = Student(**test_student_data)
        db_session.add(student)
        db_session.commit()
        
        new_name = "Петр Петров"
        student.name = new_name
        db_session.commit()
        
        updated_student = db_session.query(Student).filter_by(
            email=test_student_data["email"]
        ).first()
        
        assert updated_student.name == new_name
        assert updated_student.updated_at is not None
        
        db_session.delete(updated_student)
        db_session.commit()
    
    def test_update_subject(self, db_session, test_subject_data):
        """Тест изменения предмета"""
        subject = Subject(**test_subject_data)
        db_session.add(subject)
        db_session.commit()
        
        new_description = "Линейная алгебра и математический анализ"
        subject.description = new_description
        db_session.commit()
        
        updated_subject = db_session.query(Subject).filter_by(
            name=test_subject_data["name"]
        ).first()
        
        assert updated_subject.description == new_description
        

        db_session.delete(updated_subject)
        db_session.commit()
    
    
    def test_soft_delete_student(self, db_session, test_student_data):
        """Тест мягкого удаления студента"""
        from datetime import datetime
        
        student = Student(**test_student_data)
        db_session.add(student)
        db_session.commit()
        
        student.is_deleted = True
        student.deleted_at = datetime.now()
        db_session.commit()
        
        deleted_student = db_session.query(Student).filter_by(
            email=test_student_data["email"]
        ).first()
        
        assert deleted_student.is_deleted == True
        assert deleted_student.deleted_at is not None
        
        active_students = db_session.query(Student).filter_by(
            is_deleted=False
        ).all()
        
        student_in_active = any(
            s.email == test_student_data["email"] for s in active_students
        )
        assert student_in_active == False
        
        db_session.delete(deleted_student)
        db_session.commit()
    
    def test_hard_delete_subject(self, db_session, test_subject_data):
        """Тест полного удаления предмета"""
        subject = Subject(**test_subject_data)
        db_session.add(subject)
        db_session.commit()
        
        subject_id = subject.id
        
        db_session.delete(subject)
        db_session.commit()
        deleted_subject = db_session.query(Subject).filter_by(
            id=subject_id
        ).first()
           
        assert deleted_subject is None 
    
    def test_create_subject(self, db_session, test_subject_data):
        """Тест добавления предмета"""
        subject = Subject(**test_subject_data)
        db_session.add(subject)
        db_session.commit()
        
        subject_from_db = db_session.query(Subject).filter_by(
            name=test_subject_data["name"]
        ).first()
        
        assert subject_from_db is not None
        assert subject_from_db.description == test_subject_data["description"]
        
        db_session.delete(subject_from_db)
        db_session.commit()