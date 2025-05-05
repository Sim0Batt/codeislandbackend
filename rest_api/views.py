from rest_framework import viewsets
from .models import Project, HomePageTxts
from .serializer import ProjectSerializer, TxtsSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from urllib.parse import unquote
import logging
from django.core.mail import send_mail


logger = logging.getLogger(__name__)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer

    @api_view(['GET'])
    def get_all_projects(request):
        projects = Project.objects.all().order_by('id')
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @api_view(['POST'])
    def create_project(request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @api_view(['DELETE'])
    def delete_project(request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response(status=404)
        
        project.delete()
        return Response(status=204)
    
    @api_view(['GET'])
    def get_project_by_id(request, id):
        projects = Project.objects.filter(id=id)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @api_view(['DELETE'])
    def delete_all_projects(request):
        Project.objects.all().delete()
        return Response(status=204)

    @api_view(['POST'])
    @parser_classes([MultiPartParser, FormParser])  # Add parsers for file uploads
    def override_project_content(request, pk):
        try:
            logger.info(f"Request data: {request.data}")
            logger.info(f"Request files: {request.FILES}")

            project = Project.objects.get(pk=pk)
            # Update fields if provided in the request
            project.titleIt = request.data.get('titleIt', project.titleIt)
            project.contentIt = request.data.get('contentIt', project.contentIt)
            project.short_descriptionIt = request.data.get('short_descriptionIt', project.short_descriptionIt)
            project.titleEn = request.data.get('titleEn', project.titleEn)
            project.contentEn = request.data.get('contentEn', project.contentEn)
            project.short_descriptionEn = request.data.get('short_descriptionEn', project.short_descriptionEn)
            project.title_es = request.data.get('title_es', project.title_es)
            project.description_es = request.data.get('description_es', project.description_es)
            project.short_description_es = request.data.get('short_description_es', project.short_description_es)
            project.tech_list = request.data.get('tech_list', project.tech_list).split(',')

            if request.data.get('visible', project.visible) == 'true':
                project.visible = True
            else:
                project.visible = False
            

            if 'image' in request.FILES:
                project.image = request.FILES['image']

            # Save the updated project
            project.save()
            return Response({"message": "Project content updated successfully", "project": ProjectSerializer(project).data}, status=200)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            return Response({"error": str(e)}, status=400)
        


        

class HomePageTxtsViewSet(viewsets.ModelViewSet):
    serializer_class = TxtsSerializer
    
    @api_view(['GET'])
    def get_txts(request):
        try:
            texts = HomePageTxts.objects.first()
            serializer = TxtsSerializer(texts)
            return Response(serializer.data)
        except HomePageTxts.DoesNotExist:
            return Response(status=404)

    @api_view(['POST'])
    def create_texts(request):
        # Delete existing instance if exists
        HomePageTxts.objects.all().delete()
        
        serializer = TxtsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @api_view(['POST'])
    def update_about_text(request, lang):
        try:
            texts = HomePageTxts.objects.first()
            if not texts:
                return Response({"error": "No texts found"}, status=404)

            field_name = f'about_text_{lang}'
            if hasattr(texts, field_name):
                setattr(texts, field_name, request.data.get('text', ''))
                texts.save()
                return Response({field_name: getattr(texts, field_name)})
            return Response({"error": "Invalid language"}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

    @api_view(['POST'])
    def update_tech_text(request, lang):
        try:
            texts = HomePageTxts.objects.first()
            if not texts:
                return Response({"error": "No texts found"}, status=404)

            field_name = f'tech_text_{lang}'
            if hasattr(texts, field_name):
                setattr(texts, field_name, request.data.get('text', ''))
                texts.save()
                return Response({field_name: getattr(texts, field_name)})
            return Response({"error": "Invalid language"}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

    @api_view(['POST'])
    def update_partners_text(request, lang):
        try:
            texts = HomePageTxts.objects.first()
            if not texts:
                return Response({"error": "No texts found"}, status=404)

            field_name = f'partners_text_{lang}'
            if hasattr(texts, field_name):
                setattr(texts, field_name, request.data.get('text', ''))
                texts.save()
                return Response({field_name: getattr(texts, field_name)})
            return Response({"error": "Invalid language"}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


@api_view(['POST'])
def send_contact_email(request):
    try:
        data = request.data
        subject = f"Contact Form Submission from {data['name']} {data['surname']}"
        message = f"""
        Name: {data['name']}
        Surname: {data['surname']}
        Phone: {data['phone']}
        Email: {data['email']}
        Company: {data['company']}
        Technology: {data['tech']}
        Company Type: {data['CompanyType']}
        Message: {data['message']}
        """
        from_email = data['email']
        recipient_list = ['simonebatt51@gmail.com']
        
        send_mail(subject, message, from_email, recipient_list)
        return Response({'success': 'Email sent successfully!'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=400)