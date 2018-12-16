# coding: utf-8
from splinter import browser

LOGO = '#top > header > div > a > img'

class Home(object):
    def __init__(context, browser):
        context.browser = browser

    def open_page(context, url):
        context.browser.visit(url)
    
    def valid_logo(context):
        return context.browser.find_by_css(LOGO).visible