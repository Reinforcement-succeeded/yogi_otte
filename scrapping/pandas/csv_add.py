# csv 파일 합치는 코드
import pandas as pd
import os

##############사용자 입력 부분
# 나의 csv 있는 폴더 경로 입력
my_dir = "폴더의절대경로"
# 최종적으로 저장할 파일 이름 입력
final_file_name = "종합본"
##############


file_list = os.listdir(my_dir)
# print(file_list)

csv_list = []
for csv in file_list:
    if not csv == ".DS_Store":
        data_A = pd.read_csv(csv, on_bad_lines="skip")
        df_A = pd.DataFrame(data_A, columns=data_A.keys())
        csv_list.append(df_A)
print(csv_list)

res = pd.concat(csv_list)

file_name = final_file_name + ".csv"
res.to_csv(file_name)

# 머징한df.to_csv("결과물.csv")
