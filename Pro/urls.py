from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from Apps import views


router=routers.DefaultRouter()
router.register(r'tasks',views.TodosView,'task')
urlpatterns=[

    path('admin/',admin.site.urls),
    path('',include('Apps.urls')), #Apps is my app
    path('api/', include(router.urls)),
  
   
]


