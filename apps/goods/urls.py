from django.urls import path
from django.conf.urls import url

from .views import DetailView, ListView

app_name = 'goods'
urlpatterns = [
    # path('detail/', DetailView.as_view(), name='detail')
    url(r'^detail/(?P<id>\d+)/$', DetailView.as_view(), name='detail'),
    # path('list/<int:p_number>', ListView.as_view(), name='list')
    # url(r'^list/(?P<type>\w+)/(?P<p_number>\d*)$', ListView.as_view(), name='list'),
    url(r'^list/(?P<type>\w+)/$', ListView.as_view(), name='list'),
    url(r'^list/(?P<type>\w+)/(?P<p_number>\d*)$', ListView.as_view(), name='list'),
]