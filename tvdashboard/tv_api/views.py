from http.client import HTTPResponse
import json
from django.shortcuts import render
from .serializers import *
from .models import *
from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.views import APIView
from datetime import datetime, time
from django.utils import timezone

# Create your views here.




class LinePhase(APIView):
    
    def get(self, request):
        lines = Line.objects.all()
        serializer = LineSerializer(lines, many=True)
        return Response(serializer.data)


class SinglePhase(APIView):

    
    def get(self, request, pk=None, format=None):
        time = timezone.now().time()
        shifts = ShiftsTv.objects.filter(start__lte=time, end__gte = time).first()
        shift_target = ShiftTargetsTv.objects.filter(line__id=1, shift=shifts).all()
        serializer = ShiftTargetsTvSerializer(shift_target, many=True)
        wip = WipTv.objects.filter(line__id=1,shift=shifts).all()
        wipserializer = WipTvSerializer(wip, many=True)
        cont = {"shift":serializer.data, "wip":wipserializer.data}
        return Response(cont)
    
    def post(self, request, *args, **kwargs):
        shift_serializers = ShiftTargetsTvSerializer(data=request.data)
        wip_serializer = WipTvSerializer(data=request.data)
        if shift_serializers.is_valid() and wip_serializer.is_valid():
            shift_serializers.save()
            wip_serializer.save()
            return Response({"msg": "Data Created"})
        return Response(shift_serializers.errors & wip_serializer.errors)


class SmallMediumPhase(APIView):
    
    def get(self, request, pk=None, format=None):
        time = timezone.now().time()
        shifts = ShiftsTv.objects.filter(start__lte=time, end__gte=time).first()
        shift = ShiftTargetsTv.objects.filter(line__id=2, shift=shifts).all()
        serializer = ShiftTargetsTvSerializer(shift, many=True)
        wip = WipTv.objects.filter(line__id=2).all()
        wipserializer = WipTvSerializer(wip, many=True)
        cont = {"shift": serializer.data, "wip": wipserializer.data}
        return Response(cont)

    def post(self, request, *args, **kwargs):
            shift_serializers = ShiftTargetsTvSerializer(data=request.data)
            wip_serializer = WipTvSerializer(data=request.data)
            if shift_serializers.is_valid() and wip_serializer.is_valid():
                shift_serializers.save()
                wip_serializer.save()
                return Response({"msg": "Data Created"})
            return Response(shift_serializers.errors & wip_serializer.errors)

   
class LargePhase(APIView):
    
    def get(self, request, pk=None, format=None):
        time = timezone.now().time()
        shifts = ShiftsTv.objects.filter(start__lte=time, end__gte=time).first()
        shift = ShiftTargetsTv.objects.filter(line__id=3, shift=shifts).all()
        serializer = ShiftTargetsTvSerializer(shift, many=True)
        wip = WipTv.objects.filter(line__id=3).all()
        wipserializer = WipTvSerializer(wip, many=True)
        cont = {"shift": serializer.data, "wip": wipserializer.data}
        return Response(cont)

    def post(self, request, *args, **kwargs):
        shift_serializers = ShiftTargetsTvSerializer(data=request.data)
        wip_serializer = WipTvSerializer(data=request.data)
        if shift_serializers.is_valid() and wip_serializer.is_valid():
            shift_serializers.save()
            wip_serializer.save()
            return Response({"msg": "Data Created"})
        return Response(shift_serializers.errors & wip_serializer.errors)
    

class IndustrialPhase(APIView):
    
    def get(self, request, pk=None, format=None):
        time = timezone.now().time()
        shifts = ShiftsTv.objects.filter(start__lte=time, end__gte=time).first()
        shift = ShiftTargetsTv.objects.filter(line__id=4, shift=shifts).all()
        serializer = ShiftTargetsTvSerializer(shift, many=True)
        wip = WipTv.objects.filter(line__id=4).all()
        wipserializer = WipTvSerializer(wip, many=True)
        cont = {"shift": serializer.data, "wip": wipserializer.data}
        return Response(cont)
    
    def post(self, request, *args, **kwargs):
        shift_serializers = ShiftTargetsTvSerializer(data=request.data)
        wip_serializer = WipTvSerializer(data=request.data)
        if shift_serializers.is_valid() and wip_serializer.is_valid():
            shift_serializers.save()
            wip_serializer.save()
            return Response({"msg": "Data Created"})
        return Response(shift_serializers.errors & wip_serializer.errors)

