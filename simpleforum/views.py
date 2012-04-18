from django.views.generic.simple import direct_to_template

def index(request, template_name='simpleforum/index.haml'):
    """Forum index view"""
    return direct_to_template(request, template_name, locals())
