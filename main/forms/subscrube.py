from django.forms import Form, IntegerField


class AddSubscribe(Form):
    id_user_subs = IntegerField(required=True, label='Пользователь, который подписывается', error_messages={
        'required': 'The id_user cannot be empty'
    })
    id_user_sb = IntegerField(required=True, label='Пользователь, на которого подписываются', error_messages={
        'required': 'The id_user cannot be empty'
    })


class DeleteSubscribe(Form):
    id_user_unsubs = IntegerField(required=True, label='Пользователь, который отписывается', error_messages={
        'required': 'The id_user cannot be empty'
    })
    id_user_unsb = IntegerField(required=True, label='Пользователь, от которого отписываются', error_messages={
        'required': 'The id_user cannot be empty'
    })