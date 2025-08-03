class CSSDeclaration:
    def __init__(self, property, value):
        self.property = property
        self.value = value

class CSSSelector:
    def __init__(self, name: str):
        self.selector = name
        self.declaration = {}

    def addDeclaration(self, declaration: CSSDeclaration):
        self.declaration[declaration.property] = declaration.value