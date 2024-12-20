from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")
def mylink(request):
    return render(request, "main/mylink.html")
def search(request):
    return render(request, "main/search.html")
def mainpage(request):
    return render(request, "main/mainpage.html")
def mainpage1(request):
    return render(request, "main/mainpage1.html")
def myvisits(request):
    return render(request, "main/myvisits.html")
def myfavorites(request):
    return render(request, "main/myfavorites.html")
def myimpressions(request):
    return render(request, "main/myimpressions.html")
def account(request):
    return render(request, "main/account.html")


 