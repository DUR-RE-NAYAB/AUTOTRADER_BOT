from django.shortcuts import render,redirect
from django.http import request,HttpRequest,HttpResponse
# from .scraper import scrape_data
from .scraper import scrape_data
import csv


# Create your views here.
def index(request):
    return render(request,'webpage/index.html')

def export_csv(request):
    data = scrape_data()   ## call fucntion from scrape data  ###  data contain a list of all the cars
    print('viwes')
    cleaned_data = []
    for datas in data:
        cleaned_data.append(datas.strip())
    print(cleaned_data)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    writer = csv.writer(response)
    writer.writerow(['Data'])
    for item in cleaned_data:
        writer.writerow([item])
    return response