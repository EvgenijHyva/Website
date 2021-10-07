CYRILLIC_LATTERS = {
    u'а': u'a', u'б': u'b', u'в': u'v',  u'г': u'g',
    u'д': u'd', u'е': u'e', u'ё': u'jo', u'ж': u'zh',
    u'з': u'z', u'и': u'i', u'й': u'j', u'к': u'k',
    u'л': u'l', u'м': u'm', u'н': u'n', u'о': u'o',
    u'п': u'p', u'р': u'r', u'с': u's', u'т': u't',
    u'У': u'u', u'ф': u'f', u'х': u'h', u'ц': u'c',
    u'ч': u'ch', u'ш': u'sh', u'щ': u'sch', u'ь': u'',
    u'ы': u'yi', u'ъ': u'-', u'э': u'je', u'ю': u'ju',
    u'я': u'ja'
}

def from_cyrillic_to_slug(text: str):
    text = text.replace(" ", "_").lower()
    tmp = ""
    for ch in text:
        tmp += CYRILLIC_LATTERS.get(ch, ch)
    return tmp
