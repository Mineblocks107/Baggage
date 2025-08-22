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
    
    def __repr__(self):
        finalRetStr = ""
        finalRetStr += self.selector
        finalRetStr += "{\n"
        for k, v in self.declaration.items():
            finalRetStr += f"{k}: {v}; \n"
        finalRetStr += "}"
        return finalRetStr
    

f = CSSSelector("test")
f.addDeclaration(CSSDeclaration("test1", "test2"))

print(f)