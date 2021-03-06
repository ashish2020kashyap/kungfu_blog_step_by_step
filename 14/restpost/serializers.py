from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from mypost.models import Post
from mypost.models import Category


class listSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'id',
			'category',
			'title',
			'text',
		]