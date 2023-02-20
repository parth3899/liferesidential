# -*- coding: utf-8 -*- 
from __future__ import absolute_import, print_function, unicode_literals

from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views import static

from website.apps.area.sitemaps import AreaSitemap, AreaStaticSitemap
from website.apps.company.sitemaps import BranchSitemap
from website.apps.development.sitemaps import DevelopmentSitemap, DevelopmentStaticSitemap
# from djangocms_page_sitemap.sitemap import ExtendedSitemap
from website.apps.generic.sitemaps import MyExtendedSitemap
from website.apps.generic.views import manifest
from website.apps.news.sitemaps import NewsSitemap, ArticlesPaginationSitemap
from website.apps.property.sitemaps import PropertySitemap, PropertyStaticSitemap
from website.apps.quiz.sitemaps import QuizSitemap
from website.apps.testimonial.sitemaps import TestimonialSitemap
from django.conf.urls import static
from django.conf.urls.static import static as statics
admin.autodiscover()

urlpatterns = i18n_patterns(
    re_path(r'^admin/', admin.site.urls),
    path('manifest.json', manifest),
    re_path('', include('pwa.urls')),
    # site maps
    path('sitemap.xml/', sitemap,
         {'sitemaps': {
             'cmspages': MyExtendedSitemap,
             'area': AreaSitemap,
             'areastatic': AreaStaticSitemap,
             'development': DevelopmentSitemap,
             'developmentstatic': DevelopmentStaticSitemap,
             'branches': BranchSitemap,
             'news': NewsSitemap,
             'newspagination': ArticlesPaginationSitemap,
             'property': PropertySitemap,
             'propertystatic': PropertyStaticSitemap,
             'testimonial': TestimonialSitemap,
             'quiz': QuizSitemap,
         }
         }, name='django.contrib.sitemaps.views.sitemap'),

    path('select2/', include('django_select2.urls')),
    path('forms/', include('website.apps.forms.urls')),
    path('robots.txt/', include('robots.urls')),
    path('o/', include('oauth2_provider.urls')),

    re_path(r'^', include('cms.urls')),

    # remove default language code from url
    prefix_default_language=False
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
                      path('media/<path>', static.serve,
                           {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                  ] + staticfiles_urlpatterns() + urlpatterns

    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns = [
        path('media/<path>)', static.serve, {'document_root': settings.MEDIA_ROOT}),
        # other paths
    ] + urlpatterns + statics(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)