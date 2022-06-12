from rest_framework import views, status, viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from backend.core.models.quiz import Quiz, Question, Answer
from backend.api.serializers.quiz import QuizSerializer, QuestionSerializer
from backend.api.response import ApiResponse
from backend.api import strings


class QuizViewSet(viewsets.GenericViewSet):

    def list(self, request, *args, **kwargs):
        quizes = Quiz.objects.filter(deleted_at__isnull=True)
        serializer = QuizSerializer(quizes, many=True)

        response = ApiResponse(
            action=True, 
            result=serializer.data,
            message=strings.SUCCESS,
            status=status.HTTP_200_OK
        )

        return Response(response.to_dict(), status=response.status)

    def list_questions(self, request, *args, **kwargs):
        quiz_id = kwargs.get('quiz_id')
        quiz = get_object_or_404(Quiz.objects.filter(deleted_at__isnull=True), pk=quiz_id)
        questions = Question.objects.filter(quiz=quiz, deleted_at__isnull=True)

        serializer = QuestionSerializer(questions, many=True)

        response = ApiResponse(
            action=True, 
            result=serializer.data,
            message=strings.SUCCESS,
            status=status.HTTP_200_OK
        )

        return Response(response.to_dict(), status=response.status)