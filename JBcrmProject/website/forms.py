from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

# CustomSignUpForm for user registration
class CustomSignUpForm(UserCreationForm):
    # Email field with attributes for styling
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    # First name field with attributes for styling
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    # Last name field with attributes for styling
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        # Update username field attributes for styling
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = ''
        # Customize help text for username field
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. Max 150 characters: letters, digits, @/./+/-/_ only.</small></span>'

        # Password help text
        password_help_text = (
            '<ul class="form-text text-muted small">'
            '<li>Password should differ from personal info.</li>'
            '<li>Minimum 8 characters.</li>'
            '<li>Avoid common passwords.</li>'
            '<li>Not entirely numeric.</li>'
            '</ul>'
        )

        # Update password fields attributes for styling and help text
        for field_name in ['password1', 'password2']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'placeholder': f'Enter {field_name.replace("password", "Password")}'})
            self.fields[field_name].label = ''
            self.fields[field_name].help_text = password_help_text
        # Update password2 field help text
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Re-enter the same password for verification.</small></span>'

# CustomAddRecordForm for adding records
class CustomAddRecordForm(forms.ModelForm):
    field_attrs = {
        "placeholder": ["First Name", "Last Name", "Email", "Phone", "Address", "City", "State", "Zipcode"],
        "class": "form-control"
    }

    # Form fields with attributes for styling
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": field_attrs["placeholder"][0], "class": field_attrs["class"]}),
        label=""
    )
    field_attrs["placeholder"].pop(0)

    # Repeated pattern for other fields...

    # Define the model and excluded fields
    class Meta:
        model = Record
        exclude = ("user",)
