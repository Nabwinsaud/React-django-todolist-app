from django.urls import path
from .import views

urlpatterns=[
    path('',views.To ,name='To'),
    path('',views.TodosView,name='TodosView')
    
    # path('',views.Hello,name='Hello'),
    # path('name',views.name,name='name')
    # # path('show',views.inputs,name='inputs')
]