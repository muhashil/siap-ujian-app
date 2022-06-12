from rest_framework import serializers

from backend.core.models.quiz import Quiz, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quiz
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    def get_answers(self, obj):
        answers = obj.answer_set.all()
        return AnswerSerializer(answers, many=True).data

    class Meta:
        model = Question
        fields = '__all__'
