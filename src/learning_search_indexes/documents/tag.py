from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from learning_elasticsearch.models import Tag


# Name of the Elasticsearch index
INDEX = Index('tag')

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@INDEX.doc_type
class TagDocument(Document):
    """Tag Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    title = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword', fielddata=True),
        }
    )

    class Django(object):
        """Inner nested class Django."""

        model = Tag  # The model associate with this Document