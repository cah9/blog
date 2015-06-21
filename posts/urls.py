from django.conf.urls import url
from . import views
from .views import PostDetailView

urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^edit/done/$', views.add, name='done'),
] 