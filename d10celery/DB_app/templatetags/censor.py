from django import template

register = template.Library()

censored_words = ['редиска', 'Коронавирус','COVID', 'Потери', 'потерял', 'тревога']


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise TypeError('Ошибка: значение должно быть текстового типа')
    for word in censored_words:
        if word in value:
            value = value.replace(word, word[0] + "*" * len(word))
    return value
