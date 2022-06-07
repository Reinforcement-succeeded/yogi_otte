from django.shortcuts import render


def result_view(request):
    return render(request, 'result/result.html')
