# Django Practices

## 장고 프로젝트 만들기

### 1. pycharm에서 프로젝트(django_practices) 생성/설정/테스트

### 2. Django library 설치 (터미널)
~~~shell
(venv) $ pip install django
~~~

### 3. Mysqlclient library 설치
~~~shell
(venv) $ pip install mysqlclient
~~~

### 4. 장고 프로젝트 생성
~~~shell
(venv) $ django-admin startproject django_practices
~~~

### 5. directory 정리(pycharm 프로젝트랑 장고 프로젝트를 일치시키기)

### 6. 초기 설정(settings.py)
1) time zone 설정
~~~python
TIME_ZONE = 'Asia/Seoul'
~~~
2) database 설정
~~~python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webdb',
        'USER': 'webdb',
        'PASSWORD': 'webdb',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
~~~

### 7. Django 프로젝트 관리 어플리케이션(기본설치)이 사용하는 DB 생성
~~~shell
(venv) $ python manage.py migrate
~~~
* mysql 버전이 5.1인 경우 오류, manage.py에 다음 코드 추가하고 실행 위의 코드 실행
~~~python
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datatime'
~~~

### 8. 프로젝트(사이트) 관리 계정 만들기
~~~shell
(venv) $ python manage.py createsuperuser 

Username (leave blank to use 'seeeaaan'): admin
Email address: kickscar@gmail.com
Password:
Password (again):
Superuser created successfully.
~~~
1) Superuser 지우기:
~~~shell
(venv) $ python manage.py shell
>>>from django.contrib.auth.models import User
>>>User.objects.get(username="seeeaaan", is_superuser=True).delete()
~~~

### 9. 지금까지 작업 내용 확인
1) 서버 시작
   ~~~shell
   (venv) $ python manage.py runserver 0.0.0.0:9999
   ~~~
2) 브라우저 접근
   - url http://localhost:9999로 접근
   - admin 로그인은 http://localhost:9999/admin
   - (admin/myPW)
   - (quit server with: ^c)

----------------------------------------------------

### 2. pycharm에서 프로젝트(django_practices)에 Application 추가

#### 1. Applicatione들의 통합 template 디렉토리 templates 만들기
1) 디렉토리 생성
django_practices
   |--- templates
   
2) template 디렉토리 설정(settings.py)
~~~python
import os
~
'DIRS': [os.path.join(BASE_DIR, 'templates')],
~
~~~

#### 2. helloworld application 만들기
1) application 생성
~~~shell
(venv) $ python manage.py startapp helloworld
~~~

2) application 등록(settings.py)
~~~python
INSTALLED_APPS = [
    'helloworld',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]
~~~

3) application의 template 디렉토리 생성
django_practices
|--- templates
      |--- helloworld
   
4) urls.py 에 URL 등록하고 views.py 에 요청 처리 함수만들고 template(html) 연결하고..... (반복반복)

#### 3. emaillist01 application 만들기
1) application 생성
~~~shell
(venv) $ python manage.py startapp emaillist01
~~~

2) application 등록(settings.py)
~~~python
INSTALLED_APPS = [
    'emaillist01',
    'helloworld',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]
~~~

3) application의 template 디렉토리 생성
django_practices
|--- templates
      |--- helloworld
      |--- emaillist
   
4) urls.py 에 URL 등록하고 views.py 에 요청 처리 함수만들고 template(html) 연결하고..... (반복반복)


#### 4. guestbook01 application 만들기
1) application 생성
~~~shell
(venv) $ python manage.py startapp guestbook01
~~~

2) application 등록(settings.py)
~~~python
INSTALLED_APPS = [
    'guestbook01',
    'emaillist01',
    'helloworld',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]
~~~

3) application의 template 디렉토리 생성
django_practices
|--- templates
      |--- helloworld
      |--- emaillist01
      |--- guestbook01
   
4) urls.py 에 URL 등록하고 views.py 에 요청 처리 함수만들고 template(html) 연결하고..... (반복반복)
