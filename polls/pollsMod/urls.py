from djang.conf.urls import urls
from . import views

# url maps to the views/index function
urlpatterns = [
    url(r'^$', views.index, name='index'),
]