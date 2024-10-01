from django.shortcuts import redirect, render

from app.models import *


def home(request):
    return render(request,'index.html')
def student_reg(request):
    if request.method=='POST':
        data=request.POST
        
        name=data.get("student_name")
        age=data.get("age")
        address=data.get("address")
        
        student.objects.create(name=name,age=age,address=address)
        
        
    students=student.objects.all()
    context={'students':students}
    return render(request,'register.html',context)
    

# Create your views here.