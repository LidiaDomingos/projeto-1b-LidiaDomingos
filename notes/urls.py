from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('listaTags', views.indexTag, name='listaTags'),
    path('tag/<int:idTag>/', views.notasTag, name='notasTag'),
]