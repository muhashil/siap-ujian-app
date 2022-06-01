from rest_framework import views, status, viewsets
from rest_framework.response import Response

from backend.core.models.materi import Materi

from backend.api.serializers.materi import ListMateriSerializer

from backend.api.response import ApiResponse
from backend.api.strings import NOT_FOUND, SUCCESS


class MateriViewSet(viewsets.GenericViewSet):

    def get_object(self):
        slug = self.kwargs.get('slug')
        try:
            object_ = self.get_queryset().get(slug=slug)
        except Materi.DoesNotExist:
            object_ = None

        return object_

    def get_queryset(self):
        request = self.request
        queryset = Materi.objects.filter(deleted_at__isnull=True)

        type_ = request.query_params.get('type')
        if type_:
            queryset = queryset.filter(type=type_)

        category = request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def list(self, request, *args, **kwargs):
        list_materi = self.get_queryset()
        serializer = ListMateriSerializer(list_materi, many=True, context={'request': request})

        api_response = ApiResponse(
            action=True,
            message=SUCCESS,
            result=serializer.data,
            status=status.HTTP_200_OK
        )

        return Response(data=api_response.to_dict(), status=api_response.status)

    def retrieve(self, request, *args, **kwargs):
        materi = self.get_object()
        if materi is not None:
            serializer = ListMateriSerializer(materi, context={'request':request})

            api_response = ApiResponse(
                action=True,
                message=SUCCESS,
                result=serializer.data,
                status=status.HTTP_200_OK
            )
            return Response(data=api_response.to_dict(), status=api_response.status)

        api_response = ApiResponse(
            message=NOT_FOUND,
            result=materi,
            status=status.HTTP_200_OK
        )
        return Response(data=api_response.to_dict(), status=api_response.status)