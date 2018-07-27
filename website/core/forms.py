from django import forms

from website.core.models import Sugestao


class SugestaoModelForm(forms.ModelForm):
    class Meta:
        model = Sugestao
        fields = '__all__'
