# import csv
# import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from review import models as R
# from user import models as U
# from run_model import sentiment_predict
#categroy / name
# cat = []
# f = open('static/csv/data.csv', 'r', encoding='utf-8')
# rdr = csv.reader(f)
# for line in rdr:
#     cat.append(line[4])
# for c in set(cat):
#     Category.objects.create(name = c)
# f.close()
#store / name 3, location 6, category 4, url 2
#     cat = []
#     f = open('static/csv/data.csv', 'r', encoding='utf-8')
#     rdr = csv.reader(f)
#     for line in rdr:
#         # print(line)
#         cat.append((line[3], line[6].split('\n')[0], line[4], line[2]))
#     print(set(cat))
#     f.close()
#     for c in set(cat):
#         Store.objects.create(name=c[0], location=c[1], category=Category.objects.get(name=c[2]), url = c[3])
#reviews / store 3, user x, star 5, comment 2, calc_star x
# cat = []
# f = open('static/csv/data.csv', 'r', encoding='utf-8')
# rdr = csv.reader(f)
# for line in rdr:
#     calc = sentiment_predict(line[2])
#     cat.append((line[3], line[5], line[1], line[7].replace('.', '-')[:-1] + ' 00:00:00', calc * 100))
# print(set(cat))
# f.close()
# for c in set(cat):
#     try:
#         Review.objects.create(
#             store=Store.objects.get(name=c[0]),
#             user=CustomUser.objects.get(username=request.user.username),
#             star=c[1],
#             comment=c[2],
#             create_date=datetime.strptime(c[3], '%Y-%m-%d %H:%M:%S'),
#             calc_star=c[4]
#         )
#     except:
#         pass