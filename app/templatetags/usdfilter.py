from django import template
register=template.Library()


def swap(value):
    return value.swapcase()
register.filter('swapcase',swap)


def remove(value,char):
    return value.replace(char,'')
register.filter('remove',remove)