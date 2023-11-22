import datetime, json

from django import template

import pycountry

COUNTRY_NAMES = {country.alpha_2: country.name for country in pycountry.countries}

register = template.Library()

MONTHS = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

TYPES = {
    "sub": "English Sub",
    "dub": "English Dub",
}


@register.filter(name="title")
def title(title):
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
def timestamp_to_str(value):
    return datetime.utcfromtimestamp(value)


@register.filter
def timestr_to_str(value):
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")


@register.filter(name="to_int")
def to_int(value):
    return int(value)


@register.filter(name="month")
def month(value):
    return f"{MONTHS[value]},"


@register.filter(name="type")
def type(value):
    return TYPES[value]


@register.filter(name="suffix")
def suffix(day):
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
    return COUNTRY_NAMES[code]
