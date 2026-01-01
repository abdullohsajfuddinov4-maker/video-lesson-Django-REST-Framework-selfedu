from django.forms import model_to_dict
from django.template.defaultfilters import title
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .serializers import WomenSerializer
from .models import Women
from rest_framework import generics



class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer



















    # def get(self,request):
    #     w = Women.objects.all()
    #     return Response({"posts":WomenSerializer(w , many=True).data})
    #
    # def post(self,request):
    #     serializer = WomenSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"post":serializer.data})
    #
    # def put(self, request, *args, **kwargs ):
    #     pk = kwargs.get("pk",None)
    #     if not pk:
    #         return Response({"error":"Method  PUT not allower"})
    #
    #     try:
    #         instance = Women.objects.get(pk=pk)
    #     except:
    #         Response({"error": "Method  PUT not allower"})
    #
    #     serializer = WomenSerializer(instance=instance ,data=request.data )
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"post":serializer.data})
    #
    # def delete(self,request,*args, **kwargs ):
    #     pk = kwargs.get("pk",None)
    #     if not pk:
    #         return Response({"error":"Method  delete not allower"})
    #
    #     try:
    #         instance = Women.objects.get(pk=pk)
    #     except:
    #         return Response({"error":"Method  DELETE not allower"})
    #
    #     instance.delete()
    #     return Response({"post":"DELETE"})













# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
