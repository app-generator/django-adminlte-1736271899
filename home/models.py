# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Veículos(models.Model):

    #__Veículos_FIELDS__
    equipe = models.TextField(max_length=255, null=True, blank=True)
    odometro = models.IntegerField(null=True, blank=True)
    ano = models.IntegerField(null=True, blank=True)
    ultima_inspecao = models.DateTimeField(blank=True, null=True, default=timezone.now)
    proxima_inspecao = models.DateTimeField(blank=True, null=True, default=timezone.now)
    ultima_troca_oleo = models.DateTimeField(blank=True, null=True, default=timezone.now)
    proxima_troca_oleo = models.DateTimeField(blank=True, null=True, default=timezone.now)
    ticket_aberto = models.BooleanField()
    parado = models.BooleanField()
    aguardando_pecas = models.BooleanField()

    #__Veículos_FIELDS__END

    class Meta:
        verbose_name        = _("Veículos")
        verbose_name_plural = _("Veículos")


class Serviços(models.Model):

    #__Serviços_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)
    descrição = models.TextField(max_length=255, null=True, blank=True)
    lista_peças = models.IntegerField(null=True, blank=True)
    tempo = models.TextField(max_length=255, null=True, blank=True)
    modelo = models.TextField(max_length=255, null=True, blank=True)
    interno = models.BooleanField()

    #__Serviços_FIELDS__END

    class Meta:
        verbose_name        = _("Serviços")
        verbose_name_plural = _("Serviços")



#__MODELS__END
