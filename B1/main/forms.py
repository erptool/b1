from django import forms
from .models import Tip

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['category', 'title', 'details', 'file_attachment' ]

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    

#class AttachmentsForm(forms.ModelForm):
    #attachments = forms.FileField(widget=forms.MultipleHiddenInput(attrs={'multiple': True}))
