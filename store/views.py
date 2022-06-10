from django.shortcuts import render
import csv
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from .models import Category, Store
from review import models as R
from user import models as U
from datetime import datetime
from django.utils import timezone

# Create your views here.
def main_view(request):
    return render(request, 'main/main.html')