
from django.urls import path
from .import views
urlpatterns = [
    
    path('stuinfo/<int:pk>', views.student_detail,name='stuinfo'),
    path('stuinfo/', views.student_list),
    
]