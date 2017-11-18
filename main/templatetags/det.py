# -*- coding: utf-8 -*-

from django import template
from django.utils.translation import gettext as _

register = template.Library()
STATUS_CHOICES = (
    (1, _("سنة")),
    (2, _("ثلاثة أشهر")),
    (3, _("ستة أشهر")),
    (4, _("شهر")),
    (5, _("15 يوما")),
    (6, _("لا يوجد"))
)

@register.filter
def det(value):
    x = value-1
    return STATUS_CHOICES[x][1]
