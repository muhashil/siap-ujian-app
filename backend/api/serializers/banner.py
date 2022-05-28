from rest_framework import serializers

from backend.core.models.banner import Banner
from backend.api.utils.image import get_image_url

class ListBannerSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        request = self.context.get('request')
        return get_image_url(obj.image, request)

    class Meta:
        model = Banner
        fields = '__all__'
