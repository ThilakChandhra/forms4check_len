from django import forms

def check_for_a(value):
    if value[0]=='t':
        raise forms.ValidationError('Name should not start with T')

def check_for_len(value):
    if len(value)<6:
        raise forms.ValidationError('len is less')
    

g=[('MALE','Male'),('FEMALE','Female')]
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    age=forms.IntegerField()
    email=forms.EmailField(validators=[check_for_a])
    phno=forms.IntegerField()
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)   