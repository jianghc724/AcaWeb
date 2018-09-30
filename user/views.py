from django.shortcuts import render
from codex.baseerror import *
from codex.baseview import APIView
from user.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from AcaWeb.settings import *

import requests
import json
import html
import os
# Create your views here.


class UserRegister(APIView):
    def get(self):
        pass

    def post(self):
        self.check_input('username', 'password1', 'password2', 'email')
        info = self.input
        if info['password1'] != info['password2']:
            raise LogicError('Password not the same')
        _u = User.objects.filter(username=info['username'])
        if _u:
            raise LogicError('Username used')
        u = User()
        u.username = info['username']
        u.set_password(info['password1'])
        u.email = info['email']
        u.save()


class UserActivation(APIView):
    def get(self):
        pass

    def post(self):
        pass


class GetUser(APIView):
    def get(self):
        if self.request.user.is_authenticated:
            return self.request.user.id
        else:
            raise UserStatusError("You haven't log in")

    def post(self):
        pass


class GetFileStatus(APIView):
    def get(self):
        if self.request.user.is_authenticated:
            u = self.request.user
            p = UserProfile.objects.filter(user=u)
            if p:
                p = UserProfile.objects.get(user=u)
            else:
                p = UserProfile.objects.create(user=u)
                p.save()
            return p.fileUrl
        else:
            raise UserStatusError("You haven't log in")

    def post(self):
        pass


class UserLogin(APIView):
    def get(self):
        if self.request.user.is_authenticated:
            return
        else:
            raise UserStatusError("You haven't log in")

    def post(self):
        self.check_input('user_id', 'password')
        user = authenticate(username=self.input['user_id'], password=self.input['password'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return
            else:
                raise UserStatusError('You have not activate your email')
        raise ValidateError('username or password wrong')


class UserLogout(APIView):
    def get(self):
        pass

    def post(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        else:
            raise UserStatusError("You haven't log in")


class FormEdit(APIView):
    def get(self):
        u = self.request.user
        p = UserProfile.objects.filter(user=u)
        result = {}
        if p:
            p = UserProfile.objects.get(user=u)
        else:
            p = UserProfile.objects.create(user=u)
            p.save()
        result = {
            'phone': p.phone,
            'name': p.name,
            'major': p.major,
            'grade': p.grade,
            'gender': p.gender,
            'writing': p.writing,
            'movie': p.movie,
            'camera': p.camera,
            'photoshop': p.photoshop,
            'xuanchuan': p.xuanchuan,
            'caiwu': p.caiwu,
            'wailian': p.wailian,
            'xueyuan': p.xueyuan,
            'fileUrl': p.fileUrl,
            'firstNoon': p.firstNoon,
            'firstNight': p.firstNight,
            'secondNoon': p.secondNoon,
            'secondNight': p.secondNight,
            'userStatus': p.userStatus,
        }


    def post(self):
        u = self.request.user
        self.check_input('phone','name','major','grade','gender','writing',
            'movie','camera','photoshop','xuanchuan','caiwu','wailian',
            'xueyuan','firstNoon','firstNight','secondNoon','secondNight')
        info = self.input
        p = UserProfile.objects.get(user=u)
        p.phone=info['phone']
        p.name=info['name']
        p.major=info['major']
        p.grade=info['grade']
        p.gender=info['gender']
        p.writing=info['writing']
        p.movie=info['movie']
        p.camera=info['camera']
        p.photoshop=info['photoshop']
        p.xuanchuan=info['xuanchuan']
        p.caiwu=info['caiwu']
        p.wailian=info['wailian']
        p.xueyuan=info['xueyuan']
        p.firstNoon=info['firstNoon']
        p.firstNight=info['firstNight']
        p.secondNoon=info['secondNoon']
        p.secondNight=info['secondNight']
        p.save()


class UploadFile(APIView):
    def get(self):
        pass

    def post(self):
        f = self.request.FILES.get("file", None)
        u = self.request.user
        i = u.username
        if not f:
            raise FileError('No file to upload')
        _i = os.path.join(MEDIA_ROOT, i)
        os.mkdir(_i)
        destination = open(os.path.join(_i, f.name), 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
        p = UserProfile.objects.get(user=u)
        _p = os.path.join(i, f.name)
        p.fileUrl=_p
        p.save()
