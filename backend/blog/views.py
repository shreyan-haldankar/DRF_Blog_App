from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/'},
        {'GET': '/api/id'},
    ]

    return Response(routes)
