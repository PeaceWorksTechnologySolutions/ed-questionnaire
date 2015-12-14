#!/usr/bin/python

from django import template

register = template.Library()


@register(name="getAssociatedStylesheets")
def getAssociatedStylesheets(inclusionTag):

    return "smiley"
