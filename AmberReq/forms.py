from django import forms

from .models import Contact









class RequestForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            "placeholder": "Your title",
            "class": "form-control",
            "id": "my-id-for-textarea",
            "rows": 20,
            'cols': 120
        }
    )
    )

    descriptions = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your description",
                "class": "form-control",
                "id": "my-id-for-textarea",
                "rows": 20,
                'cols': 120
            }
        )
    )
    phone = forms.IntegerField(label='', widget=forms.TextInput(
        attrs={
            "placeholder": "+996..",
            "class": "form-control",
            "id": "my-id-for-textarea",
            "rows": 20,
            'cols': 120
        }
    ))

    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={
            "placeholder": "Your email",
            "class": "form-control",
            "id": "my-id-for-textarea",
            "rows": 20,
            'cols': 120
        }
    ))

    class Meta:
        model = Contact
        fields = [
            'username',
            'descriptions',
            'phone',
            'email'
        ]
