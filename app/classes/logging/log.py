import app.classes.colours.codes01 as colour

threading = f"{colour.CBLUE2}[Threading   ]{colour.CEND}: "
pc = f"{colour.CVIOLET}[Post creation   ]{colour.CEND}: "
ui = f"{colour.CVIOLET2}[UI   ]{colour.CEND}: "
csh = f"{colour.CGREEN}[C-SHandler   ]{colour.CEND}: "


def log(file, header, content):
    print(f"{colour.CYELLOW}[{str(file)}]:{colour.CEND}"
          f"{str(header)}"
          f"{colour.CBEIGE2}{str(content)}{colour.CEND}")
