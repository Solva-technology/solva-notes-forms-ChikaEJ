from django.shortcuts import get_object_or_404, render

from .models import UserProfile


def all_users(request):
    users = UserProfile.objects.select_related('user')
    context = {'users': users}
    return render(request, 'users/all_users.html', context)


def user_detail(request, id):
    user_profile = get_object_or_404(
        UserProfile.objects.select_related('user'),
        user__id=id
    )
    return render(
        request,
        'users/user_detail.html',
        {'user_profile': user_profile}
    )
