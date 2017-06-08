from django.conf.urls import url
from drc_web import views

# patterns here are prefixed with 'web/'
urlpatterns = [
    url(r'^ping$', views.ping),
    url(r'^heat_map$',views.heat_map),
    url(r'^radar_plot$',views.radar_plot),
    url(r'^matplotlib', views.matplotlib),
]
