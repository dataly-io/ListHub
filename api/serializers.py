from rest_framework import serializers
from posts import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'content',
            'created',
            'updated'
        )
        model = models.Post
