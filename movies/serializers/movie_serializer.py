from django.db.models import Avg
from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('id',)

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('rating'))['rating__avg']

        if rate:
            return round(rate, 1)

        return None
