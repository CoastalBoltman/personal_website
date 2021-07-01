from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me':"Hello, I M from views.py"}
    return render(request,'first_page/index.html',context=my_dict)
    # return HttpResponse("HELLO MAHA")
# Create your views here.
