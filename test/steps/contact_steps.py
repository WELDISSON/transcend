# coding: utf-8

from behave import *
from splinter import browser
from faker import Faker
import time

fake = Faker('pt_BR')

FACEBOOK = 'a[href="https://facebook.com/"]'
TWITTER = 'a[href="https://twitter.com/"]'
INSTAGRAM = 'a[href="https://instagram.com/"]'
BEHANCE = 'a[href="https://behance.com/"]'
DRIBBBLE = 'a[href="https://dribbble.com/"]'
EMAIL = '#mc-email'
SUBMIT = '#mc-form > input[type="submit"]:nth-child(2)'
MSG = '#mc-form > label'

@then(u'valido os links das redes sociais')
def step_impl(context):
    context.browser.find_by_css(FACEBOOK).visible
    context.browser.find_by_css(TWITTER).visible
    context.browser.find_by_css(INSTAGRAM).visible
    context.browser.find_by_css(BEHANCE).visible
    context.browser.find_by_css(DRIBBBLE).visible

@when(u'preencho o email')
def step_impl(context):
    email = fake.email()
    context.browser.find_by_css(EMAIL).fill(email)
    context.browser.find_by_css(SUBMIT).click()
    time.sleep(3)

@then(u'valido a mensagem de sucesso')
def step_impl(context):
    mensage = 'We have sent you a confirmation email'
    assert mensage in context.browser.find_by_css(MSG).value

@given(u'que eu esteja em Contact')
def step_impl(context):
    url = 'http://localhost:8000/#contact'
    context.browser.visit(url)

@when(u'preencho o email inválido')
def step_impl(context):
    email = 'teste@a.com'
    context.browser.find_by_css(EMAIL).fill(email)
    context.browser.find_by_css(SUBMIT).click()
    time.sleep(2)

@then(u'valido a mensagem de erro')
def step_impl(context):
    mensage = 'is an invalid email address and cannot be imported.'
    assert mensage in context.browser.find_by_css(MSG).value

    