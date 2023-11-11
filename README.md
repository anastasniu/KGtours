# KGtours
Final project: Booking trips around Kyrgyzstan
Django Project Configuration

Чтобы запустить проект следуйте данной инструкции:

1. Склонируйте репозиторий проекта:
   
git clone https://github.com/anastasniu/KGtours

2. Далее нужно создать виртуальное окружение и активировать его:

python -m venv venv
venv/Scripts/activate

3. скачайте необходимые бибилиотеки:

pip install -r requirements.txt

4. Создайте .env file в вашем проекте и установить поднастройки django (SECRET_KEY, DEBUG)

vim .env




## Environment Variables

This project uses environment variables for configuration. Create a .env file in the project's root directory and set the following variables:

- SECRET_KEY: A secret key for your Django application.
- DEBUG: Set to 'True' for development or 'False' for production.
- Set other environment variables like database settings and more as required.

## Installed Apps

This project includes the following Django apps:
- django.contrib.admin
- django.contrib.auth
- django.contrib.contenttypes
- django.contrib.sessions
- django.contrib.messages
- django.contrib.staticfiles
- Third-party libraries:
  - rest_framework
  - drf_yasg
  - rest_framework_simplejwt
  - rest_framework_simplejwt.token_blacklist
- Custom apps specific to the project:
  - Tour
  - Comments
  - Userprofile
  - accounts
  - 
 Идея проекта:
1.   Предыстория
Люди любят красиво отдыхать, и рынок туристических услуг забит предложениями турфирм и туроператоров буквально до отказа.
Конкуренция действительно огромная, вот только сайты большинства туристических компаний — это безнадежно устаревшие образцы дизайна и юзабилити десяти-пятнадцатилетней давности.
А ведь на дворе 2023-й… Давайте посмотрим, как должен выглядеть современный сайт для туризма.
2. Цель проекта
Разработать сайт для поиска туров по Кыргызстану с возможностью бронирования, создания собственной страницы пользователя для отслеживания истории путешествий по Кыргызстану.
Путешествуйте и делитесь своими впечатлениями!
3. Аудитория
Бишкекчане и гости столицы.






    
