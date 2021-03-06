import json
from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from learning_search_indexes.documents.tag import TagDocument


class TagDocumentSerializer(DocumentSerializer):
    """Serializer for the Book document."""

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = TagDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'title',
        )
