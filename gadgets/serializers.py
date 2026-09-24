from rest_framework import serializers

from gadgets.models import MovieGadget


class MovieGadgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGadget
        fields = '__all__'