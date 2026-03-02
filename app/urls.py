from django.urls import path,include
from rest_framework.routers import DefaultRouter

from app.views.department import DepartmentViewSet
from app.views.job_position import JobPositionViewSet
from app.views.oranization import OrganizationViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'organization', OrganizationViewSet, basename='organization')
router.register(r'jon-position', JobPositionViewSet, basename='job-position')


urlpatterns = [
    path('', include(router.urls)),
]