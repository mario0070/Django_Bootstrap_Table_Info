
from django.shortcuts import render,redirect
from .models import std
from django.views.generic import CreateView, ListView,UpdateView
# from django.views.generic import CreateView,ListView,UpdateView,DeleteView



def home(request):
    context={
        'cont':std.objects.all()
    }
    return render(request,"students/home.html",context)

def contact(request):
    context={
        'cont':std.objects.all()
    }
    return render(request,"students/contact.html",context)

def about(request):
    context={
        'cont':std.objects.all()
    }
    return render(request,"students/about.html",context)

def table(request):
    context={
        'cont':std.objects.all()
    }
    return render(request,"students/table.html",context)

def messages(request):
    context={
        'cont':std.objects.all()
    }
    return render(request,"students/messages.html",context)


class postcreate(CreateView):
    model=std
    fields=['first_name','last_name','email','country']


class postupdate(UpdateView):
    model=std
    fields=['first_name','last_name','email','country']

def delete(request,pk):
    stds=std.objects.get(id=pk)
    a=std.objects.all()
    if request.method=="POST":
        stds.delete()
        return redirect("table")
    return render(request,"students/delete.html",{"stds":stds,"a":a})