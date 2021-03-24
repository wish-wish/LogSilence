#-*- coding:UTF-8 -*-
#coding=utf-8
#__author__ = 'cclin'
#write by cclin 2015.8.27

import sys
import os,os.path
#import re
import codecs
#import xml.dom.minidom as minidom
#import math
#from xml.etree import ElementTree as ET
#import json
#import xmltodict
#from PIL import Image
from subprocess import Popen,PIPE
import subprocess
import time

if __name__ == '__main__':
    reload(sys) 
    sys.setdefaultencoding( "utf-8" )
    ss=u"请关注全国留守儿童，请关注全国城乡差距，请关注全国教育现状......"
    print ss
    cmd = "TITLE "+ss
    os.system(cmd.encode('gb2312'))    
    print "author cclin 2015.04"
    print "support:e-mail=12092020@qq.com"
    print "copyright 2015~2018 for anyone to use"
    '''
    cmdcompile=os.path.split(os.path.realpath(__file__))[0]+r"/cocos2d/tools/cocos2d-console/bin/cocos.bat compile -p android -ap 10";
        
    #stdout=sys.stdout
    #sys.stdout=TextArea();
    os.system(cmdcompile)
    os.system("adb install-multiple -lr proj.android/bin/skydream-debug.apk");
    #os.system("pause")
    #os.system("dir")
    '''
    '''
    p=subprocess.Popen(cmdcompile,stdout=subprocess.PIPE,shell=False)
    #logs=p.communicate()
    #print logs;    
    while p.poll() == None:
        logline=p.stdout.readline()
        if logline.strip()!="":
            print logline,
        time.sleep(1)    
    print "ret code=",p.returncode
    '''

    #text_area,sys.stdout = sys.stdout,stdout
    #sys.stderr.write("abcd")
    #print text_area.buffer;
    #os.system("pause")
        
    #sys.stdout.write("please input:")
    #print sys.stdin.readline()
    
    #result,output=commands.getstatusoutput('"cocos2d/tools/cocos2d-console/bin/cocos.bat" compile -p android -ap 10')    
    #print(result)
    #print(output)
