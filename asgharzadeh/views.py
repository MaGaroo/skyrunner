import asyncio
import sys
from asgiref.sync import sync_to_async

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.conf import settings

from .skyroom import Skyroom
from .models import NightName


def hello_world_view(request):
    return HttpResponse('Hello world!')


def class_members_view(request, name):
    if name not in settings.ROOMS:
        raise Http404('Class not found')
    room_id = settings.ROOMS[name]
    room = Skyroom(
        settings.SKYROOM_URI,
        room_id,
        settings.SKYROOM_USERNAME,
        settings.SKYROOM_PASSWORD,
        settings.SKYROOM_SURNAME,
    )
    if request.method == 'POST':
        get_object_or_404(
            NightName,
            name=request.POST.get('night'),
        )
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
