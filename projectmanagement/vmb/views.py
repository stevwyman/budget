from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models.functions import TruncMonth
from django.db.models import Sum, Count
from django.template import loader
from pathlib import Path

import csv
import os
import math
from os import walk
from logging import getLogger
import pandas as pd

from .models import ExpenditureItem, Project

from datetime import datetime


# Create your views here.

logger = getLogger(__name__)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def read(request):

    BASE_DIR = Path(__file__).resolve().parent.parent
    import_folder = os.path.join(BASE_DIR, "import")

    filenames = next(walk(import_folder), (None, None, []))[2]  # [] if no file

    date_format = '%d-%b-%Y'

    saved_entries = 0

    for filename in filenames:
        abs_file_path = os.path.join(import_folder, filename)
        data=pd.read_csv(abs_file_path,sep='\t', encoding='utf-16')

        for index, row in data.iterrows():

            trans_id = row.get('Trans Id')
            items = ExpenditureItem.objects.filter(trans_id = trans_id)
            if items.exists():
                logger.debug("Trans Id %i already existing, skipping", trans_id)
                continue

            project_id = row.get('Project')
            try:
                project = Project.objects.get(oracle_id = project_id)
            except Exception:
                logger.warning("No Project for Oracle ID %s, skipping entry", project_id)
                continue

            item = ExpenditureItem()

            item.trans_id = trans_id
            item.project = project

            item.task = row.get('Task')
            item.expnd_type = row.get('Project')

            date_obj = datetime.strptime(row.get('Item Date'), date_format)

            item.item_date = date_obj
            item.employee_supplier = row.get('Employee/Supplier')
            item.quantity = row.get('Quantity')
            item.uom = row.get('UOM')

            item.proj_func_burdened_cost = row.get('Proj Func Burdened Cost')
            item.project_burdened_cost = row.get('Project Burdened Cost')
            
            ar = row.get('Accrued Revenue')
            if (math.isnan(ar)):
                ar = 0.0
            item.accrued_revenue = ar

            ba = row.get('Bill Amount')
            if (math.isnan(ba)):
                ba = 0.0
            item.bill_amount = ba
            
            item.comment = row.get('Comment')

            item.save()
            saved_entries += 1

    logger.info("stored %i entries to database", saved_entries)

    return HttpResponse("Yupp - read the file and imported " + str(saved_entries))

def detail_by_project(request, project_id):
                      
    if request.method == "GET":
        project = get_object_or_404(Project, pk=project_id)

    data = project.expenditureitem_set.filter(uom='Hours')

    hours_by_month = data.annotate(month=TruncMonth('item_date')).values('month').annotate(sum=Sum('quantity'))                  
    hours_sum = data.aggregate(sum=Sum('quantity'))                  

    template = loader.get_template("vmb/detail_by_project.html")
    context = {
        "hours_by_month": hours_by_month,
        "hours_sum": hours_sum,
        "project": project,
    }
    return HttpResponse(template.render(context, request))

def detail_by_project_month(request, project_id, month):

    if request.method == "GET":
        project = get_object_or_404(Project, pk=project_id)
    
    target_month = datetime.strptime(month, '%d%b%Y')

    filter_month = target_month.month
    filter_year = target_month.year

    data = project.expenditureitem_set.filter(
        uom='Hours',
        item_date__year__gte=filter_year,
        item_date__month__gte=filter_month,
        item_date__year__lte=filter_year,
        item_date__month__lte=filter_month)
    
    hours_by_employee = data.values('task', 'employee_supplier').order_by('task').annotate(sum=Sum('quantity'))
    sum_by_month = data.aggregate(hours_sum=Sum('quantity')) 

    template = loader.get_template("vmb/detail_by_project_month.html")
    context = {
        "hours_by_employee": hours_by_employee,
        "sum_by_month": sum_by_month,
        "project": project,
        "month": filter_month,
        "year": filter_year,
    }
    return HttpResponse(template.render(context, request))


def overview(request):

    data = ExpenditureItem.objects.filter(uom='Hours')

    hours_by_project = data.values('project_id').order_by('project').annotate(hours_sum=Sum('quantity'))  

    template = loader.get_template("vmb/overview.html")
    context = {
        "hours_by_project": hours_by_project,
    }
    return HttpResponse(template.render(context, request))