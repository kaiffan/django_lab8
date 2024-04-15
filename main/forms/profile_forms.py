from django.forms import ModelForm, IntegerField, Form, CharField
from main.models import Profile


class ProfileAddForm(ModelForm):
    id_user = IntegerField(required=True)

    class Meta:
        model = Profile
        fields = ['name', 'age', 'city']


class ProfileDeleteForm(Form):
    id_profile = IntegerField(required=True, error_messages={
        'required': 'The id_user cannot be empty'
    })


class ProfileChangeForm(Form):
    id_profile = IntegerField(required=True)
    name = CharField(required=True, label='Name', error_messages={
        'required': 'The email cannot be empty'
    })
    age = IntegerField(label='Age',required=True, error_messages={
        'required': 'The password cannot be empty'
    })
    city = CharField(label='City', required=True, error_messages={
        'required': 'The password cannot be empty'
    })
    id_user = IntegerField(required=True)
