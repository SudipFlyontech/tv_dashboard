from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Line, ShiftsTv, ShiftTargetsTv, WipTv



class ShiftTvSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftsTv
        fields = '__all__'
    


class ShiftTargetsTvSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftTargetsTv
        fields = ['shift', 'target', 'actual', 'variance', 'line']
        
        # def get_shift_target_tv(self, obj):
        #     shift_target = ShiftTargetsTv.objects.filter()
        #     shiftserializer = ShiftTargetsTvSerializer(shift_target, many=True)
        #     return (shiftserializer.data)
        


class WipTvSerializer(serializers.ModelSerializer):
    class Meta:
        model = WipTv
        fields = ['shift', 'process', 'wip', 'line']
        
class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = ['line']