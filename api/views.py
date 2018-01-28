from bashim.models import BashAbyssQuote, BashQuote
from rest_framework import viewsets
from .serializers import BashQuoteSerializer, BashAbyssQuoteSerializer

class BashQuoteViewSet(viewsets.ModelViewSet):
    queryset = BashQuote.objects.all()[:50]
    serializer_class = BashQuoteSerializer

class BashAbyssQuoteViewSet(viewsets.ModelViewSet):
    queryset = BashAbyssQuote.objects.all()[:50]
    serializer_class = BashAbyssQuoteSerializer