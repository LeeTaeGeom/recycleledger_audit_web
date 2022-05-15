from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="result/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

# views.py에 작성했던 Report 모델 예시

class Report(models.Model):
    date = models.CharField(max_length=200,null=True)
    PO_name = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True) 
    collector = models.CharField(max_length=200,null=True) 
    quantity = models.IntegerField(null=True) 
    converted_qty = models.FloatField(null=True) 
    conllecting_company = models.CharField(max_length=200,null=True)
