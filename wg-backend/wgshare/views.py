from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import wgshare
from .serializers import *

@api_view(['GET', 'POST'])
def wgshare_list(request):
    if request.method == 'GET':
        data = wgshare.objects.all()

        serializer = wgshareSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = wgshareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def wgshare_detail(request, pk):
    try:
        local_wgshare = wgshare.objects.get(pk=pk)
    except local_wgshare.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = wgshareSerializer(local_wgshare, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        local_wgshare.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
