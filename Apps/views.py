from django.http import HttpResponse
from django.shortcuts import render#sorry we have to import render....
from .models import Todos
from .serializers import TodosSerializer  
from rest_framework import viewsets    

def To(request):
      return HttpResponse('<h1>Hey we are on something big ........</h1>')


# class TodosView(viewsets.ModelViewSet):
#       serial=TodosSerializer
#       queryset=Todos.objects.all()

class TodosView(viewsets.ModelViewSet):       # add this
    serializer_class = TodosSerializer          # add this
    queryset = Todos.objects.all()        



# def Hello(request):
#     # return HttpResponse('Hello djnago admin')
#     #   Name=Names.objects.all()
#       return render(request,'main.htm',{'Name':Name})
  

# def name(request):
#     name=request.POST['name']
#     return render(request,'name.htm',{'name':name})


# def inputs(request):
#     show=request.POST['show']
#     return render(request,'/static/post.htm',{{'show':show}})