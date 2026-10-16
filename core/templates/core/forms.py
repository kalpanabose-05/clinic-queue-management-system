from django import forms

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(
        max_length=10, 
        min_length=10,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter 10-digit phone number',
            'pattern': '[0-9]{10}',  # HTML5 validation
            'title': 'Enter exactly 10 digits',
        })
    )
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))