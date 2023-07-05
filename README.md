# Books 
### Запуск проекта
- Клонировать репозиторий
```
git clone https://github.com/borrrv/books.git
```
- Установить и запустить виртуальное окружение
```
python -m venv env
source env/Scripts/activate
```
- Установить зависимости
```
pip install -r requirements.txt
```
- Переименовать файл ```.env_example``` в ```.env```
- Создать в postgres таблицу ```books``` и пользователя ```books_author``` с паролем ```books_password```(либо создать свою таблицу и имзенить значения в файле ```.env```)
- Создать и применить миграции
```
python manage.py makemigrations
python manage.py migrate
```
- Запустить локально
```
python manage.py runserver
```
### Эндопинты относительно ```http://127.0.0.1:8000/```
- (POST) Регистрация пользователя
```
/api/auth/authors/
```
Пример запроса:
```
{
    "email": "test@ya.ru",
    "password": "Qweasdzxc1!",
    "first_name": "test",
    "last_name": "test last name"
}
```
- (POST) Получить токен
```
/api/auth/jwt/create/
```
Пример запроса:
```
{
    "email": "test@ya.ru",
    "password": "Qweasdzxc1!"
}
```
#### Для редактирования, создания постов, удаления требуется передавать токен при каждом запросе
```
Bearer {You token}
```
- (GET, POST) CRUD для книг с указанием авторов и количетсовм комментариев к этой книге
```
/api/books/
```
- (GET, PATCH, DELETE) Получение конкретной книги (Если автор, то можно редактировать и удалять)
```
/api/books/<int>/
```
- (GET) Список авторов с указанием кол-ва книг и кол-ва комментариев
```
/api/auth/authors/
```
- (PATCH, DELETE) Изменение и удаление текущего профиля + получение книг автора текущего пользователя
```
/api/auth/authors/me/
```
- (GET) Получение списка книг выбранного автора (только те книги, которые не являются заархивированными)
```
/api/books/1/authors/
```
- (GET) Получение списка книг (только те книги, которые не являются заархивированными)
```
/api/books/not_archived/
```
- (PATCH) Изменение флага archived
```
/api/books/1/archived/
```
Пример запроса:
```
{
    "archived": "True"
}
```
- (POST) Создание комментария к книге
```
/api/books/1/comment/
```
Пример запроса:
```
{
    "text": "second comment"
}
```
- (PATCH, DELETE) Редактировать, удалить комментарий (если пользователь является автором комментария)
```
/api/comments/7/
```
