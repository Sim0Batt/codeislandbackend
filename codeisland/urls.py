from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_api.views import ProjectViewSet, HomePageTxtsViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_api.views import send_contact_email

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects', ProjectViewSet.get_all_projects),
    path('api/create_project', ProjectViewSet.create_project),
    path('api/delete_project/<int:pk>', ProjectViewSet.delete_project),
    path('api/get_single_project/<int:id>', ProjectViewSet.get_project_by_id),
    path('api/delete_all_projects', ProjectViewSet.delete_all_projects),
    path('api/get_textes', HomePageTxtsViewSet.get_txts),
    path('api/create_texts', HomePageTxtsViewSet.create_texts),
     path('api/override_project_content/<int:pk>', ProjectViewSet.override_project_content),

    path('api/update_about_text/<str:lang>', HomePageTxtsViewSet.update_about_text),
    path('api/update_tech_text/<str:lang>', HomePageTxtsViewSet.update_tech_text),
    path('api/update_partners_text/<str:lang>', HomePageTxtsViewSet.update_partners_text),

    path('api/send_contact_email', send_contact_email),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
