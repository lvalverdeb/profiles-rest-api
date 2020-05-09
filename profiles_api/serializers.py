from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serialises a name field for testing our APiView"""
    name = serializers.CharField(max_length=10)
