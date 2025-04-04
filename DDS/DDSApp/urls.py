from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StatusViewSet, TypeViewSet, CategoryViewSet, SubcategoryViewSet, DDSRecordViewSet

router = DefaultRouter()
router.register(r'statuses', StatusViewSet)
router.register(r'types', TypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'records', DDSRecordViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]

