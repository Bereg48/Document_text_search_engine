
from rest_framework import viewsets

from .elasticsearch import DocumentDocument
from .models import Document
from .serializers import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().order_by('-created_date')
    serializer_class = DocumentSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        if query is not None:
            s = DocumentDocument.search().query("match", text=query)
            response = s.execute()
            ids = [hit.id for hit in response]
            return self.queryset.filter(id__in=ids)
        return self.queryset

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        s = DocumentDocument.get(id=instance.id)
        s.delete()
