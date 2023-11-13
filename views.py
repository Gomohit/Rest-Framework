from django.http import JsonResponse
from .models import food
from .serializers import foodSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def food_list(request,format=None):
    if request.method=='GET':
        food_data=food.objects.all()
        serializer=foodSerializer(food_data,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        try:
            f=food.objects.get(name=request.data['name'])
            return Response(status=status.HTTP_208_ALREADY_REPORTED)
        except food.DoesNotExist:    
            serializer=foodSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def food_detail(request,id,format=None):
    try:
        f=food.objects.get(pk=id)
    except food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=foodSerializer(f)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=foodSerializer(f,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
              
    elif request.method=='DELETE':
        f.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
