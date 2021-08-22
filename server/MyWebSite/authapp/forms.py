from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.forms import forms

from users.models import CustomUser

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")

    # дополнительные параметры:
    def __init__(self, *args, **kwargs):  # переопределяя метод нужно указать
        super(UserLoginForm, self).__init__(*args, **kwargs)  # все переменные что было созданы выше их нужно
        # использовать

        self.fields["username"].widget.attrs['placeholder'] = "Введите имя пользователя"  # добавим placeholder
        self.fields["password"].widget.attrs['placeholder'] = "Введите пароль"
        # добавим класс в input циклом for:
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control py-4"


class UserRegisterForm(UserCreationForm):  # форма регистрации register.html
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "password1", "password2", "phone", "gender")

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['placeholder'] = "Enter your full name"
        self.fields["phone"].widget.attrs["placeholder"] = "123-456-7890 or +123-123-123-1234"
        self.fields["phone"].widget.attrs["pattern"] = "([\+]?[\d]{3}-?)?0?[\d]{2}-?[\d]{3}-?[\d]{4}"
        self.fields["phone"].widget.attrs["required"] = True

        self.fields["email"].widget.attrs['placeholder'] = "your@mail.domen"
        self.fields["email"].widget.attrs['required'] = True

        self.fields["gender"].widget.attrs['required'] = True

        self.fields["first_name"].widget.attrs['placeholder'] = "Your name"
        self.fields["first_name"].widget.attrs['required'] = True
        self.fields["last_name"].widget.attrs['placeholder'] = "Your lastname "

        self.fields["password1"].widget.attrs['placeholder'] = "Create password (Min 8 character)"
        self.fields["password1"].widget.attrs['pattern'] = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"
        self.fields["password1"].widget.attrs['title'] = "Please include at least 1 uppercase char, 1 lowercase char, and 1 number."
        self.fields["password1"].widget.attrs['required'] = True

        self.fields["password2"].widget.attrs['placeholder'] = "Confirm password"
        self.fields["password2"].widget.attrs['pattern'] = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control py-4"
            field.help_text = ''


    ############################################     for refactoring
class UserEditForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "email", "avatar", "age")

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""
            if field_name == "password":
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды")
        return data


