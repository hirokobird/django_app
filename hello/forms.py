from django import forms

class HelloForm(forms.Form):
    data=[
        ('one', 'item 1'),
        ('two', 'item 2'),
        ('three', 'item 3'),
        ('four', 'item 4'),
        ('five', 'item 5')
    ]
    choice = forms.MultipleChoiceField(label='radio', \
            choices=data, widget=forms.SelectMultiple(attrs={'size':6,
                'class':'form-select'}))

class SessionForm(forms.Form):
    session = forms.CharField(label='session', required=False, \
            widget=forms.TextInput(attrs={'class':'form-control'}))

# check = forms.NullBooleanField(label='Check')
# check = forms.BooleanField(label='checkbox', required=False)
# name = forms.CharField(label='name', \
#     widget=forms.TextInput(attrs={'class':'form-control'}))
# mail = forms.CharField(label='mail', \
#     widget=forms.TextInput(attrs={'class':'form-control'}))
# age = forms.IntegerField(label='age', \
#     widget=forms.NumberInput(attrs={'class':'form-control'}))