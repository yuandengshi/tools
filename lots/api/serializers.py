from rest_framework.serializers import ModelSerializer

from lots.models import Set, Lot


class SetSerializer(ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'


class LotSerializer(ModelSerializer):
    class Meta:
        model = Lot
        fields = '__all__'