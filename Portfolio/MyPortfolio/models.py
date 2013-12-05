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
    name = models.CharField(db_column='Name', max_length=20) # Field name made lowercase.
    id = models.IntegerField(db_column='Id', unique=True) # Field name made lowercase.
    red = models.IntegerField(db_column='Red') # Field name made lowercase.
    blue = models.IntegerField(db_column='Blue') # Field name made lowercase.
    green = models.IntegerField(db_column='Green') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Color'

class Colorscheme(models.Model):
    id = models.IntegerField(db_column='Id', unique=True) # Field name made lowercase.
    color1 = models.ForeignKey(Color, db_column='Color1') # Field name made lowercase.
    color2 = models.ForeignKey(Color, db_column='Color2') # Field name made lowercase.
    color3 = models.ForeignKey(Color, db_column='Color3') # Field name made lowercase.
    color4 = models.ForeignKey(Color, db_column='Color4', blank=True, null=True) # Field name made lowercase.
    color5 = models.ForeignKey(Color, db_column='Color5', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ColorScheme'

class Digitalimage(models.Model):
    id = models.IntegerField(db_column='Id', unique=True) # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255) # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255) # Field name made lowercase.
    imageid = models.ForeignKey('Image', db_column='ImageId') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'DigitalImage'

class Image(models.Model):
    id = models.IntegerField(db_column='Id', unique=True) # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=255) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Image'

class Page(models.Model):
    id = models.IntegerField(db_column='Id', unique=True) # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255) # Field name made lowercase.
    pageimageid = models.ForeignKey(Image, db_column='PageImageId') # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=255) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Page'

class Project(models.Model):
    id = models.IntegerField(db_column='Id', unique=True) # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255) # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255) # Field name made lowercase.
    yearcreated = models.DateField(db_column='YearCreated') # Field name made lowercase.
    sourcecodeid = models.ForeignKey('Sourcecode', db_column='SourceCodeId') # Field name made lowercase.
    imageid = models.ForeignKey(Image, db_column='ImageId') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Project'

class Sitetemplate(models.Model):
    id = models.IntegerField(db_column='Id', unique=True) # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255) # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255) # Field name made lowercase.
    pageimghome = models.ForeignKey(Page, db_column='PageImgHome') # Field name made lowercase.
    pageimggeneral = models.ForeignKey(Page, db_column='PageImgGeneral') # Field name made lowercase.
    pageimgabout = models.ForeignKey(Page, db_column='PageImgAbout') # Field name made lowercase.
    colorscheme = models.ForeignKey(Colorscheme, db_column='ColorScheme') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'SiteTemplate'

class Sourcecode(models.Model):
    id = models.IntegerField(db_column='Id', unique=True) # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=255) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'SourceCode'

