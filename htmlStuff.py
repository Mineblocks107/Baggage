import uuid
import webview

class HTMLAttribute:
    def __init__(self, attributeName, attributeValue = None):
        self.attributeName = attributeName
        self.attributeValue = attributeValue

class HTMLElement:
    def __init__(self, name: str):
        self.name: str = name
        self.child: dict[HTMLElement, HTMLPlainText] = {}
        self.attributes: dict = {}
        self.id = str(uuid.uuid4())
    
    def addChildElement(self, element):
        self.child[element.id] = element

    def addAttribute(self, attribute: HTMLAttribute):
        self.attributes[attribute.attributeName] = attribute.attributeValue

    def __repr__(self):
        attributes = self.getAttributes()
        reprString = f'<{self.name}'
        if attributes != '':
            reprString += f' {attributes}'
        reprString += '>'
        for k, v in self.child.items():
            reprString += str(v)
        reprString += f'</{self.name}>'
        return reprString

    def getAttributes(self):
        attrStr = ''
        for k, v in self.attributes.items():
            attrStr += ''.join(k)
            if v:
                attrStr += ''.join(['="', v, '"'])
        return attrStr

class HTMLPlainText:
    def __init__(self, text: str):
        self.text = text
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return f'{self.text}'

class HTMLInit(HTMLElement):
    def __init__(self):
        super().__init__("html")

class HTMLInputText(HTMLElement):
    def __init__(self):
        super().__init__("input")
        self.addAttribute(HTMLAttribute("type", "text"))


def initWebpage(titleName: str):
    html = HTMLInit()
    return html

root = initWebpage("Html")
root.addChildElement(HTMLInputText())

open("test.html", "w").write(str(root))
webview.create_window('', 'test.html')
webview.start()