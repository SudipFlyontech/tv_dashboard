from pyexpat import model
from django.db import models


# class ShiftTargetsTv(models.Model):
#     shift = models.CharField(db_column='Shift', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
#     target = models.IntegerField(db_column='Target')  # Field name made lowercase.
#     actual = models.IntegerField(db_column='Actual')  # Field name made lowercase.
#     variance = models.IntegerField(db_column='Variance')  # Field name made lowercase.
#     line = models.CharField(db_column='Line', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'shift_targets_tv'


# class ShiftsTv(models.Model):
#     shift = models.CharField(db_column='Shift', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
#     start = models.TimeField(db_column='Start')  # Field name made lowercase.
#     end = models.TimeField(db_column='End')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'shifts_tv'


# class WipTv(models.Model):
#     shift = models.CharField(db_column='Shift', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
#     process = models.CharField(db_column='Process', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
#     wip = models.IntegerField(db_column='WIP')  # Field name made lowercase.
#     line = models.CharField(db_column='Line', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'wip_tv'


class Line(models.Model):
    line = models.CharField(max_length=100)
    
class ShiftsTv(models.Model):
    shift = models.CharField(max_length=100)  # Field name made lowercase.
    start = models.TimeField()  # Field name made lowercase.
    end = models.TimeField()  # Field name made lowercase.


class ShiftTargetsTv(models.Model):
    shift = models.ForeignKey(ShiftsTv, on_delete=models.CASCADE)  # Field name made lowercase.
    target = models.IntegerField()  # Field name made lowercase.
    actual = models.IntegerField()  # Field name made lowercase.
    variance = models.IntegerField()  # Field name made lowercase.
    line = models.ForeignKey(Line, on_delete=models.CASCADE)  # Field name made lowercase.

class WipTv(models.Model):
    shift = models.ForeignKey(ShiftsTv, on_delete=models.CASCADE) # Field name made lowercase.
    process = models.CharField(max_length=100)  # Field name made lowercase.
    wip = models.IntegerField()  # Field name made lowercase.
    line = models.ForeignKey(Line, on_delete=models.CASCADE)  # Field name made lowercase.

    