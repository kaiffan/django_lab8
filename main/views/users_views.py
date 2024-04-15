from django.shortcuts import render
from main.forms.user_forms import UserAddForm, UserDeleteForm, UserChangeForm
from django.contrib.messages import error
from main.models import User


def add_user(request):
    all_users = User.objects.all()
    if request.method == 'GET':
        form = UserAddForm()
        return render(request, 'add_user.html', {'form': form,
                                                 'title': 'Add user',
                                                 'all_users': all_users})
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            User.objects.create(email=email, password=password)
            all_users = User.objects.all()
            return render(request, 'add_user.html', {'form': form,
                                                     'title': 'Add user',
                                                     'all_users': all_users})
        else:
            return render(request, 'add_user.html', {'form': form,
                                                     'title': 'Add user',
                                                     'all_users': all_users})


def delete_user(request):
    all_users = User.objects.all()
    if request.method == 'GET':
        form = UserDeleteForm()
        return render(request, 'delete_user.html', {'form': form,
                                                    'title': 'Delete user',
                                                    'all_users': all_users})
    if request.method == 'POST':
        form = UserDeleteForm(request.POST)
        if form.is_valid():
            id_user = request.POST['id_user']
            user = User.objects.filter(id=id_user).first()
            if not user:
                error(request, 'Такого пользователя не существует')
                return render(request, 'delete_user.html', {'form': form,
                                                            'title': 'Delete user',
                                                            'all_users': all_users})
            user.delete()
            all_users = User.objects.all()
            return render(request, 'delete_user.html', {'form': form,
                                                        'title': 'Delete user',
                                                        'all_users': all_users})
        else:
            return render(request, 'delete_user.html', {'form': form,
                                                        'title': 'Delete user',
                                                        'all_users': all_users})


def change_user(request):
    all_users = User.objects.all()
    if request.method == 'GET':
        form = UserChangeForm()
        return render(request, 'delete_user.html', {'form': form,
                                                    'title': 'Delete user',
                                                    'all_users': all_users})
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            id_user = request.POST['id_user']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.filter(id=id_user).first()
            if not user:
                error(request, 'Такого пользователя не существует')
                return render(request, 'delete_user.html', {'form': form,
                                                            'title': 'Delete user',
                                                            'all_users': all_users})
            User.objects.get(id=id_user).update(email=email, password=password)
            all_users = User.objects.all()
            return render(request, 'delete_user.html', {'form': form,
                                                        'title': 'Delete user',
                                                        'all_users': all_users})
        else:
            return render(request, 'delete_user.html', {'form': form,
                                                        'title': 'Delete user',
                                                        'all_users': all_users})
