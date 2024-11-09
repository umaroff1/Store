from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['name','comment']
        widgets = {
            'name' :  forms.TextInput(attrs={'class':'form-control','minlength':3,}),
            'comment' :  forms.Textarea(attrs={'class':'form-control','minlength':3,'maxlength':550})
        }