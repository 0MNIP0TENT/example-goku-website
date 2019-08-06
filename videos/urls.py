from django.urls import path
from . import views

urlpatterns = [
    path('',views.Videos.as_view(), name='videos'),
    path('submit/', views.Submit.as_view(), name='submit'),
    path('<int:pk>/comment/', views.Comment.as_view(), name='comment'),
]
