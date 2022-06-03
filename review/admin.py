from django.contrib import admin
from .models import Review

# Register your models here.
@admin.register(Review)
class CustomReview(admin.ModelAdmin):
    list_display = ('store', 'user', 'star', 'comment',)