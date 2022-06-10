from django.shortcuts import render
# import csv
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from .models import Category, Store
from review import models as R
import random
# from user import models as U
from datetime import datetime
# from django.utils import timezone

# Create your views here.
def main_view(request):
    input = {}
    #카테고리 집어 넣기
    all_category = Category.objects.all()
    for ac in all_category:
        if input == {}:
            input['category'] = [ac]
        else:
            input['category'].append(ac)
    #오늘의 리뷰 넣기
    all_reviews = R.Review.objects.all().filter(star = 5)
    input['today_review'] = random.choice(all_reviews)
    #오늘의 주문랭킹
    all_reviews = R.Review.objects.filter(create_date__gte=datetime(2022, 1, 10),create_date__lte=datetime(2022, 6, 10))
    order_volume = {}
    for ar in all_reviews:
        if ar.store.category.name in order_volume:
            order_volume[ar.store.category.name] += 1
        else:
            order_volume[ar.store.category.name] = 1
    order_volume2 = list(sorted(order_volume.items(), key=lambda x:x[1], reverse=True))
    input['today_ranking'] = order_volume2[:5]
    return render(request, 'main/main.html', {'data':input})
#