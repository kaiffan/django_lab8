from django.urls import path
from .views import profile_views, users_views, main_view, subscribe_views

urlpatterns = [
    path('main_page/', main_view.main_page),
    path('add_user/', users_views.add_user, name='add_user'),
    path('delete_user/', users_views.delete_user, name='delete_user'),
    path('change_user/', users_views.change_user, name='change_user'),
    path('add_profile/', profile_views.add_profile, name='add_profile'),
    path('delete_profile/', profile_views.delete_profiles, name='delete_profile'),
    path('change_profile/', profile_views.change_profiles, name='change_profile'),
    path('subscribe/', subscribe_views.subscribe, name='subscribe'),
    path('unsubscribe/', subscribe_views.unsubscribe, name='unsubscribe')
]
