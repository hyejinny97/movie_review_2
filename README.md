# 프로젝트 주간 페어 프로그래밍 - 영화 리뷰 커뮤니티 ModelForm

## 과정

- [목표](#목표)
- [준비 사항](#준비-사항)
- [요구사항](#요구-사항)
- [프로젝트 결과 완성본](#프로젝트-결과-완성본)
- [프로젝트 후기](#프로젝트-후기)

## 목표

- 페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다.
- 아래 조건을 만족해야합니다.
  - ModelForm 활용 CRUD 구현
  - Staticfiles 활용 서비스 로고 표시

## 준비 사항

### ▶ 프로젝트 시작 전

> 1번 개발자

1. 깃허브 저장소 생성
2. 2번 사람을 collaborator로 초대
3. 가상환경 생성 후, 장고 프로젝트를 생성
   - `.gitignore` : 가상환경을 ignore
   - pip freeze > requirements.txt : 패키지 목록을 생성
4. 생성한 저장소에 장고 프로젝트를 push

> 2번 개발자

1. 1번 개발자가 생성한 저장소를 clone
2. 가상환경 생성한 후, requirements.txt 설치
   - pip install -r requirements.txt 
3. 앱 생성한 후, 저장소에 push
4. 1번 개발자가 저장소로부터 pull 땡겨오기

### ▶ 프로젝트 진행 중

드라이버 <-> 네비게이터 전환할 때, 드라이버는 push하고 네비게이터는 pull해서 항상 두 사람이 같은 코드를 유지해야 한다.

### ▶ 프로젝트 완성 후

> 2번 개발자는 1번 개발자의 Github 저장소를 Mirror

1. 2번 개발자는 깃허브에 새로운 저장소 생성

2. 1번 개발자의 저장소를 clone
   
   ```bash
   $ git clone --mirror {1번 개발자의 저장소 주소}
   $ cd {1번 개발자의 저장소 이름}
   ```

3. 복사한 저장소를 자신의 원격 저장소에 연결
   
   ```bash
   $ git remote set-url --push origin {2번 개발자가 새롭게 생성한 저장소 주소}
   ```

4. push
   
   ```bash
   $ git push --mirror
   ```

## 요구 사항

> 모델 Model - `M`

- 모델은 아래 조건을 만족해야합니다. 

- 적절한 필드와 속성을 부여하세요.

- 모델 이름 : `Review`

- 모델 필드
  
  | 이름         | 역할      | 필드       | 속성                |
  | ---------- | ------- | -------- | ----------------- |
  | title      | 리뷰 제목   | Char     | max_length=80     |
  | content    | 리뷰 내용   | Text     |                   |
  | movie_name | 영화 이름   | Char     | max_length=80     |
  | grade      | 영화 평점   | Integer  | default=1         |
  | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
  | updated_at | 리뷰 수정시간 | DateTime | auto_now=True     |

> 기능 View - `V`

- 아래 작성된 기능을 구현합니다.
- 생성 및 수정은 ModelForm을 사용하여 구현합니다.
  - 데이터 목록 조회
    - `GET` `http://127.0.0.1:8000/reviews/`
  - 데이터 정보 조회
    - `GET` `http://127.0.0.1:8000/reviews/<int:pk>/`
  - 데이터 생성 
    - `POST` `http://127.0.0.1:8000/reviews/create/`
    - 사용자에게 리뷰 제목, 리뷰 내용, 영화 이름, 영화 평점 데이터를 입력 받습니다.
  - 데이터 수정
    - `POST` `http://127.0.0.1:8000/reviews/<int:pk>/update/`
  - 데이터 삭제
    - `POST` `http://127.0.0.1:8000/reviews/<int:pk>/delete/`

> 화면 Template - `T`

- 아래 작성된 페이지와 컴포넌트를 구현해야 합니다.

- 네비게이션바, Bootstrap `<nav>`
  - 서비스 로고
    - Django Staticfiles 활용
    - 클릭 시 메인 페이지로 이동
  - 리뷰 목록 버튼
    - 클릭 시 목록 페이지로 이동
  - 리뷰 작성 버튼
    - 클릭 시 작성 페이지로 이동

- 메인 페이지
  - `GET` `http://127.0.0.1:8000/reviews/`
  - 자유 디자인

- 목록 페이지
  - `GET` `http://127.0.0.1:8000/reviews/index/`
  - 리뷰 목록 출력
    - 리뷰 제목
    - 영화 이름
  - 제목을 클릭하면 해당 리뷰의 정보 페이지로 이동

- 리뷰 정보 페이지
  - `GET` `http://127.0.0.1:8000/reviews/<int:pk>/`
  - 해당 리뷰 정보 출력
  - 수정 / 삭제 버튼

- 리뷰 작성 페이지
  - `GET` `http://127.0.0.1:8000/reviews/create/`
  - 리뷰 작성 폼

- 리뷰 수정 페이지
  - `GET` `http://127.0.0.1:8000/reviews/<int:pk>/update/` 
  - 리뷰 수정 폼

## 프로젝트 결과 완성본
> 영화 리뷰 페이지 (페어 프로그래밍 결과)

![](gif/django_project_03_animation.gif)

> 추가) TMDB API를 이용해 영화 정보 페이지 추가

![](gif/django_project_03_api_animation.gif)

## 프로젝트 후기

오늘은 두 분과 같이 페어 프로그래밍을 했다. 세 명이서 페어 프로그래밍을 한 적은 처음이어서 역할 분담을 잘해서 차질없이 진행할 수 있을지 조금 걱정은 되었지만, 오히려 사람이 많으니 더 많은 것을 배웠던 시간이었다. 오늘 프로젝트에서는 [Canva](https://www.canva.com/) 사이트를 이용해 제목 로고를 직접 만들어서 사용했다. 예쁘진 않았지만 직접 만든 로고라 의미가 있었다. 폰트도 조원분들과 협의 하에 배달의 민족에서 제공하는 무료 폰트 중 하나인 주아체를 사용해서 좀 더 디자인에 신경을 썼다. 오늘 한가지 배운 것이 있다면 model 작성 시 grade를 IntegerField로 했는데, 그러면 아주 큰 수까지 입력이 가능해서 범위를 0에서 5까지 설정해야 했다. IntegerField()의 인자로 `validators=[MinValueValidator(0), MaxValueValidator(5)]`를 넣어주면 입력 범위가 넘어설 경우 저장되지 않고 메시지가 떴다. 

오늘 이미지 파일 첨부도 가능하게끔 시도해보면서 많이 배울 수 있었고 디자인도 나름 보기 좋게 구현된 것 같다. 이번 프로젝트에서 내가 너무 의견을 많이 제시해서 조원분들이 혼란스럽고 힘들었을텐데 그래도 귀 기울여주시고 반영을 많이 해주셔서 감사했다. 