from django.shortcuts import render,redirect
from django.contrib import messages,auth
from .algo import compute,tests
def home(request):
    return render(request,"base.html")

def calculate(request):
    if request.method=="POST":
        vertex = request.POST["vertex"]
        graph = request.POST["graph"]
        sv = request.POST["sv"]
        dv = request.POST["dv"]
        if int(sv)>=int(vertex) or int(dv)>=int(vertex):
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,'Unknown source and vertex entered. Try again')
            return redirect('/')
        output = tests(graph,vertex)
        if output == 0:
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,'Input is not specified as above format. Follow sample input for reference.')
            return redirect('/')
        output = compute(output)
        if sv=="" and dv=="":
            return render(request,"result.html",{'output':output})
        else:
            return render(request,"result.html",{'output':output,'req':output[int(sv)][int(dv)],'pre':True})
    return redirect('/')