from django.shortcuts import render,redirect

from django.views.generic import View

from crm.forms import EmployeeForm

from crm.models import Employee

# Create your views here.

class EmployeeCreateView(View):

    template_name ="employee_add.html"

    form_class = EmployeeForm

    def get(self,request,*args,**kwargs):

        form_instance = self.form_class

        return render(request,self.template_name,{'form':form_instance})

    def post(self,request,*args,**kwargs):

        form_data = request.POST

        form_instance = self.form_class(form_data,files=request.FILES)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("employee-list")
        
        return render(request,self.template_name,{'form':form_instance})

class EmployeeListView(View):

    template_name = "employee_list.html" 

    form_class = EmployeeForm

    def  get(self,request,*args,**kwargs):

        qs = Employee.objects.all()

        return render(request,self.template_name,{'data':qs})
    
class EmployeeDetailView(View):

    template_name = "employee_detail.html"

    def get(self,request,*args,**kwargs):

        id = kwargs.get("id")

        qs = Employee.objects.get(id=id)

        return render(request,self.template_name,{"data":qs})

class EmployeeDeleteView(View):

    template_name = "employee_delete.html"

    def get(self,request,*args,**kwargs):

        id = kwargs.get("id")

        Employee.objects.get(id=id).delete()

        return redirect("employee-list")

class EmployeeUpdateView(View):

    template_name="employee_update.html"

    form_class = EmployeeForm

    def get(self,request,*args,**kwargs):

        id = kwargs.get("id")

        employee_object = Employee.objects.get(id=id)

        form_instance = self.form_class(instance=employee_object)

        return render(request,self.template_name,{'form':form_instance})
    
    def post(self,request,*args,**kwargs):

        id = kwargs.get("id")

        employee_object = Employee.objects.get(id=id)

        form_data = request.POST

        form_instance = self.form_class(form_data,files=request.FILES,instance=employee_object)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("employee-list")
        
        return render(request,self.template_name,{'form':form_instance})

