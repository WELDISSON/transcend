# coding: utf-8

from behave import *
from pages.home_page import *

@given(u'que eu esteja na home')
def step_impl(context):
    context.home = Home(context.browser)

    url = 'http://localhost:8000/'
    context.home.open_page(url)

@then(u'valido a logo do transcend')
def step_impl(context):
    assert True is context.home.valid_logo()

@when(u'clico no menu')
def step_impl(context):
    assert False

@then(u'valido os links dos menus')
def step_impl(context):
    assert False