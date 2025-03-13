from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_api.views import ProjectViewSet

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects', ProjectViewSet.get_all_projects),
    path('api/create_project', ProjectViewSet.create_project),
    path('api/delete_project/<int:pk>', ProjectViewSet.delete_project),
    path('api/get_single_project/<int:id>', ProjectViewSet.get_project_by_id),
    path('api/delete_all_projects', ProjectViewSet.delete_all_projects),
]
