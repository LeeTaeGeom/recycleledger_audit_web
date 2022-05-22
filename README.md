## recycleledger_audit_web

# recycleledger 웹 사이트
- Eco list 제작

## 1. 웹 개발
- [이태검](https://github.com/LeeTaeGeom)
- [이형석](https://github.com/lhs961021) 

### 1.1 주요 기능
1. filtering 기능 (중상,좌상,단석이 서로서로 앞뒤부분이 보이지 않도록 한다.)
2. 엑셀파일 업로드 기능 <br/> 
-> 파일 업로드 시 서버 단에서 바로 영업 여부 판별후 레포트 반영
4. 레포트 기능<br/>
<summary>
- Total Qty <br/> 
- Total Weight <br/>
- Collecting company <br/>
- verified Ratio <br/>
- Region <br/>
- 영업점 클릭시 지도 뜨고 <br/>
- 위치 뜨게하기 <br/>
- verified 안됐을 경우 직접 수정 가능하게 하기 <br/>

## 2. 프로그래밍 언어

본 프로젝트는
[**Python**](https://www.python.org)을 메인 프로그래밍 언어로 사용하고, 
웹 프레임워크로 [**Django**](https://www.djangoproject.com)를 이용한다.

### 2.1. Requirements.txt

본 애플리케이션의 소스코드 내에서 활용한 모든 외부 라이브러리는 requirements.txt에 해당 라이브러리 리스트를 저장하여 팀원들에게 공유하여야 한다.
```
$ pip freeze > requirements.txt
```
requirements.txt에 저장된 외부 라이브러리를 다운로드 받는 명령어는 다음과 같다.
```
$ pip install -r requirements.txt
```

### 2.3. Python 가상환경
- [pipenv](https://github.com/pypa/pipenv) :  Python.org에서 공식적으로 권장하는 패키지 설치 툴 및 가상환경 구현용 프로그램

## 3. 서버 실행
```
$ python manage.py runserver 
```
## 4. 환경변수 파일

.gitignore

- Git 관련 환경변수 파일

requirements.txt

- 파이썬 라이브러리 종속성 파일

