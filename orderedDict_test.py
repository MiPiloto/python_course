from collections import OrderedDict

glossary = OrderedDict()


glossary["python"] = "an easy and powerful language!"
glossary["unity"] = "good for games!"
glossary["java"] = "old and reliable language."
glossary["ruby"] = "useful for mobile development!"
glossary["javascript/React"] = "fabulous language and framework, in high ascension!"
glossary["swift"] = "used in IOS development!"


for name,language in glossary.items():
    print(name + language)