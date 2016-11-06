from rest_framework.generics import ListAPIView

from lots.models import Set, Lot
from .serializers import SetSerializer, LotSerializer


class SetListAPIView(ListAPIView):
    queryset = Set.objects.all()
    serializer_class = SetSerializer


class LotListAPIView(ListAPIView):
    serializer_class = LotSerializer

    def get_queryset(self):
        set_id = self.kwargs['set_id']
        return Lot.objects.filter(set=set_id)