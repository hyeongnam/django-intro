import random
from django.shortcuts import render

# Create your views here.
def index(request):
    # templates폴더 안에서 html파일 찾는다.
    return render(request, 'index.html')
def dinner(request):
    menu = ['순대국밥', '쌀국수', '햄버거', '곱창']
    choice = random.choice(menu)
    # templates폴더 안에서 html파일 찾는다.
    return render(request, 'dinner.html', {'dinner':choice})
def greeting(request, name):
    return render(request, 'greeting.html',{'name': name})