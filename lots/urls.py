from django.conf.urls import url

from .views import SetListView, LotListView

urlpatterns = [
    url(r'sets/$', SetListView.as_view(), name='set-list'),
    url(r'^$', LotListView.as_view(), name='lot-list'),
]
