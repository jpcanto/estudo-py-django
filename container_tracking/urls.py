from django.urls import path, register_converter

from . import views, converters

register_converter(converters.ContainerIdConverter, 'ID_CONVERTER')

urlpatterns = [
    path('', views.index, name='index'),
    path('<ID_CONVERTER:container_id>', views.results, name='results')
]