from django.shortcuts import render
from codex.baseerror import *
from codex.baseview import APIView
from user.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
            p = UserProfile.objcets.create(user=u)
            p.save()
        result = {
            'phone': p.phone,
            'name': p.name,
            'major': p.major,
            'grade': p.grade,
            'gender': p.gender,
            'sightsing': p.sightsing,
            'othersightsing': p.othersightsing,
            'theory': p.theory,
            'instrument': p.instrument,
            'instrumentKind': p.instrumentKind,
            'bbox': p.bbox,
            'bboxAbility': p.bboxAbility,
            'record': p.record,
            'recordAbility': p.recordAbility,
            'compose': p.compose,
            'composeAbility': p.composeAbility,
            'midi': p.midi,
            'midiAbility': p.midiAbility,
            'writing': p.writing,
            'movie': p.movie,
            'camera': p.camera,
            'photoshop': p.photoshop,
            'otherAbility': p.otherAbility,
            'schoolUnion': p.schoolUnion,
            'majorUnion': p.majorUnion,
            'otherClub': p.otherClub,
            'otherWork': p.otherWork,
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
        self.check_input('phone','name','major','grade','gender','sightsing',
            'othersightsing','theory','instrument','instrumentKind','bbox',
            'bboxAbility','record','recordAbility','compose','composeAbility',
            'midi','midiAbility','writing','movie','camera','photoshop',
            'otherAbility','schoolUnion','majorUnion','otherClub','otherWork',
            'xuanchuan','caiwu','wailian','xueyuan','firstNoon','firstNight',
            'secondNoon','secondNight')
        info = self.input
        p = UserProfile.objects.get(user=u)
        p.update(phone=info['phone'],name=info['name'],major=info['major'],
            grade=info['grade'],gender=info['gender'],sightsing=info['sightsing'],
            othersightsing=info['othersightsing'],theory=info['theory'],
            instrument=info['instrument'],instrumentKind=info['instrumentKind'],
            bbox=info['bbox'],bboxAbility=info['bboxAbility'],
            record=info['record'],recordAbility=info['recordAbility'],
            compose=info['compose'],composeAbility=info['composeAbility'],
            midi=info['midi'],midiAbility=info['midiAbility'],
            writing=info['writing'],movie=info['movie'],camera=info['camera'],
            photoshop=info['photoshop'],otherAbility=info['otherAbility'],
            schoolUnion=info['schoolUnion'],majorUnion=info['majorUnion'],
            otherClub=info['otherClub'],otherWork=info['otherWork'],
            xuanchuan=info['xuanchuan'],caiwu=info['caiwu'],
            wailian=info['wailian'],xueyuan=info['xueyuan'],
            firstNoon=info['firstNoon'],firstNight=info['firstNight'],
            secondNoon=info['secondNoon'],secondNight=info['secondNight'])
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
        destination = open(os.path.join(MEDIA_ROOT, i, f.name), 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
        p = UserProfile.objects.get(user=u)
        _p = os.path.join(i, f.name)
        p.update(fileUrl=_p)
        p.save()
