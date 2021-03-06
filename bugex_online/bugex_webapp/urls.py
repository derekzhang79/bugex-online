# -*- coding: utf-8 -*-

"""
Project: BugEx Online
Authors: Amir Baradaran
         Tim Krones
         Frederik Leonhardt
         Christos Monogios
         Akmal Qodirov
         Iliana Simova
         Peter Stahl
"""

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from bugex_webapp.views import provide_user_content, process_main_page_forms
from bugex_webapp.views import submit_contact_form, log_user_out, show_bugex_result
from bugex_webapp.views import delete_bugex_result, get_source_file_content

urlpatterns = patterns('',
    url(r'^$', process_main_page_forms, name='main-page'),
    url(r'^howto/$',
        TemplateView.as_view(template_name='bugex_webapp/howto.html'),
        name='howto-page'
    ),
    url(r'^contact/$', submit_contact_form, name='contact-page'),

    url(r'^result/(?P<token>[a-z0-9\-]{36})$', show_bugex_result,
        name='results-page'),
    url(r'^delete/(?P<delete_token>[a-z0-9\-]{36})$', delete_bugex_result,
        name='delete-page'),

    url(r'^account/$', provide_user_content, name='user-page'),
    url(r'^account/logout/$', log_user_out, name='logout'),

    url(r'^source/(?P<token>[a-z0-9\-]{36})/'
        r'(?P<class_name>([a-z0-9]+\.)+[A-Z][A-Za-z0-9]+)$',
        get_source_file_content,
        name='source-page'),

)
