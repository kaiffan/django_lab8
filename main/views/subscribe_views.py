from django.contrib.messages import error
from django.shortcuts import render

from main.models import User, Subscription
from main.forms.subscrube import AddSubscribe, DeleteSubscribe


def subscribe(request):
    all_users = User.objects.all()
    all_subs = Subscription.objects.all()
    if request.method == 'GET':
        form = AddSubscribe()
        return render(request, 'subscribe.html', {'form': form,
                                                  'title': 'Subscribe',
                                                  'all_users': all_users,
                                                  'all_subs': all_subs})
    if request.method == 'POST':
        form = AddSubscribe(request.POST)
        if form.is_valid():
            id_user_subs = request.POST["id_user_subs"]
            id_user_sb = request.POST["id_user_sb"]
            if id_user_subs == id_user_sb:
                error(request, 'На самого себя подписаться нельзя')
                return render(request, 'subscribe.html', {'form': form,
                                                          'title': 'Subscribe',
                                                          'all_users': all_users,
                                                          'all_subs': all_subs})
            user_subs = User.objects.filter(id=id_user_subs).first()
            if not user_subs:
                error(request, 'Такого пользователя не существует')
                return render(request, 'subscribe.html', {'form': form,
                                                          'title': 'Subscribe',
                                                          'all_users': all_users,
                                                          'all_subs': all_subs})
            user_sb = User.objects.filter(id=id_user_sb).first()
            if not user_sb:
                error(request, 'Такого пользователя не существует')
                return render(request, 'subscribe.html', {'form': form,
                                                          'title': 'Subscribe',
                                                          'all_users': all_users,
                                                          'all_subs': all_subs})
            Subscription.objects.create(subscriber=user_subs, subscribed_to=user_sb)
            all_users = User.objects.all()
            all_subs = Subscription.objects.all()
            return render(request, 'subscribe.html', {'form': form,
                                                      'title': 'Subscribe',
                                                      'all_users': all_users,
                                                      'all_subs': all_subs})
        else:
            return render(request, 'subscribe.html', {'form': form,
                                                      'title': 'Subscribe',
                                                      'all_users': all_users,
                                                      'all_subs': all_subs})


def unsubscribe(request):
    all_users = User.objects.all()
    all_subs = Subscription.objects.all()
    if request.method == 'GET':
        form = DeleteSubscribe()
        return render(request, 'unsubscribe.html', {'form': form,
                                                    'title': 'Unsubscribe',
                                                    'all_users': all_users,
                                                    'all_subs': all_subs})
    if request.method == 'POST':
        form = DeleteSubscribe(request.POST)
        if form.is_valid():
            id_user_unsubs = request.POST["id_user_unsubs"]
            id_user_unsb = request.POST["id_user_unsb"]
            if id_user_unsubs == id_user_unsb:
                error(request, 'На самого себя подписаться нельзя')
                return render(request, 'unsubscribe.html', {'form': form,
                                                            'title': 'Unsubscribe',
                                                            'all_users': all_users,
                                                            'all_subs': all_subs})
            user_subs = User.objects.filter(id=id_user_unsubs).first()
            if not user_subs:
                error(request, 'Такого пользователя не существует')
                return render(request, 'unsubscribe.html', {'form': form,
                                                            'title': 'Unsubscribe',
                                                            'all_users': all_users,
                                                            'all_subs': all_subs})
            user_sb = User.objects.filter(id=id_user_unsb).first()
            if not user_sb:
                error(request, 'Такого пользователя не существует')
                return render(request, 'unsubscribe.html', {'form': form,
                                                            'title': 'Unsubscribe',
                                                            'all_users': all_users,
                                                            'all_subs': all_subs})
            subs_user = Subscription.objects.filter(subscriber=id_user_unsubs, subscribed_to=id_user_unsb).first()
            if not subs_user:
                error(request, 'Такой пары подписчиков нет')
                return render(request, 'unsubscribe.html', {'form': form,
                                                            'title': 'Unsubscribe',
                                                            'all_users': all_users,
                                                            'all_subs': all_subs})
            Subscription.objects.filter(subscriber=id_user_unsubs, subscribed_to=id_user_unsb).delete()
            all_users = User.objects.all()
            all_subs = Subscription.objects.all()
            return render(request, 'unsubscribe.html', {'form': form,
                                                        'title': 'Unsubscribe',
                                                        'all_users': all_users,
                                                        'all_subs': all_subs})
        else:
            return render(request, 'unsubscribe.html', {'form': form,
                                                        'title': 'Unsubscribe',
                                                        'all_users': all_users,
                                                        'all_subs': all_subs})
