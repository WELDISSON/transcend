# coding: utf-8

from behave import *
from pages.home_page import *
from pages.contact_page import *
from faker import Faker
import time

fake = Faker('pt_BR')

@then(u'valido os links das redes sociais')
def step_impl(context):
    context.contact = Contact(context.browser)
    
    context.contact.facebook_valid()
    context.contact.twitter_valid()
    context.contact.instagram_valid()
    context.contact.behance_valid()
    context.contact.dribbble_valid()

@when(u'preencho o email')
def step_impl(context):
    context.contact = Contact(context.browser)
    
    email = fake.email()
    context.contact.fill_email(email)
    context.contact.subscribe_click()
    time.sleep(3)

@then(u'valido a mensagem de sucesso')
def step_impl(context):
    mensage = 'We have sent you a confirmation email'
    
    assert mensage in context.contact.msg_return()


@given(u'que eu esteja em Contact')
def step_impl(context):
    context.home = Home(context.browser)
    url = 'http://localhost:8000/#contact'
    context.home.open_page(url)

@when(u'preencho o email inválido')
def step_impl(context):
    context.contact = Contact(context.browser)

    context.contact.fill_email('teste@a.com')
    context.contact.subscribe_click()
    time.sleep(2)

@then(u'valido a mensagem de erro')
def step_impl(context):
    mensage = 'is an invalid email address and cannot be imported.'
    assert mensage in context.contact.msg_return()

    