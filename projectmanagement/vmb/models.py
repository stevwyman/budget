from django.db import models

class Project(models.Model):
    oracle_id = models.BigIntegerField("Oracle ID", primary_key=True)
    name = models.CharField("Name", max_length=200)
    pub_date = models.DateTimeField("date published")

class ExpenditureItem(models.Model):
    trans_id = models.IntegerField("Trans Id", unique=True, null=False, primary_key=True)	
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.CharField("Task", max_length=5)	
    expnd_type = models.CharField("Expnd Type", max_length=55)	
    item_date = models.DateField("Item Date")
    employee_supplier = models.CharField("Employee/Supplier", max_length=255)	
    quantity = models.DecimalField("Quantity", decimal_places=2, max_digits=12)	
    uom = models.CharField("UOM", max_length=55)
    proj_func_burdened_cost = models.DecimalField("Proj Func Burdened Cost", decimal_places=2, max_digits=12)
    project_burdened_cost = models.DecimalField("Project Burdened Cost", decimal_places=2, max_digits=12)
    accrued_revenue = models.DecimalField("Accrued Revenue", decimal_places=2, max_digits=12)
    bill_amount= models.DecimalField("Bill Amount", decimal_places=2, max_digits=12)
    comment = models.CharField("Comment", max_length=255, null=True)	
