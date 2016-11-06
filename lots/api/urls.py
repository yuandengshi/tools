from django.conf.urls import url

from .views import SetListAPIView, LotListAPIView

urlpatterns = [
    url(r'sets/$', SetListAPIView.as_view(), name='set-list'),
    url(r'sets/(?P<set_id>[0-9]+)/lots/$', LotListAPIView.as_view(), name='lot-list'),
]
