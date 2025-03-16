
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# NB: We are using this "'class': 'form-control'," because we are using Bootstrap in our project.
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))


    # meta is rule in django framework where we will define which field from the module class we
    # want to show in our form
    class Meta:
        model = User
        
        # if we use 'fields = __all__' all the fields in the user model could be include.
        # But for selective field to use, we use this.
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
