from django.urls import path
from . import views
urlpatterns = [
    path('create-property/', views.cretepro),
    path('property-list/', views.propertylist),
    path('project/<int:property_id>/edit/', views.property_edit),
    path('plot-land-add/', views.plotland_add),
    path('plot-land-list/', views.plotlandlist),
    path('plot-land-edit/<int:plotland_id>/', views.plotland_edit),
    path('plot-land-delete/<int:plotland_id>/', views.plotland_delete),
    path('project-add/', views.projectproperty),
    path('property-project/', views.propertyprojectlist),
    path('property-project/<int:id>/edit/', views.property_project_edit),
    path('property-project/<int:id>/delete/', views.property_project_delete),
    path('project-plot-land/', views.projectplotland),
    path('land-project/<int:id>/edit/', views.land_project_edit),
    path('land-project/<int:id>/delete/', views.land_project_delete),
    path('land-project/', views.landprojectlist),
    path('property-photo-edit/<int:id>/', views.property_photo_edit),
]