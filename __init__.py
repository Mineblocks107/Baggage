import webview
from Bhtml import *

def initWebpage():
    html = HTMLInit()
    return html

root = initWebpage()
root.addChildElement(HTMLElement("input"))

root.mainLoop()