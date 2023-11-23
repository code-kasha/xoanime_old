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
    "ca": "Catalan",
    "de": "German",
    "en": "English",
    "es": "Spanish",
    "es-la": "Spanish (Latin America)",
    "la": "Latin",
    "et": "Estonian",
    "el": "Greek",
    "id": "Indonesian",
    "fi": "Finnish",
    "ka": "Kannada",
    "my": "Malay",
    "mn": "Mongolian",
    "ko": "Korean",
    "he": "Hebrew",
    "hi": "Hindi",
    "hu": "Hungarian",
    "fa": "Persian",
    "ne": "Nepali",
    "pt-br": "Portugese",
    "fr": "French",
    "it": "Italian",
    "ja": "Japanese",
    "ja-ro": "Japanese (Romaji)",
    "pl": "Polish",
    "pt": "Portugese",
    "ru": "Russian",
    "sr": "Serbian",
    "ta": "Tamil",
    "th": "Thai",
    "sv": "Slovak",
    "uk": "Ukrainian",
    "ro": "Romanian",
    "tr": "Turkish",
    "zh-hk": "Chinese (Hong Kong)",
    "zh": "Chinese",
}
