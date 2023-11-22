import datetime, json

from django import template

from .helpers import COUNTRIES, MONTHS, TYPES, LANGUAGES


register = template.Library()


@register.filter(name="title")
def title(title):
    """Return title."""
    if isinstance(title, str):
        return title

    elif isinstance(title, dict):
        return (
            title.get("english")
            or title.get("romaji")
            or title.get("userPreffered")
            or title.get("native")
        )


@register.filter
def to_json(obj):
    return json.dumps(obj)


@register.filter
def load_json(obj):
    return json.loads(obj)


@register.filter
def time_from_timestamp(value):
    """Return time from a timestamp."""
    return datetime.utcfromtimestamp(value)


@register.filter
def time_from_timestr(value):
    """Return time from a time string."""
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")


@register.filter(name="to_int")
def to_int(value):
    """Type conversion - INT"""
    return int(value)


@register.filter(name="month")
def month(value):
    """Return month from number."""
    return f"{MONTHS[value]},"


@register.filter(name="type")
def type(value):
    """Return Audio Type Sub/Dub"""
    return TYPES[value]


@register.filter(name="suffix")
def suffix(day):
    """Return proper suffix for the day."""
    if day % 10 == 1 and day % 100 != 11:
        suffix = "st"
    elif day % 10 == 2 and day % 100 != 12:
        suffix = "nd"
    elif day % 10 == 3 and day % 100 != 13:
        suffix = "rd"
    else:
        suffix = "th"
    return f"{day}{suffix}"


@register.filter(name="country")
def country(code):
    """Return country name from country code."""
    return COUNTRIES[code]


@register.filter(name="lang")
def lang(code):
    """Return language name from code"""
    if code == "id":
        return "Indonesian"
    return LANGUAGES[code]
