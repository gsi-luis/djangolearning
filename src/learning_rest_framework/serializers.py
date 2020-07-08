from django.contrib.auth.models import User, Group
from rest_framework import serializers, validators
from .models import Snippet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='learning_rest_framework:user-detail')
    groups = serializers.HyperlinkedIdentityField(view_name='learning_rest_framework:group-detail')
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'snippets']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='learning_rest_framework:group-detail')

    class Meta:
        model = Group
        fields = ['url', 'name']


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def validate_title(self, value):
        if value == '':
            raise serializers.ValidationError("Title value is not null.")

        return value

    def validate_language(self, value):
        try:
            snippet = Snippet.objects.get(language=value)
        except Snippet.DoesNotExist:
            return value

        raise serializers.ValidationError("The value for 'language' must make a unique set")

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Snippet.objects.all(),
                fields=['code']
            )
        ]
