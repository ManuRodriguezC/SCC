from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulador, name='simulador'),
    path('deudaaporte/', views.deudaAporte, name='deudaaporte'),
    path('deudaaporte/<int:id>/update/', views.update_deudaaporte, name='deudaaporte_update'),
    path('deletedeudaaporte/<int:id>/', views.delete_deudaaporte, name="deudaaporte_delete"),
    path('extracupos/', views.extracupo, name="extracupos"),
    path('extracupos/<int:id>/update/', views.update_extracupo, name="extracupo_update"),
    path('deleteextracupo/<int:id>/', views.delete_extracupo, name="extracupo_delete")
]
