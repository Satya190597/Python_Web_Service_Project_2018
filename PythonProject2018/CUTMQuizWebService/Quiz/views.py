from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import QuestionBank
from .serializers import QuestionBankSerializer

@api_view(['GET','POST'])
def questionBank_list(request):

    if request.method == 'GET':
        questionBank = QuestionBank.all()
        serializer = QuestionBankSerializer(questionBank, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionBankSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
