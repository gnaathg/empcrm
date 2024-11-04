from django import forms

from crm.models import Employee

from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):


    class Meta:

        model =Employee

        fields= "__all__"

        widgets ={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "address":forms.Textarea(attrs={"class":"form-control","rows":5}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "date_of_join":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "gender":forms.Select(attrs={"class":"form-control" "form-select"}),
            "picture":forms.FileInput(attrs={"class":"form-control"}),

        }

class SignupForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ["username","password","email"]

class SigninForm(forms.Form):

    username = forms.CharField()

    password = forms.CharField(widget=forms.PasswordInput())