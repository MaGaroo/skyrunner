from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.conf import settings
from django.utils import timezone

from .skyroom import Skyroom
from .models import NightName, Room


def hello_world_view(request):
    return HttpResponse('Hello world!')


def class_members_view(request, name):
    vc = get_object_or_404(Room, name=name)
    room = Skyroom(
        vc.uri or settings.SKYROOM_URI,
        vc.code,
        vc.username,
        vc.password,
        vc.surname,
    )
    if request.method == 'POST':
        nn = get_object_or_404(
            NightName,
            name=request.POST.get('night'),
        )
        if timezone.now() < nn.start or timezone.now() > nn.end:
            raise Http404()
        users = room.users_list()
        room.promote(int(request.POST.get('uid')))
    else:
        users = room.users_list()
    return render(
        request,
        'asgharzadeh/members.html',
        {
            'users': users,
        }
    )
