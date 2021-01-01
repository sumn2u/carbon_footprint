'''
############################################################################
##                         GRETA REPOSITORY                               ##
############################################################################

repository name: Carbon_footprint
repository version: 1.0 
repository link: https://github.com/protea-earth/carbon_footprint
author: Jim Schwoebel 
author contact: jim@protea.earth
description: 
license category: opensource 
license: Apache 2.0 license 
organization name: Protea.earth 
location: Boston, MA
website: http://protea.earth 
release date: 2019-10-07

This code is hereby released under a Apache 2.0 license license. 

For more information, check out the license terms below. 

##############################################################################
##                            LICENSE TERMS                                 ##
##############################################################################

Copyright 2019 Protea.Earth

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 

##############################################################################
##                        CARBON_FOOTPRINT.PY                               ##
##############################################################################

Calculate your carbon footprint through answering a few questions on the command
prompt. 
'''

##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

import requests, time, random, webbrowser, datetime, platform, sys, pygame, shutil
import ftplib, getpass, os, json, pyaudio, wave, smtplib, random, socket
import speech_recognition as sr_audio
from bs4 import BeautifulSoup
import sys
import pyttsx3 as pyttsx
import os, re, matplotlib
from reportlab.pdfgen import canvas
from reportlab.lib import utils
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape, portrait
from reportlab.platypus import Image
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.patches import Shadow
import numpy as np
from textblob import TextBlob
from PyPDF2 import PdfFileMerger, PdfFileReader
import numpy as np 
from os.path import basename
import os.path
from reportlab.lib.units import inch
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE, formatdate
from email import encoders
import pandas as pd 


def get_date():
    return str(datetime.datetime.now())


def delete_pdfs():
    listdir=os.listdir()
    for i in range(len(listdir)):
        if listdir[i][-4:]=='.pdf':
            os.remove(listdir[i])
def cover_page(pdfname, name, carbon, date, sampleid):
    c=canvas.Canvas(pdfname, pagesize=portrait(letter))
    logo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'certificate.png')
    page_width, page_height = c._pagesize
    c.drawImage(logo,0,0, width=page_width, height=page_height)
    
    carbonAmount = carbon + 'Kg'
    c.setFont('Helvetica-Bold', 32, leading=None)
    
    c.setFillColor(HexColor('#355f4b'))
    # c.drawCentredString(300,460,"Carbon Footprint Report")
    # c.setFont('Helvetica', 16, leading=None)
    c.drawCentredString(250,400,"%s"%(name))
    c.setFillColor(HexColor('#f9f7eb'))
    c.setFont('Helvetica', 28, leading=None)
    c.drawCentredString(515,300,"%s"%(carbonAmount))

    # get .PNG from GDRIVE for text
    # c.drawImage('cover_text.png', 50,200,width=510,height=200,preserveAspectRatio=True)
    # wave looking thing on front page
    # c.drawImage('footer.png', -100,-35,width=800,height=100,preserveAspectRatio=True)
    c.save()

    return pdfname

def combine_pdfs():
    return ''


# FOR TESTING ONLY 


delete_pdfs()
firstName = sys.argv[1]
lastName = sys.argv[2]
carbon = sys.argv[3]
name= firstName + ' ' + lastName
filename='certificate.pdf'
cover_page(filename, name, carbon, str(datetime.datetime.now()), '100')
os.system('open %s'%(filename))