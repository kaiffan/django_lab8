from django.forms import ModelForm, Form, IntegerField, CharField, PasswordInput
from main.models import User


class UserAddForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': PasswordInput
        }


class UserDeleteForm(Form):
    id_user = IntegerField(required=True, error_messages={
        'required': 'The id_user cannot be empty'
    })


class UserChangeForm(Form):
    id_user = IntegerField(required=True)
    email = CharField(required=True, label='Email', error_messages={
        'required': 'The email cannot be empty'
    })
    password = CharField(widget=PasswordInput, required=True, error_messages={
        'required': 'The password cannot be empty'
    })