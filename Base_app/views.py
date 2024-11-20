from django.shortcuts import render,HttpResponse
from Base_app.models import *

# Create your views here.
def HomeView(request):
    item=Items.objects.all()
    list=ItemList.objects.all()
    review=Feedback.objects.all()
    return render(request,'home.html',{'items':item,'list':list,'review':review})

def AboutView(request):
    data=AboutUs.objects.all()
    return render(request,'about.html',{'data':data})

def MenuView(request):
    item=Items.objects.all()
    list=ItemList.objects.all()
    return render(request,'menu.html',{'items':item,'list':list})

def BookTableView(request):
    if request.method=='POST':
        name=request.POST.get('user_name')
        email=request.POST.get('user_email')
        phone=request.POST.get('phone_number')
        table=request.POST.get('total_person')
        booking_date=request.POST.get('booking_date')
        if name!=None and email!=None and phone!=None and table!=None and booking_date!=None:
            data=BookTable(Name=name,Phone_number=phone,Email=email,Total_persons=table,Booking_Date=booking_date)
            data.save()
    return render(request,'book_table.html')

def FeedbackView(request):
    if request.method=='POST':
        name=request.POST.get('user_name')
        description=request.POST.get('Description')
        rating=request.POST.get('rating')
        image=request.FILES.get('image')
        # if name!=None and description!=None and rating!=None and image!=None:
        data=Feedback(Name=name,Description=description,Rating=rating,Image=image)
        print(data)
        data.save()
    return render(request,"feedback.html")