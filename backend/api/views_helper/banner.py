from django.db.models.query import QuerySet

from rest_framework import views, status
from rest_framework.response import Response

from backend.core.models.banner import Banner

from backend.api.response import ApiResponse
from backend.api.serializers.banner import ListBannerSerializer

from backend.api.strings import SUCCESS

class ListBannerView(views.APIView):

    def get_banners(self) -> QuerySet[Banner]:
        return Banner.objects.filter(deleted_at__isnull=True)

    def get(self, request, *args, **kwargs):
        api_response = ApiResponse()

        banners = self.get_banners()
        serializer = ListBannerSerializer(banners, many=True)

        api_response = ApiResponse(
            action=True,
            message=SUCCESS,
            result=serializer.data,
            status=status.HTTP_200_OK
        )

        return Response(data=api_response.to_dict(), status=api_response.status)