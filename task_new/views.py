from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from django.db.models import F
import time
from django.http import JsonResponse
from django.http import HttpResponseForbidden
from lock_tokens.exceptions import AlreadyLockedError, UnlockForbiddenError
from lock_tokens.sessions import check_for_session, lock_for_session, unlock_for_session
import threading

@api_view(['GET'])
def try_first_time(request):
    api_urls = {
        'list': 'start your project',

    }
    a = Task(given_id=0)
    a.save()

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    lock = threading.Lock()
    while (1):
        try:
            with lock:



                Task.objects.filter(id=1).update(given_id=F("given_id") + 1)

                serializer = TaskSerializer(Task.objects.all(), many=True)



                return Response(serializer.data)
        except AlreadyLockedError:
            time.sleep(2)

            pass

@api_view(['GET'])

def reset(request):
    lock = threading.Lock()
    while (1):
        try:
            with lock:

                obj = Task.objects.get(id=1)
                if obj.exists():
                    lock_for_session(obj, request.session)
                    obj.given_id=0
                    obj.save()
                    unlock_for_session(obj, request.session)
                else:
                    a = Task(given_id=0)
                    a.save()

                return JsonResponse({"given_id": "newly value set to 0 "})
        except AlreadyLockedError:
            time.sleep(2)

            pass


