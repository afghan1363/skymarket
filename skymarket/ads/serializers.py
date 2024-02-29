from rest_framework import serializers
from ads.models import Comment, Ad


# class CommentCreateSerializer(serializers.ModelSerializer):
#     created_at = serializers.DateTimeField(read_only=True)
#
#     class Meta:
#         model = Comment
#         fields = ('author', 'ad', 'text', 'created_at')
#
#
# class CommentUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ('text',)


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_image = serializers.CharField(source="author.image", read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True, default=None)

    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True, default=None)
    title = serializers.CharField(max_length=250),
    price = serializers.IntegerField(),
    phone = serializers.CharField(source='author.phone'),
    description = serializers.CharField(),
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')

    class Meta:
        model = Ad
        fields = '__all__'
