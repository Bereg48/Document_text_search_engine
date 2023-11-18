# Document_text_search_engine

## Предназначение приложения:
- сервис принимает на вход произвольный текстовый запрос, ищет по тексту документа в индексе и возвращает первые 20 документов со всем полями БД, упорядоченные по дате создания;
- удаляет документ из БД и индекса по полю

### 1. Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости с помощью группы команд:
    Команда для Windows:
        1- python -m venv venv
        2- venv\Scripts\activate
        3- pip install -r requirements.txt

    Команда для Unix:
        1- python3 -m venv venv
        2- source venv/bin/activate 
        3- pip install -r requirements.txt

### 2. Для запуска приложения: 
    Команда для Windows:
    - python manage.py runserver

    Команда для Unix:
    - python3 manage.py runserver
