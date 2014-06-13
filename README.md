Django Mptt Comments
====================

**Django Mptt Comments**  is a simple way to display threaded comments. It uses [django-mptt][mptt] to extend [django-contrib-comments][dcc] (*ex. django.contrib.comments*).

*This fork contains some quick fixes to make it work with the Django 1.6 (and maybe 1.7).*

Installation
------------

#### Get the required third party modules

    pip install django-mptt
    pip install django-template-utils
    pip install django-contrib-comments

#### Add the needed apps to INSTALLED_APPS

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

#### Configure your root urls.py

    url(r'^comments/', include('mptt_comments.urls')),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),

#### Set COMMENTS_APP variable in the settings.py

Add following to your settings.py:

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

`object` is any model object instance you want attach comments to. Usage is uqual to [django-contrib-comments][dcc] (*django.contrib.comments*).

**Django-mptt-comments** uses jQuery for AJAX, you may need to add it to your template.

**Django-mptt-comments** can use [django-notification][ntf] for notifying users about replies, friends posts e.t.c. (see [mptt_comments/management.py](mptt_comments/management.py) for notification types supported).


#### Pagination
You can also use pagination in toplevel tree by adding this settings:

    # Enable pagination (default: False)
    MPTT_COMMENTS_PAGINATION = True
    # Comments per page (default: 50)
    MPTT_COMMENTS_PAGINATION_PAGE_LENGTH = 30

#### Additional settings
`MPTT_COMMENTS_OFFSET`: Number of comments displayed before "read more" link appears. Default: 20.

`MPTT_COMMENTS_TOPLEVEL_OFFSET`: Default: 20.

`MPTT_COMMENTS_CUTOFF`: Depth of comments to be shown. Default: 3.

`MPTT_COMMENTS_COLLAPSE_ABOVE`: Default: 2.

`MPTT_COMMENTS_COLLAPSE_BELOW_DETAIL`: Default: True.

`MPTT_COMMENTS_SEND_NOTICES_FOR_NONPUBLIC`: Default: True.

[mptt]: http://django-mptt.github.io/django-mptt/ "Django mptt documentation"
[dcc]: http://django-contrib-comments.readthedocs.org/en/latest/ "Django comments documentation"
[ntf]: http://django-notification.readthedocs.org/en/latest/ "Django-notification documentation"