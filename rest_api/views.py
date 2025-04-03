from rest_framework import viewsets
from .models import Project, HomePageTxts
from .serializer import ProjectSerializer, TxtsSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from urllib.parse import unquote

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
