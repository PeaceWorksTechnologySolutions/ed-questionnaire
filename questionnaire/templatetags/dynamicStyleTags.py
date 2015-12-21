#!/usr/bin/python

from django import template
from models import QuestionSet

register = template.Library()


@register.filter(name="getAssociatedStylesheets")
def getAssociatedStylesheets(inclusionTag):

    return "smiley"
