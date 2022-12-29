from rest_framework import serializers 
from drf_extra_fields.fields import Base64ImageField
from FaceRecognition.models import AttendeesImage

class ImageSerializer(serializers.Serializer): 
    image = Base64ImageField()
    
    class Meta:
        model = AttendeesImage
        fields = ['image']
    
    def create(self, validated_data):
        image=validated_data.pop('image')
        data=validated_data.pop('data')
        return AttendeesImage.objects.create(data=data,image=image)