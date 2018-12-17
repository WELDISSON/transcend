# coding: utf-8
from splinter import browser

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

class Home(object):
    def __init__(context, browser):
        context.browser = browser

    def open_page(context, url):
        context.browser.visit(url)
    
    def valid_logo(context):
        return context.browser.find_by_css(LOGO).visible

    def click_menu(context):
        context.browser.find_by_css(MENU).click()

    def valid_menu_home(context):
        context.browser.find_by_css(MENU_HOME)

    def valid_menu_about(context):
        context.browser.find_by_css(MENU_ABOUT)

    def valid_menu_services(context):
        context.browser.find_by_css(MENU_SERVICES)

    def valid_menu_works(context):
        context.browser.find_by_css(MENU_WORKS)
    
    def valid_menu_contact(context):
        context.browser.find_by_css(MENU_CONTACT)

    def click_about(context):
        context.browser.find_by_css(ABOUT).click()

    def click_services(context):
        context.browser.find_by_css(SERVICES).click()
    
    def click_contact(context):
        context.browser.find_by_css(CONTACT).click()

    def valid_page(context):
        return context.browser.url