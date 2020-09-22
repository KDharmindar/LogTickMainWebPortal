from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect,redirect, get_object_or_404
from django.utils import decorators
from django.views.generic import CreateView
from django.db import transaction
from .forms import UserForm, ProjectForm, TaskForm
from .models import *
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Main.main_models.ProcessedData import ProcessedData
from .Serializers import ProcessDataSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
import sys
import os
import base64
from django.core.files.base import ContentFile
from datetime import datetime



def base64_file(data):
    return ContentFile(base64.b64decode(data), datetime.now().strftime(("%d%m%Y%H%M%S")) + '.jpg')



class process_data_view(APIView):
    def get(self, request):
        process_data_list = []
        serializer = ProcessDataSerializer(process_data_list, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProcessDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






def home(request):
    return HttpResponseRedirect("/accounts/login/")

@login_required()
def profile(request):
    processes = []
    return render(request,"index.html", {'processes':processes})


@login_required()
def dashboard(request):
    processes = []
    
    processes = ProcessedData.objects.all()
    print("Does it have data ???")
    #print(processes[0].image_data)
    return render(request,"index.html", {'processes':processes})


@login_required()
def manage(request):
    #processes = []
    return render(request,"manage.html",{})


@login_required()
def screens(request):
    processes = []
    processes = ProcessData.objects.all()
    return render(request,"screens.html",{'processes':processes})

@csrf_exempt
#@api_view(['GET','POST',])
def get_process_data(request):
    process_data = ProcessedData()
    received_process_data = json.loads(request.POST.dict()['process_data'])
    
    # print(received_process_data['process_id'])
    
    # for k,v in received_process_data.items():
    #     print('Property Name is ' + k + ' and value is ' + str(v))
    
    # print(received_process_data['process_id'])
    
        
    process_data.process_id = int(str(received_process_data['process_id']))
    # process_data.task_id = int(str(received_process_data['task_id']))
    # process_data.project_id = int(str(received_process_data['project_id']))
    # process_data.start_time = float(str(received_process_data['start_time']))
    # process_data.end_time = float(str(received_process_data['end_time']))
    # #process_data.duration = received_process_data['duration']
    # process_data.duration = 1
    # process_data.weekend_id = int(str(received_process_data['weekend_id']))
    # process_data.user_id = 1
    process_data.image_data = base64_file(str(received_process_data['image_data'])) 
    #process_data.image_thumbnail_data = ImageModel.objects.create(received_process_data['image_data']) 
    print('image data is here.')
    print(process_data.image_data)
    try:
        process_data.save()
        print("saved in db")
    except Exception as ex:

        print("Oops!", sys.exc_info()[0], "occurred.", str(ex.args[0]))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(ex)

    return HttpResponse({'Data Received...'}, status=200)
     
       
#     if request.METHOD == 'GET':
#         return Response({'Error: No data received'}, status=400)
#     else:
#         return HttpResponse(request.DATA, status=200, content_type='application/json')





@login_required()
def report_overview(request):
    #processes = []
    return render(request,"reports/overview.html",{})



def login(request):
    return render(request, "login.html",{})

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserForm(instance=request.user)
        
    return render(request, "account/signup.html", {})

@login_required()
def new_project(request):
    if request.method == "POST":
        project = Project(created_by=request.user)
        form = ProjectForm(instance=project, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_project')
    else:
        form = ProjectForm()
    return render(request, "project.html",{'form':form})

@login_required()
def new_task(request):
    if request.method == "POST":
        task = ProjectTask(created_by=request.user)
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_task')
    else:
        form = TaskForm()
    return render(request, "task.html",{'form':form})

