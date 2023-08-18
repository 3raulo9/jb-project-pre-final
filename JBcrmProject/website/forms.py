from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record


class CustomSignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
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
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. Max 150 characters: letters, digits, @/./+/-/_ only.</small></span>'

        password_help_text = (
            '<ul class="form-text text-muted small">'
            '<li>Password should differ from personal info.</li>'
            '<li>Minimum 8 characters.</li>'
            '<li>Avoid common passwords.</li>'
            '<li>Not entirely numeric.</li>'
            '</ul>'
        )

        for field_name in ['password1', 'password2']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'placeholder': f'Enter {field_name.replace("password", "Password")}'})
            self.fields[field_name].label = ''
            self.fields[field_name].help_text = password_help_text

        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Re-enter the same password for verification.</small></span>'


class CustomAddRecordForm(forms.ModelForm):
    field_attrs = {
        "placeholder": ["First Name", "Last Name", "Email", "Phone", "Address", "City", "State", "Zipcode"],
        "class": "form-control"
    }

    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": field_attrs["placeholder"][0], "class": field_attrs["class"]}),
        label=""
    )
    field_attrs["placeholder"].pop(0)

    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": field_attrs["placeholder"][0], "class": field_attrs["class"]}),
        label=""
    )
    field_attrs["placeholder"].pop(0)

    email = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": field_attrs["placeholder"][0], "class": field_attrs["class"]}),
        label=""
    )
    field_attrs["placeholder"].pop(0)

    phone = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": field_attrs["placeholder"][0], "class": field_attrs["class"]}),
        label=""
    )
    field_attrs["placeholder"].pop(0)

    address = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": field_attrs["placeholder"][0], "class": field_attrs["class"]}),
        label=""
    )
    field_attrs["placeholder"].pop(0)

    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": field_attrs["placeholder"][0], "class": field_attrs["class"]}),
        label=""
    )
    field_attrs["placeholder"].pop(0)

    state = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": field_attrs["placeholder"][0], "class": field_attrs["class"]}),
        label=""
    )
    field_attrs["placeholder"].pop(0)

    zipcode = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": field_attrs["placeholder"][0], "class": field_attrs["class"]}),
        label=""
    )

    class Meta:
        model = Record
        exclude = ("user",)
