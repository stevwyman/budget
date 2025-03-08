from django.db import models

# Create your models here.

class Project(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class ExpenditureItem(models.Model):
    question = models.ForeignKey(Project, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    trans_id = models.IntegerField("Trans Id")	
    Project	
    task = models.CharField("Task", max_length=5)	
    expnd_type = models.CharField("Expnd Type", max_length=55)	
    item_date = models.DateField("Item Date")	
    employee_supplier = models.CharField("Employee/Supplier", max_length=255)	
    quantity = models.DecimalField("Quantity", )	
    uom = models.CharField("UOM", max_length=55)
    	
    Proj Func Burdened Cost	
    Project Burdened Cost	
    Accrued Revenue	
    Bill Amount	
    Comment	
    Expnd Org	
    Non-Labor Resource	
    Non-Labor Resource Org	
    [ ]	
    Prvdr Legal Entity	
    Recvr Legal Entity	


