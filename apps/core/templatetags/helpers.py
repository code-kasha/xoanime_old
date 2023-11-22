import pycountry


COUNTRIES = {country.alpha_2: country.name for country in pycountry.countries}

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


LANGUAGES = {
    "ar": "Arabic",
    "bn": "Bengali",
    "bg": "Bulgarian",
    "cs": "Czech",
    "de": "German",
    "en": "English",
    "es": "Spanish",
    "fi": "Finnish",
    "ka": "Kannada",
    "my": "Malay",
    "ko": "Korean",
    "he": "Hebrew",
    "hi": "Hindi",
    "fr": "French",
    "it": "Italian",
    "ja": "Japanese",
    "pl": "Polish",
    "pt": "Portugese",
    "ru": "Russian",
    "sr": "Serbian",
    "ta": "Tamil",
    "th": "Thai",
    "tr": "Turkish",
    "zh-hk": "Chinese (Hong Kong)",
    "zh": "Chinese",
}
