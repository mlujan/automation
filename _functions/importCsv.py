# -*- coding: utf-8 -*-
import csv
import os
from sst.actions import *
from sst import runtests



def loadmain(fileName):
    with open(fileName, 'rb') as f:
        reader = csv.reader(f)
        for line in reader:
           for each in line:
                if each =='go':
                    go(line)
                elif each == 'fill':
                    fill(line)
                elif each == 'clickid':
                    clickid(line)
                elif each == 'clickname':
                    clickname(line)
                elif each == 'fill':
                    fill(line)
		elif each == 'dropdown':
		    dropdown(line)
		elif each == 'radio':
		    radio(line)
		elif each == 'clickclass':
		    clickclass(line)
def go(line):
    print "++Function GO"
    line.pop(0)
    for each in line:
        go_to(each)
def clickid(line):
    line.pop(0)
    for each in line:
        click_element(each)
def clickname(line):
    line.pop(0)
    for each in line:
        name = get_element(name=each)
        click_element(name)
def fill(line):
    line.pop(0)
    name = get_element(name=line[0])
    write_textfield(name,line[1])
def dropdown(line):
    line.pop(0)
    name = get_element(name=line[0])
    set_dropdown_value(name,line[1])
def radio(line):
    line.pop(0)
    set_radio_value(line[0])
def clickclass(line):
    line.pop(0)
    for each in line:
        name = get_element(css_class=each)
        click_element(name)
	sleep(10)

