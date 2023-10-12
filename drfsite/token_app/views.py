from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import ListView, CreateView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from uuid import uuid4
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import *


class GetTokenAPI(APIView):
    def get(self, request):
        rand_token = str(uuid4())
        t = Token(token=rand_token)
        t.save()

        return Response({'token': t.token})


def view_goods(request):
    token = request.GET.get('token', '')
    db_tokens = list(Token.objects.values('token'))
    db_tokens = [t['token'] for t in db_tokens]
    if not token:
        return HttpResponse('Token must be presented', status=401)
    if token in db_tokens:
        goods = Good.objects.all()
        return render(request, 'token_app/goods.html', {'goods': goods, 'token': token})
    else:
        return HttpResponse('Token is invalid', status=401)


def new_good(request):
    token = request.GET.get('token', '')
    db_tokens = list(Token.objects.values('token'))
    db_tokens = [t['token'] for t in db_tokens]
    if not token:
        return HttpResponse('Token must be presented', status=401)
    if token in db_tokens:
        if request.method == 'POST':
            form = GoodForm(request.POST)
            if form.is_valid():
                Good.objects.create(**form.cleaned_data)
                url = '/goods/?token=' + token
                return redirect(url)
        else:
            form = GoodForm()

        return render(request, 'token_app/create_goods.html', context={'form': form, 'token': token})
    else:
        return HttpResponse('Token is invalid', status=401)

#"token": "0e85acb2-330d-4479-907d-d8799c29bfa8"