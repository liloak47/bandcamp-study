from rest_framework import serializers


class AlbumSerializer(serializers.Serializer):
    title = serializers.CharField()


class MusicianSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    instrument = serializers.CharField()
    albums =  AlbumSerializer(many=True)
