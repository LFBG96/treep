from django import forms
from .models import Roteiro,Natureza, Gastronomia,Praia,Cultura 

class RoteiroForm(forms.ModelForm):
    
    natureza = forms.ModelMultipleChoiceField(queryset=Natureza.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)
    gastronomia = forms.ModelMultipleChoiceField(queryset=Gastronomia.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)
    praia = forms.ModelMultipleChoiceField(queryset=Praia.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
    cultura = forms.ModelMultipleChoiceField(queryset=Cultura.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["gastronomia"].widget.attrs.update({"class": "special"})
        self.fields["gastronomia"].widget.attrs.update({"style": "display: none;"})
        
        """
    class Meta:
        model = Roteiro
        fields = '__all__'
        data = forms.DateField()
        #fields = ['nome','posicao','gastronomia','praia']
        #nome = forms.CharField(widget=forms.TextInput(attrs={'class':'special'}))
        #widgets  =  { 'praia': forms.Select(attrs = {'onchange' : "Mudarestado();"}) }
        