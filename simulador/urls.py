from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulador, name='simulador'),
    path('simulacion/', views.simulacion, name='simulacion'),
    path('socialesretencion/', views.socialRetencion, name="socialesretencion"),
    path('socialesretencion/<int:id>/update/', views.update_socialRetencion, name="socialesretencion_update"),
    path('deletesocialesretencion/<int:id>/', views.delete_socialRetencion, name="socialesretencion_delete"),
    path('sociales/', views.social, name="sociales"),
    path('sociales/<int:id>/update/', views.update_social, name="sociales_update"),
    path('deletesociales/<int:id>/', views.delete_social, name="sociales_delete"),
    path('extras/', views.extra, name="extras"),
    path('extra/<int:id>/update/', views.update_extra, name="extra_update"),
    path('deleteextra/<int:id>/', views.delete_extra, name="extra_delete"),
    path('tasas/', views.tasas, name="tasas"),
    path('tasas/<int:id>/update/', views.update_tasa, name="tasa_update"),
    path('deletetasa/<int:id>/', views.delete_tasa, name="tasa_delete"),
    path('salario/', views.salary, name="salario"),
    path('salario/<int:id>/update/', views.updateSalary, name="salario_update"),
    path('deletesalario/<int:id>/', views.delete_salario, name="salario_delete"),
    path('downloadSimulation', views.generatePdf, name="download")
]


# path('deudaaporte/', views.deudaAporte, name='deudaaporte'),
# path('deudaaporte/<int:id>/update/', views.update_deudaaporte, name='deudaaporte_update'),
# path('deletedeudaaporte/<int:id>/', views.delete_deudaaporte, name="deudaaporte_delete"),
# path('extracupos/', views.extracupo, name="extracupos"),
# path('extracupos/<int:id>/update/', views.update_extracupo, name="extracupo_update"),
# path('deleteextracupo/<int:id>/', views.delete_extracupo, name="extracupo_delete"),