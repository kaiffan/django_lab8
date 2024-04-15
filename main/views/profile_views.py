from django.contrib.messages import error
from django.shortcuts import render

from main.forms.profile_forms import ProfileAddForm, ProfileDeleteForm, ProfileChangeForm
from main.models import Profile, User


def add_profile(request):
    all_profiles = Profile.objects.all()
    all_users = User.objects.all()
    if request.method == 'GET':
        form = ProfileAddForm()
        return render(request, 'add_profiles.html', {'form': form,
                                                     'title': 'Add profile',
                                                     'all_profiles': all_profiles,
                                                     'all_users': all_users})
    if request.method == 'POST':
        form = ProfileAddForm(request.POST)
        if form.is_valid():
            profile = Profile()
            id_user = request.POST['id_user']
            user = User.objects.filter(id=id_user).first()
            if not user:
                error(request, 'Такого пользователя не существует')
                return render(request, 'add_profiles.html', {'form': form,
                                                             'title': 'Add profile',
                                                             'all_profiles': all_profiles,
                                                             'all_users': all_users})
            profile.user = user
            profile.name = request.POST['name']
            profile.age = request.POST['age']
            profile.city = request.POST['city']
            profile.save()
            all_profiles = Profile.objects.all()
            return render(request, 'add_profiles.html', {'form': form,
                                                         'title': 'Add profile',
                                                         'all_profiles': all_profiles,
                                                         'all_users': all_users})
        else:
            return render(request, 'add_profiles.html', {'form': form,
                                                         'title': 'Add profile',
                                                         'all_profiles': all_profiles,
                                                         'all_users': all_users})


def delete_profiles(request):
    all_profiles = Profile.objects.all()
    all_users = User.objects.all()
    if request.method == 'GET':
        form = ProfileDeleteForm()
        return render(request, 'delete_profiles.html', {'form': form,
                                                        'title': 'Add profile',
                                                        'all_profiles': all_profiles,
                                                        'all_users': all_users})
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST)
        if form.is_valid():
            id_profile = request.POST['id_profile']
            profile = Profile.objects.filter(id=id_profile).first()
            if not profile:
                error(request, 'Такого профиля не существует')
                return render(request, 'delete_profiles.html', {'form': form,
                                                                'title': 'Add profile',
                                                                'all_profiles': all_profiles,
                                                                'all_users': all_users})
            profile.delete()
            all_profiles = Profile.objects.all()
            return render(request, 'delete_profiles.html', {'form': form,
                                                            'title': 'Add profile',
                                                            'all_profiles': all_profiles,
                                                            'all_users': all_users})
        else:
            return render(request, 'delete_profiles.html', {'form': form,
                                                            'title': 'Add profile',
                                                            'all_profiles': all_profiles,
                                                            'all_users': all_users})


def change_profiles(request):
    all_profiles = Profile.objects.all()
    all_users = User.objects.all()
    if request.method == 'GET':
        form = ProfileChangeForm()
        return render(request, 'change_profiles.html', {'form': form,
                                                        'title': 'Add profile',
                                                        'all_profiles': all_profiles,
                                                        'all_users': all_users})
    if request.method == 'POST':
        form = ProfileChangeForm(request.POST)
        if form.is_valid():
            id_profile = request.POST['id_profile']
            profile = Profile.objects.get(id=id_profile)
            if not profile:
                error(request, 'Такого профиля не существует')
                return render(request, 'change_profiles.html', {'form': form,
                                                                'title': 'Delete user',
                                                                'all_users': all_users})
            profile.name = request.POST['name']
            profile.age = request.POST['age']
            profile.city = request.POST['city']
            id_user = request.POST['id_user']
            user_exists = User.objects.filter(id=id_user).first()
            if not user_exists:
                error(request, 'Такого пользователя не существует')
                return render(request, 'change_profiles.html', {'form': form,
                                                                'title': 'Delete user',
                                                                'all_users': all_users})
            profile.user = user_exists
            profile.save()
            all_profiles = Profile.objects.all()
            return render(request, 'change_profiles.html', {'form': form,
                                                            'title': 'Add profile',
                                                            'all_profiles': all_profiles,
                                                            'all_users': all_users})
        else:
            return render(request, 'change_profiles.html', {'form': form,
                                                            'title': 'Add profile',
                                                            'all_profiles': all_profiles,
                                                            'all_users': all_users})
