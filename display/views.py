from django.shortcuts import render
import pymysql as pym
from display.models import student
from django.http import HttpResponse

def home(request):
    return render(request,'display/home.html')

def show_tables(request):
    table=request.GET['table_name']
    myconn=pym.connect(user="subbu",password="subbu",database="menagerie",host="localhost")
    cursor=myconn.cursor()
    qstr="select * from %s" % (table)
    try:
        count=cursor.execute(qstr)
    except:
        res="Table Not Found"
        return render(request,'display/show_tables.html',{'result':res,'table':None})

    if count>0:
        res=cursor.fetchall()
    else:
        res="No records Found"   
        return render(request,'display/show_tables.html',{'result':res,'table':None})
   
    return render(request,'display/show_tables.html',{'result':res,'table':table})

def add_student(request):
    if request.method=='GET':
        return render(request,'display/add_student.html')
    else:
        s=student()
        s.st_id   = int(request.POST['stid'])
        s.st_name = request.POST['stname']
        s.save()
        return HttpResponse("User Added successfully")