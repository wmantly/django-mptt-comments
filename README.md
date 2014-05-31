Django Mptt Comments
====================

**Django Mptt Comments**  is a simple way to display threaded comments. It uses [django-mptt][mptt] to extend [django-contrib-comments][dcc] (*ex. django.contrib.comments).

*This fork contains some quick fixes to make it work with the Django 1.6 (and maybe 1.7).*

Installation
------------

#### Get the required third party modules

    pip install django-mptt
    pip install django-template-utils
    pip install django-contrib-comments

#### Add the needed apps to `INSTALLED_APPS

    'django_comments',
    'template_utils',
    'mptt',
    'mptt_comments'

#### You may also need to configure MIDDLEWARE_CLASSES

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

#### Congigure Your root urls.py

    url(r'^comments/', include('mptt_comments.urls')),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),

#### Set COMMENTS_APP variable in the settings.py

Add following to Your settings.py:

    COMMENTS_APP = 'mptt_comments'

#### Add the required code to the objects detail page (see Usage)

#### Copy the templates to adapt them for your site

#### Style the forms using css

Example usage
-------------

To display the toplevel tree in templates:

    {% load mptt_comments_tags %}
    
    {% block extrahead %}
    {% include "comments/comments_media.html" %}
    {% endblock extrahead %}
    
    {% block content %}
    
    {% if object %}
      {% display_comment_toplevel_for object %}
    {% endif %}
    
    {% endblock content %}

`object` is any model object instance You want attach comments to. Usage is uqual to [django-contrib-comments][dcc] (*django.contrib.comments*).
.
[mptt]: http://django-mptt.github.io/django-mptt/ "Django mptt documentation"
[dcc]: http://django-contrib-comments.readthedocs.org/en/latest/ "Django comments documentation"
