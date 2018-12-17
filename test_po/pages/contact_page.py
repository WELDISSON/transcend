# coding: utf-8
from splinter import browser


FACEBOOK = 'a[href="https://facebook.com/"]'
TWITTER = 'a[href="https://twitter.com/"]'
INSTAGRAM = 'a[href="https://instagram.com/"]'
BEHANCE = 'a[href="https://behance.com/"]'
DRIBBBLE = 'a[href="https://dribbble.com/"]'
EMAIL = '#mc-email'
SUBMIT = '#mc-form > input[type="submit"]:nth-child(2)'
MSG = '#mc-form > label'
class Contact(object):
    def __init__(context, browser):
        context.browser = browser
    
    def facebook_valid(context):
        context.browser.find_by_css(FACEBOOK).visible
    
    def twitter_valid(context):
        context.browser.find_by_css(TWITTER).visible
    
    def instagram_valid(context):
        context.browser.find_by_css(INSTAGRAM).visible
        
    def behance_valid(context):
        context.browser.find_by_css(BEHANCE).visible

    def dribbble_valid(context):
        context.browser.find_by_css(DRIBBBLE).visible

    def fill_email(context, value):
        context.browser.find_by_css(EMAIL).fill(value)

    def subscribe_click(context):
        context.browser.find_by_css(SUBMIT).click()

    def msg_return(context):
        return context.browser.find_by_css(MSG).value