#!/usr/bin/env python
# coding: utf-8

from behave import *
from splinter import Browser
 
def before_all(context):
    
    context.browser = Browser('chrome')

def after_scenario(context, scenario):
    context.browser.cookies.delete()

    for step in scenario.steps:
        if step.status == 'failed':
            scenario_name = scenario.name
            context.browser.driver.save_screenshot('test/erro.png')
            
def after_all(context):
    context.browser.quit()