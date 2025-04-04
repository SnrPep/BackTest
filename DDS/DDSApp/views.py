from rest_framework import viewsets
from .models import DDSRecord, Status, Type, Category, Subcategory
from .serializers import DDSRecordSerializer, StatusSerializer, TypeSerializer, CategorySerializer, SubcategorySerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class DDSRecordViewSet(viewsets.ModelViewSet):
    queryset = DDSRecord.objects.all()
    serializer_class = DDSRecordSerializer
