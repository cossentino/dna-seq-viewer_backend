from rest_framework import serializers


class DNASequenceSerializer(serializers.Serializer):
    seq = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    name = serializers.CharField()
    description = serializers.CharField()
