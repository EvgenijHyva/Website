from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()  # метод сохраняет данные формы в БД
            messages.success(request, "Вы успешно зарегистрировались")  # при регистрации
            return HttpResponseRedirect(reverse("auth:login"))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    content = {
        "form": form,
        "title": "New account"
    }
    return render(request, "authapp/register.html", content)

def login(request):
    # авторизация пользователя
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            # print(user.__dict__)
            # messages.success(request, "Вы успешно авторизовались")
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("entry_point"))
    else:
        form = UserLoginForm()
    content = {
        "form": form,
        "title": "GeekShop - Авторизация"
    }
    return render(request, "authapp/login.html", content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("entry_point"))


##################################### for refactoring
def edit(request):
    context = {
        "title": "Редактирование"
    }
    if request.method == "POST":
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("main"))

    else:
        edit_form = UserEditForm(instance=request.user)
    context.update({
        "edit_form": edit_form
    })

    return render(request, "authapp/change_form.html", context)

