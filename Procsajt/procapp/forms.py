from django import forms


class ProcForm(forms.Form):
    p = forms.IntegerField(label='P: ')
    n = forms.IntegerField(label='n: ')
    i = forms.DecimalField(label='i: ')
    z1 = forms.IntegerField(label='z1: ')
    beta = forms.IntegerField(label='β: ')
    fi = forms.DecimalField(label='φ: ')
    x = forms.IntegerField(label='x: ')
    ka = forms.DecimalField(label='Ka: ')

    
    
    


