from django.urls import path
from . import views
from .views import postcreate,postupdate
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('messages/',views.messages,name='messages'),
    path('table/',views.table,name='table'),
    path('create/',postcreate.as_view(),name='create'),
    path('table/<int:pk>/update',postupdate.as_view(),name='update'),
     path('table/<int:pk>/delete',views.delete,name='delete'),
]