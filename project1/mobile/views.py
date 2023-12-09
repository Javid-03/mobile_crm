from django.shortcuts import render,redirect
from django.views import View 
from mobile.forms import MobileForm
from mobile.models import Mobile
from django.contrib import messages


class Viewmobile(View):
    def get(self,request):
        data=MobileForm()
        return render(request,"view_mobile.html",{"data":data})
    
    def post(self,request):
        data=MobileForm(request.POST)
        if data.is_valid():
            Mobile.objects.create(**data.cleaned_data)
            messages.success(request,"Success")
        else:
            messages.error(request,"Failed")

        return render(request,"view_mobile.html",{"data":data})
    

class Listmobile(View):
    def get(self,request):
        data=Mobile.objects.all()
        return render(request,"list_mobile.html",{"data":data})

    def post(self,request):
        brand=request.POST.get("mob-product")
        data=Mobile.objects.filter(brand=brand)
        return render(request,"list_mobile.html",{"data":data})



class Detailsmobile(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        data=Mobile.objects.get(id=id)
        return render(request,"details_mobile.html",{"data":data})


class Updatemobile(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        obj=Mobile.objects.get(id=id)
        data=MobileForm(instance=obj)
        return render(request,"mobile_edit.html",{"data":data})

    def post(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        obj=Mobile.objects.get(id=id)
        data=MobileForm(request.POST,instance=obj)
        if data.is_valid():
            data.save()
        else:
            print("Failed")
        return redirect('mob-all')
    

class Deletemobile(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        data=Mobile.objects.get(id=id).delete()
        return redirect('mob-all')

        