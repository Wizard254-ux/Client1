from rest_framework import serializers
from .models import User,clientInfo,propertyInfo,PropertyImage,PropertyReview
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True},
                        }
class clientInfoSerializer(serializers.ModelSerializer):
     
     class Meta:
        model = clientInfo
        fields = '__all__'
class reviewSerializer(serializers.ModelSerializer):
     
     class Meta:
        model = PropertyReview
        fields = '__all__'

class propertyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=propertyInfo
        fields='__all__'


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image']

class PropertySerializer(serializers.ModelSerializer):
    images_read = PropertyImageSerializer(many=True, read_only=True)
    images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = propertyInfo
        fields = ['id', 'title', 'rent', 'buy', 'location', 'type', 
                 'bedrooms', 'bathrooms', 'area', 'description', 
                  'images_read', 'images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('images', [])
        property_instance = propertyInfo.objects.create(**validated_data)

        for image in uploaded_images:
            PropertyImage.objects.create(property=property_instance, image=image)

        property_instance = propertyInfo.objects.prefetch_related('images_read').get(id=property_instance.id)
        
        return property_instance