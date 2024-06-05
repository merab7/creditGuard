from rest_framework import viewsets, mixins
from .models import Card
from .serializers import CardSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated




class CardViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = CardSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    permission_classes = [IsAuthenticated]
    
    # filtering possibility by title
    filterset_fields = ['title']  
    # ordering possibility by date_created
    ordering_fields = ['date_created']
    #default order
    ordering = ['-date_created']

    
    # filter queryset by current user 
    def get_queryset(self):
        user = self.request.user        
        return Card.objects.filter(user=user.id)
    
    #every created card belongs to current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)