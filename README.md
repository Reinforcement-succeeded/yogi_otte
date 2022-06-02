# 요기 어때?

![Screen Shot 2022-06-02 at 20 29 31](https://user-images.githubusercontent.com/99478108/171622919-d4540ee0-a5aa-4d7a-8044-462a46bf7929.png)<br>

###### 사진출처 : 요기요, 여기어때

---

## 프로젝트 진행 단계

-   [계획 및 진행]() 단계
-   [마무리]() 단계

---

# 계획 및 진행 단계

<details>
<summary>프로젝트 진행 순서</summary>
<div markdown="1">
발제 → 프로젝트 주제선정, 발제자료에 나와있는 기능구현 회의(모든 팀원이 필수기능 이해하기, 추가기능 어디까지 구현할 것인가?) → 프로젝트에 필요한 Notion page, GitHub repository 개설 → Figma 이용해 레이아웃 제작, GitHub Readme, Wiki 업로드 → 역할분담 및 마감기한 설정 → 마감기한까지 열심히 만들기! → 모든 branch merge (파일 합치기)→ 완성! → 코드리뷰
</div>
</details>
<br>

### **기획**

<details>
<summary>주제 브레인스토밍</summary>
<div markdown="1">

: 상품추천, (코딩자료 등)공부자료추천, 뉴스자료 모아보기, 신발추천, 책 추천, 주류 추천, 맛집 추천 등 — 어려움 : 데이터 구하기, 해결책 : 아이디어는 최대한 많이 내보고 데이터 있는 방향으로 진행
<br><br>
**주제 선정 : 사용자 기반 맛집 추천 시스템**

</div>
</details><br>

### **주제 선정**

**요기어때?** :
당신을 위한 맛집을 추천해드립니다!<br></br>

**서비스 소개**<br>
사용자 기반 맛집 추천 사이트<br></br>
**개발 툴**<br>
Vscode, Pycharm, Django, MongoDB, HTML, CSS, JavaScript, Python<br></br>
**협업 툴**<br>
Notion, Github, Figma, Slack, GatherTown

<details>
<summary>필수기능</summary>
<div markdown="1">
1. Django를 사용해주세요.<br>
2. 하나의 레포지토리에서 **기능별 혹은 개인별 브랜치를 사용해서 협업**해주세요.<br>
3. **회원 기능**을 포함해주세요.<br>
4. **CRUD 기능**을 포함해주세요.<br>
5. 장고의 모델에서 **one-to-many와 many-to-many** 기능을 사용해주세요 (ERD 제출 필수).<br>
6. 콘텐츠는 팀에서 자유롭게 선정해주세요.<br>
7. 목요일 오전 특강으로 배우게 될 추천시스템(협업필터링)을 활용해주세요.<br>
8. 크롤링한 데이터를 바탕으로 유사한 콘텐츠를 추천해주어야 합니다<br>
9. 영화 추천 사이트를 만들어도 좋고, 유튜브 영상을 추천하는 사이트를 만드셔도 좋습니다.<br>
</div>
</details>

<details>
<summary>추가기능</summary>
<div markdown="1">
1. 아래의 예시 와이어프레임을 참고해주세요!<br>
2. 배포 (프로젝트 말미에 특강 예정. 난이도 상)<br>
 1. AWS EC2를 이용해 장고 프로젝트를 배포해 주세요<br>
 2. 장고의 sqlite3가 아닌 AWS RDS의 DB를 이용해주세요<br>
 3. 스태틱 파일들을 ec2가 아닌 AWS S3로 업로드 해주세요<br>
    - **주의할 점**<br>
        1. 프론트 / 백은 안 나누셔도 됩니다 (이번 프로젝트 이후에 진행 예정)<br>
        2. 아직 CRUD에 집중하고 싶은 팀은 추천기능(필수 포함 6번)을 단순 필터링(별점순, 조회순)으로 만드셔도 좋습니다.<br>
        3. **VSCode의 Live Share 익스텐션 사용하여 실시간 협업**<br>

</details><br>

**페이지 이용자**<br>
배가 고픈 사람, 맛집을 빠르고 쉽게 찾고싶은 사람

---

-   **팀 내 약속**
    -   개인이 맡은 기능 **Github 개인 브랜치에 업로드** 후 **매일 머지**
    -   **Github Readme에 각자가 오늘 한 일 업로드**
    -   **Notion 개발일정에 자기가 맡은 기능 참조파일 업로드** (추후 코드리뷰 및 팀원 자료 공유용)
    -   Github Readme, Wiki는 계속 업데이트
    -   자리비울일 있거나 얘기 나눌때 Gather, Slack으로 소통
    -   미리 정해둔 **폴더**, **파일 경로설정** 지키기
    -   가상환경, 인터프리터 통일
        -   python 3.9.12, django 4.0.4
    -   커밋메세지 통일
        -   MOD : modify한 내용
        -   ENH : enhancement한 내용
        -   ADD : add한 내용
        -   DEL : delete한 내용
        -   MOV : move한 내용
        -   MOD & MOV : modify한 내용 & move한 내용
    -   .gitignore로 필요없는 파일은 업로드 시키지 않기
    -   결과값 신뢰도를 높이기 위한 커스텀 데이터 생성
    ***
-   **경로설정**

    초기 (프로젝트 진행하면서 변경될 수 있음)

    [스타일시트 파일 경로 : projects\mysite\static\style.css]

    ![Untitled 2](https://user-images.githubusercontent.com/99478108/171621367-7c12fded-d5fa-4777-952c-c16709fc3b9f.png)

    [출처 : 점프 투 장고](https://wikidocs.net/70804)

    ***

-   **팀명과 팀원: 강화성공(6조) (윤가현[팀장], 김민재, 전진영, 이승태)**
-   **개발 기간 : 22.06.02.목 ~ 22.05. 24.화 오후 5:00 마감**
-   **역할 분담**
    -   **데이터 수집 (스크래핑, 모델 학습용) : 가현**
    -   **AI 모델 제작 : 진영**
    -   **백엔드 담당 : 승태**
    -   **프론트앤드 담당 : 민재**
        <br><br>
-   **발표자 및 영상촬영** - **발표자 : 윤가현** - **영상촬영 : 김민재**
    <br><br>
-   **🛠 개발 일정**<br><br>
    ![Screen Shot 2022-06-02 at 20 37 45](https://user-images.githubusercontent.com/99478108/171621113-bab3a29a-91a5-49fb-adfd-f98b69c411a3.png)

-   **레이아웃**
    ![Untitled 3](https://user-images.githubusercontent.com/99478108/171620969-1b4ec1c4-2734-4a58-ad81-d2231a745fb7.png)
-   **API 설계**
    ![Screen Shot 2022-06-02 at 20 36 08](https://user-images.githubusercontent.com/99478108/171620865-8a5d1866-dafc-4109-a587-18c82b6c1f46.png)

---

## **DB설계**

[ERD Cloud 사용](https://www.erdcloud.com/d/gwWqsmNR7R5FcAK7L)

-   **관계선, 기호 종류**
    ![Screen Shot 2022-06-02 at 20 31 48](https://user-images.githubusercontent.com/99478108/171620165-d36cfa96-41c7-4ab0-b112-28b5fde9fb54.png)

---
