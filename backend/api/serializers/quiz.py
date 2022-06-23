from rest_framework import serializers

from backend.core.models.quiz import QuestionImage, Quiz, Question, Answer


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


class QuestionDetailSerializer(QuestionSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = obj.questionimage_set.all()
        return QuestionImageSerializer(images, many=True).data


class QuestionImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionImage
        fields = '__all__'