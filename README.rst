=====
Ninfo
=====


Quick start
-----------

1. Add "django_ninfo" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'django_ninfo',
      )

2. Include the polls URLconf in your project urls.py like this::

      url(r'^ninfo/', include('django_ninfo.urls')),

3. Run `python manage.py syncdb` to create the ninfo table models.
