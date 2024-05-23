from django import forms
from .models import Family, Word

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['name', 'meaning', 'description']

class WordForm(forms.ModelForm):
    family = forms.ModelMultipleChoiceField(queryset=Family.objects.all(), widget=forms.SelectMultiple())
    class Meta:
        model = Word
        fields = ['name', 'connotation','definition', 'family']
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     families = []
    #     for family in Family.objects.all():
    #         families.append((family.id, family.name))            
    #     self.fields['family'].initial = 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)