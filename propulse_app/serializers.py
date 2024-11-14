from rest_framework import serializers
from .models import Utility, HostelMedia, Hostel, Message

class UtilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Utility
        fields = ['id', 'name']

class HostelMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelMedia
        fields = ['id', 'video', 'picture']

class HostelSerializer(serializers.ModelSerializer):
    utilities = serializers.PrimaryKeyRelatedField(
        queryset=Utility.objects.all(), many=True
    )
    more_media = HostelMediaSerializer(required=False)
    address = serializers.StringRelatedField()

    # Define all image fields
    picture1 = serializers.ImageField(required=True)
    picture2 = serializers.ImageField(required=True)
    picture3 = serializers.ImageField(required=True)
    picture4 = serializers.ImageField(required=False)
    picture5 = serializers.ImageField(required=False)

    class Meta:
        model = Hostel
        fields = [
            'id', 'name', 'address', 'property_size', 'distance_to_junction', 
            'utilities', 'picture1', 'picture2', 'picture3', 
            'picture4', 'picture5', 'more_media'
        ]


    def create(self, validated_data):
        utilities_data = validated_data.pop('utilities')
        hostel = Hostel.objects.create(**validated_data)
        hostel.utilities.set(utilities_data)  # Set the many-to-many relationship
        return hostel

    def to_representation(self, instance):
        # Use the default representation first
        representation = super().to_representation(instance)
        # Replace the utilities with a detailed view
        representation['utilities'] = UtilitySerializer(instance.utilities, many=True).data
        return representation


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'message']