# coding: utf-8

from behave import *
from splinter import browser
import time

LOGO = '#top > header > div > a > img'
MENU = '#top > header > a'
MENU_HOME = '#top > header > nav > div > ul.header-nav__list > li.current > a'
MENU_ABOUT = '#top > header > nav > div > ul.header-nav__list > li:nth-child(2) > a'
MENU_SERVICES = '#top > header > nav > div > ul.header-nav__list > li:nth-child(3) > a' 
MENU_WORKS = '#top > header > nav > div > ul.header-nav__list > li:nth-child(4) > a'
MENU_CONTACT = '#top > header > nav > div > ul.header-nav__list > li:nth-child(5) > a' 
ABOUT = '#home > ul.home-sidelinks > li:nth-child(1) > a'
SERVICES = '#home > ul.home-sidelinks > li:nth-child(2) > a'
CONTACT = '#home > ul.home-sidelinks > li:nth-child(3) > a'

@given(u'que eu esteja na home')
def step_impl(context):
    url = 'http://localhost:8000/'
    context.browser.visit(url)
    time.sleep(3)
    
@then(u'valido a logo do transcend')
def step_impl(context):
    assert True is context.browser.find_by_css(LOGO).visible

@when(u'clico no menu')
def step_impl(context):
    context.browser.find_by_css(MENU).click()

@then(u'valido os links dos menus')
def step_impl(context):
    context.browser.find_by_css(MENU_HOME)
    context.browser.find_by_css(MENU_ABOUT)
    context.browser.find_by_css(MENU_SERVICES)
    context.browser.find_by_css(MENU_WORKS)
    context.browser.find_by_css(MENU_CONTACT)

@when(u'clico em About')
def step_impl(context):
    context.browser.find_by_css(ABOUT).click()
    time.sleep(2)

@then(u'sou redirecionado para página de About')
def step_impl(context):
    assert '#about' in context.browser.url

@when(u'clico em Services')
def step_impl(context):
    context.browser.find_by_css(SERVICES).click()
    time.sleep(2)

@then(u'sou redirecionado para página de Services')
def step_impl(context):
    assert '#services' in context.browser.url

@when(u'clico em Contact')
def step_impl(context):
    context.browser.find_by_css(CONTACT).click()
    time.sleep(2)
    
@then(u'sou redirecionado para página de Contact')
def step_impl(context):
    assert '#contact' in context.browser.url