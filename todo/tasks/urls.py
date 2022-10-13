from django.urls import path
from . import views

urlpatterns = [
    # path('', index.as_view(), name="list"),
	# path('update_task/<str:pk>/', updateTask.as_view(), name="update_task"),
	# path('delete/<str:pk>/',deleteTask.as_view(), name="delete"),
    
    
    
	path('', views.index, name="list"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
]