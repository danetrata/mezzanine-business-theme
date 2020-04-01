========
Overview
========

Starter business theme for Mezzanine CMS.
Demo: http://demo.skyfalk.ru

Features:

- editable homepage
- sitewide content

Requirements:

- mezzanine >= 3.1


===========
Quick start
===========

0. pip install git+https://github.com/dfalk/mezzanine-business-theme.git
    echo git+https://github.com/dfalk/mezzanine-business-theme.git >> requirements.txt

1. Add "business_theme" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        'business_theme',
        ...
    )
    
2. Create database tables::
    python manage.py makemigrations business_theme

    python manage.py migrate
    
3. Add "SitewideContent" to your ADMIN_MENU_ORDER setting like this::

    ADMIN_MENU_ORDER = (
        ("Content", ("pages.Page", "blog.BlogPost",
        "generic.ThreadedComment", "business_theme.SitewideContent",
        ("Media Library", "fb_browse"),)),

4. Activate the editable home URLconf in your project urls.py::

    url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home"),

5. Visit /admin/ to add the HomePage content with slug "/".

6. Visit the admin menu Content -> Sitewide Content to edit sitewide blocks.


====
ToDo
====

- slider
- portfolio