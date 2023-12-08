from django import forms

class DepositForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    amount = forms.IntegerField(label="Amount", required=True, min_value=50)
    country = forms.CharField(label='Country', required=True)
    address = forms.CharField(label='Address')
    city = forms.CharField(label="Town/City", required=True)
    phone = forms.CharField(label="Phone", required=True)
    email = forms.CharField(label="Email", required=True)
    description = forms.CharField(widget=forms.Textarea)