from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import QuestionBank
from .serializers import QuestionBankSerializer

@api_view(['GET','POST'])
def questionBank_list(request):

    if request.method == 'GET':
        questionBank = QuestionBank.objects.all()
        serializer = QuestionBankSerializer(questionBank, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionBankSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET'])
def questionBank_category(request):

    if request.method == 'GET':
        questionBank = QuestionBank.objects.all().filter(category=request.GET['category'])
        serializer = QuestionBankSerializer(questionBank, many=True)
        return Response(serializer.data)
