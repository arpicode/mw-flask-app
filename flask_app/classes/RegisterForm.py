from wtforms import Form, StringField, TextAreaField, PasswordField, validators


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Password do not match.')
    ])
    confirm = PasswordField('Confirm Password')
