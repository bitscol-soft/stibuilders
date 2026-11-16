from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/map-data/', views.project_map_data, name='project_map_data'),
    path('projects/compare/', views.compare_projects, name='compare'),
    path('compare/', views.compare_projects, name='compare_short'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('projects/<slug:slug>/unit/<int:pk>/', views.apartment_detail, name='apartment_detail'),
    path('projects/<slug:slug>/unit/<int:pk>/card/', views.apartment_modal, name='apartment_card'),
    path('projects/<slug:slug>/units.json', views.project_units_json, name='units_json'),

    path('suburbs/', views.suburb_list, name='suburb_list'),
    path('suburbs/<slug:slug>/', views.suburb_detail, name='suburb_detail'),

    path('booking/', views.book_visit, name='booking'),
    path('saved/', views.saved_projects, name='saved'),
    path('saved/toggle/', views.save_project, name='save_project'),

    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('land-sharing/', views.land_sharing, name='land_sharing'),
    path('investors/', views.investors, name='investors'),
    path('news/', views.news_list, name='news'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('search/', views.search, name='search'),
    path('robots.txt', views.robots_txt, name='robots'),
    path('prefs/', views.set_prefs, name='set_prefs'),
]
