from django.shortcuts import render,HttpResponse
from bittu.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
   
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


def services(request):
    return render(request,"services.html")

def contact(request):
   if request.method == "POST":
        FirstName = request.POST.get("FirstName")
        LastName = request.POST.get("LastName")
        Province = request.POST.get("Province")
        City = request.POST.get("City")
        Address = request.POST.get("Address")
        Address2 = request.POST.get("Address2")
        EmailAddress = request.POST.get("EmailAddress")
        PhoneNumber = request.POST.get("PhoneNumber")
       
        desc = request.POST.get("desc")
        contact= Contact(FirstName=FirstName, LastName=LastName, Province=Province, City=City, Address=Address, Address2=Address2,
        EmailAddress=EmailAddress, PhoneNumber=PhoneNumber, desc=desc)

        contact.save()
        messages.success(request, "Your Details Have Been Saved!")

   return render(request,"contact.html")
    

