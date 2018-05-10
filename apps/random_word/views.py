from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not "count" in request.session:
        request.session["count"] = 0
    return render(request, "random_word/index.html")

def process(request):
    request.session["count"] += 1
    request.session["word"] = get_random_string(length=14)    
    return redirect("/random_word")

def reset(request):
    if request.method == "GET":
        print("GETTTTTTT")
    request.session.clear()
    print("called***********")
    return redirect("/random_word")

