from django.shortcuts import render
from codex.baseerror import *
from codex.baseview import APIView
from user.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import requests
import json
import html
# Create your views here.


class UserRegister(APIView):
    def get(self):
        pass

    def post(self):
        pass


class UserActivation(APIView):
    def get(self):
        pass

    def post(self):
        pass


class UserLogin(APIView):
    def get(self):
        pass

    def post(self):
        pass


class UserLogout(APIView):
    def get(self):
        pass

    def post(self):
        pass


class FormEdit(APIView):
    def get(self):
        pass

    def post(self):
        pass


class UploadFile(APIView):
    def get(self):
        pass

    def post(self):
        pass
