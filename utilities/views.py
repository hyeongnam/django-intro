from django.shortcuts import render

def index(request):
    # templates폴더 안에서 html파일 찾는다.
    return render(request, 'utilities/index.html')