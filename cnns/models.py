# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AreaEn(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_parent_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_code = models.CharField(max_length=20, blank=True, null=True)
    area_name = models.CharField(max_length=50, blank=True, null=True)
    area_level = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_en'
