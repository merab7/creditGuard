from rest_framework import viewsets, mixins
from .models import Card
from .serializers import CardSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend



class CardViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = CardSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)

    #filter by title for this i install django-filters
    filterset_fields = ['title']  
 

 # filter queryset by current user and order by date_created descending order
    def get_queryset(self):
       
        user = self.request.user        
        return Card.objects.filter(user=user.id).order_by('-date_created')






     

