# coding: utf-8

from behave import *
from pages.home_page import *
import time

@given(u'que eu esteja na home')
def step_impl(context):
    context.home = Home(context.browser)

    url = 'http://localhost:8000/'
    context.home.open_page(url)
    time.sleep(2)
@then(u'valido a logo do transcend')
def step_impl(context):
    assert True is context.home.valid_logo()

@when(u'clico no menu')
def step_impl(context):
    context.home.click_menu()

@then(u'valido os links dos menus')
def step_impl(context):
    context.home.valid_menu_home()
    context.home.valid_menu_about()
    context.home.valid_menu_services()
    context.home.valid_menu_works()
    context.home.valid_menu_contact()

@when(u'clico em About')
def step_impl(context):
    context.home.click_about()
    time.sleep(2)

@then(u'sou redirecionado para página de About')
def step_impl(context):
    assert '#about' in context.home.valid_page()

@when(u'clico em Services')
def step_impl(context):
    context.home.click_services()
    time.sleep(2)

@then(u'sou redirecionado para página de Services')
def step_impl(context):
    assert '#services' in context.home.valid_page()

@when(u'clico em Contact')
def step_impl(context):
    context.home.click_contact()
    time.sleep(2)
    
@then(u'sou redirecionado para página de Contact')
def step_impl(context):
    assert '#contact' in context.home.valid_page()