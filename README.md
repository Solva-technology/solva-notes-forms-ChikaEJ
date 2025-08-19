[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=20106047&assignment_repo_type=AssignmentRepo)
# Note App — Часть #3: Формы (CRUD)

Текущая цель — добавить возможность **создания, изменения и удаления заметок** с помощью Django Forms.  

---

## Описание проекта

**Note App** — учебное Django-приложение для работы с заметками.  

Проект уже включает:  
- админку и локализацию;  
- список заметок (главная), страницу отдельной заметки;  
- базовый шаблон `base.html`;  
- запуск в Docker + PostgreSQL.  

На этом этапе вы реализуете **CRUD для модели `Note`** через формы и шаблоны.  

---

## Новые страницы (CRUD)

### 1. Создание заметки
- **URL:** `/notes/create/`  
- Форма для добавления заметки.  
- Поля: `text`, `status`, `categories`, `author`.  
- После успешного создания → редирект на главную.  

### 2. Редактирование заметки
- **URL:** `/notes/<int:note_id>/edit/`  
- Форма с предзаполненными данными.  
- После сохранения → редирект на страницу заметки.  

### 3. Удаление заметки
- **URL:** `/notes/<int:note_id>/delete/`  
- Страница подтверждения удаления.  
- После удаления → редирект на главную.  

---

## Требования

- Использовать Django **ModelForm**.  
- Все страницы форм наследуются от `base.html`.  
- Ошибки валидации отображаются в шаблоне.  
- Авторизация пока не требуется.  
- Ранее сделанные страницы (список заметок, страница пользователя и т.д.) должны остаться рабочими.
- Весь функцилнал визуально отображается на сайте в виде ссылок в шапе или у объекта.

---

## Структура проекта (пример)

```
note_app/
├── notes/
│   ├── templates/notes/
│   │   ├── note_form.html
│   │   ├── note_confirm_delete.html
│   │   ├── note_detail.html
│   │   └── note_list.html
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── templates/base.html
├── docker-compose.yml
├── Dockerfile
└── .env.example
```

---
