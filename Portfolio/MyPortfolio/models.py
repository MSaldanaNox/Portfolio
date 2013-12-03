# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Color(models.Model):
    class Meta:
        managed = False
        db_table = 'Color'

class Colorscheme(models.Model):
    class Meta:
        managed = False
        db_table = 'ColorScheme'

class Design(models.Model):
    class Meta:
        managed = False
        db_table = 'Design'

class Digitalimage(models.Model):
    class Meta:
        managed = False
        db_table = 'DigitalImage'

class Image(models.Model):
    class Meta:
        managed = False
        db_table = 'Image'

class Page(models.Model):
    class Meta:
        managed = False
        db_table = 'Page'

class Project(models.Model):
    sourcecode = models.CharField(db_column='SourceCode', max_length=255) # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20) # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50) # Field name made lowercase.
    yearcreated = models.DateField(db_column='YearCreated') # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=60) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Project'

class Sitetemplate(models.Model):
    class Meta:
        managed = False
        db_table = 'SiteTemplate'

class Sourcecode(models.Model):
    class Meta:
        managed = False
        db_table = 'SourceCode'

