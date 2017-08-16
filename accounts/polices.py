from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render, redirect

class IsRoot(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.nivel == 0:
            return redirect('accounts:dashboard')
        return super(IsRoot, self).dispatch(request, *args, **kwargs)

class IsAdm(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.nivel == 1 and not request.user.nivel == 0:
            return redirect('accounts:dashboard')
        return super(IsAdm, self).dispatch(request, *args, **kwargs)