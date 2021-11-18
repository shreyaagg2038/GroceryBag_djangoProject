from django import forms
from . import models

class DateInput(forms.DateInput):
    input_type = 'date'

class AddItem(forms.ModelForm):
    class Meta:
        model = models.item
        fields = ['item_name','item_quantity','item_status','item_date']
        widgets= {
            'item_name': forms.TextInput(attrs={'placeholder': 'Item name','class':'form-control'}),
            'item_quantity': forms.TextInput(attrs={'placeholder': 'Item quantity','class':'form-control'}),
            'item_status': forms.Select(attrs={'class':'form-control'}),
            'item_date':DateInput(attrs={'placeholder': 'mm/dd/yyyy','class':'form-control'}),
        }
class UpdateItem(forms.ModelForm):
    class Meta:
        model = models.item
        fields = ['item_name','item_quantity','item_status','item_date']
        widgets= {
            'item_name': forms.TextInput(attrs={'placeholder': 'Item name','class':'form-control'}),
            'item_quantity': forms.TextInput(attrs={'placeholder': 'Item quantity','class':'form-control'}),
            'item_status': forms.Select(attrs={'class':'form-control'}),
            'item_date':DateInput(attrs={'placeholder': 'mm/dd/yyyy','class':'form-control'}),
        }
