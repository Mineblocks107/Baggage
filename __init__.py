import webview
from htmlStuff import *

def initWebpage():
    html = HTMLInit()
    return html

def mainLoop():
    webview.create_window('', "test.html")
    webview.start()

root = initWebpage()

