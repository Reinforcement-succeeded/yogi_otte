import pandas as pd


# 저장할 파일 이름 적기
final_file_name = "정수로 바꿔준 총합본"
# 조회할 파일 경로 적기
file_path = "파일의 절대경로"

df = pd.read_csv(file_path)
# 변경 전 키값 타입 조회
print(df.info())

# 0,1중 NAN인 값 0으로 바꿔줌
df["label"] = df["label"].fillna(0)
# "label" 타입을 int로 바꿔주고 원래의 "label"에대입해줌
df["label"] = df["label"].astype(int)
# 데이터 타입 확인해보기
print(df.info())

# 파일 저장
file_name = final_file_name + ".csv"
df.to_csv(file_name)
