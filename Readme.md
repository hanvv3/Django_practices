# Django Practices

## 장고 프로젝트 만들기

### 1. pycharm에서 프로젝트(django_practices) 생성/설정/테스트

### 2. Django library 설치 (터미널)
~~~shell
(venv) # pip install django
~~~

### 3. Mysqlclient library 설치
~~~shell
(venv) # pip install mysqlclient
~~~

### 4. 장고 프로젝트 생성
~~~shell
(venv) # django-admin startproject django_practices
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
(venv) # python manage.py migrate
~~~
* mysql 버전이 5.1인 경우 오류, manage.py에 다음 코드 추가하고 실행 위의 코드 실행
~~~python
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datatime'
~~~

### 8. 프로젝트(사이트) 관리 계정 만들기
~~~shell
(venv) # python manage.py createsuperuser
~~~

### 9. 지금까지 작업 내용 확인
1) 서버 시작
   ~~~shell
   (venv) # python manage.py runserver 0.0.0.0:9999
   ~~~
2) 브라우저 접근
   - url http://localhost:9999로 접근

----------------------------------------------------

### 1. pycharm에서 프로젝트(django_practices)에 Application 추가


