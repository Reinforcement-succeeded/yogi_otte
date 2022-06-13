naver_map_scrapping 폴더 내에서

1. search.py 먼저 실행 ( 전처리 전 파일 생성 : 예시파일을 넣어두었습니다. naver(은평구 맛집).csv )
2. data_preprocessing.py 실행 ( 전처리 후 파일 생성 : 예시파일을 넣어두었습니다. naver(은평구맛집).csv )

### 카카오 지도 스크랩 후 데이터 정제 작업

1. kakao_map_scrapping > kakao_map_scrap.py 실행
2. pandas/csv_files 내에 모든 csv파일 위치 > csv_add.py 실행 후 총합본 제작 > csv_check.py 실행후 label값 int로 바꿔줌
3. 마지막 인간 정제 작업 : csv 파일 내에 이상하게 생긴 열 (untitled.. 등 값이 비워져있거나 중복되어 생긴 열)을 지워준다!
