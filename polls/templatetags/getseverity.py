from django import template
register = template.Library()

@register.filter()
def getseverity(dict, arg):
  """
  Usage:
  {% if text|contains:"http://" %}
  This is a link.
  {% else %}
  Not a link.
  {% endif %}
  """
  return dict.get("severity" + arg[-1])