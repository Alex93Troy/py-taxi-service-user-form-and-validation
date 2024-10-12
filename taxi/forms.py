from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core import validators
from taxi.models import Driver


class DriverCreationForm(UserCreationForm):
    license_number = forms.CharField(
        min_length=8,
        max_length=8,
        validators=[
            validators.RegexValidator(
                regex=r"^[A-Z]{3}\d{5}$",
                message="The license number must consist"
                        " of 3 uppercase letters followed by 5 digits.",
            )
        ],
    )

    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "license_number",
            "first_name",
            "last_name",
            "email",
        )


class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(
        min_length=8,
        max_length=8,
        validators=[
            validators.RegexValidator(
                regex=r"^[A-Z]{3}\d{5}$",
                message="The license number must consist"
                        " of 3 uppercase letters followed by 5 digits.",
            )
        ],
    )

    class Meta:
        model = Driver
        fields = ("license_number",)
