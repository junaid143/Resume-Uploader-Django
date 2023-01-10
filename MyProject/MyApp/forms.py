from cProfile import label
from secrets import choice
from django import forms
from .models import Resume

gender_choices = [('Male','Male'),('Female','Female'),('Not To Prefer','Not To Prefer')]

prog_choices = [('Python','Python'),('Java','Java'),('C','C'),('C++','C++'),('Sql','Sql'),('Css','Css'),('Html','Html')]



class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=gender_choices , widget=forms.RadioSelect)
    programming_language = forms.MultipleChoiceField(choices=prog_choices , widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        
        fields = ['fname' ,'lname','dob','gender','language','locality','city','state' ,'pin','mobile','email','programming_language','profile_photo']

        labels = {
            'fname': 'First Name',
            'lname' : 'Last Name',
            'dob':'Date Of Birth (dd/mm/yyy)',
            'pin':'Pin Code',
            'mobile':'Contact No',
            'email':'Email-ID',
        }

        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'dob' : forms.DateInput(attrs={'class':'form-control w-50'}),
            'language':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.Select(attrs={'class':'form-control w-50'}),
            'state' : forms.Select(attrs={'class':'form-control w-50'}),
            'pin' : forms.TextInput(attrs={'class':'form-control'}),
            'mobile' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email': forms.TextInput(attrs={'class' : 'form-control'}),
        }