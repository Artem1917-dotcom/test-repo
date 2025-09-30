import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models import Base, Student, Subject

@pytest.fixture(scope="function")
def db_session():
    """Фикстура для создания сессии БД"""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)  # Создаем таблицы
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session  # Передаем сессию тесту
    
    # Cleanup - откатываем изменения и закрываем сессию
    session.rollback()
    session.close()

@pytest.fixture
def test_student_data():
    """Тестовые данные для студента"""
    return {
        "name": "Иван Иванов",
        "email": "ivan@test.ru"
    }

@pytest.fixture
def test_subject_data():
    """Тестовые данные для предмета"""
    return {
        "name": "Математика",
        "description": "Высшая математика и анализ"
    }