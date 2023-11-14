from elasticsearch_dsl import Index

from .models import Document

documents = Index('documents')


@documents.document
class DocumentDocument(Document):
    class Django:
        model = Document
        fields = [
            'id',
            'text',
        ]
