from rest_framework import serializers

from ads.ad.serializers import AdSerializer
from ads.models import Ad, Selection

from users.models import User


class SelectionSerializer(serializers.ModelSerializer):
    ads = serializers.SlugRelatedField(read_only=True,
                                       many=True,
                                       slug_field='name')
    user = serializers.SlugRelatedField(read_only=True,
                                        slug_field='username')


    class Meta:
        model = Selection
        fields = '__all__'


class SelectionDetailSerializer(serializers.ModelSerializer):
    ads = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    ads = serializers.SlugRelatedField(required=False,
                                       queryset=Ad.objects.all(),
                                       slug_field='id',
                                       many=True)
    user = serializers.SlugRelatedField(required=False,
                                        queryset=User.objects.all(),
                                        slug_field='id')

    class Meta:
        model = Selection
        fields = '__all__'