from django import forms
g=[('MALE','male'),('FEMALE','female')]
c=[('PYTHON','python'),('JAVA','java'),('SQL','sql'),('HTML','html'),('DJANGO','django')]
class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=18)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    email=forms.EmailField()
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #courses=forms.MultipleChoiceField(choices=c)
    courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    address=forms.CharField(max_length=1000,widget=forms.Textarea)