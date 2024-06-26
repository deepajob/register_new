from django import forms
from app.models import Record
class RecordForm(forms.ModelForm):
    class Meta:
        model=Record
        field=['name','email']
        widgets={
            'name':forms.TextInput(),
            'email':forms.EmailField()
        }