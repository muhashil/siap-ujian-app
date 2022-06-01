from rest_framework import serializers

from backend.api.utils.image import get_image_url
from backend.core.models.materi import Materi


class ListMateriSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    def get_file_url(self, obj: Materi):
        if obj.file:
            request = self.context.get('request')
            return get_image_url(obj.file, request)
        return 

    class Meta:
        model = Materi
        fields = '__all__'
