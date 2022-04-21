import webbrowser, click, kvk
from pathlib import Path

@click.command(help='Argument: url, word(s) or keyword. To search multiple words, wrap them around with double quotes or put "\\" before each space\n\nVersion: 2.2.1')
@click.argument('argument', required=False)
@click.option('--set', '-s', help='Set keywords to access your links', required=False)
@click.option('--remove', '-r', help='Remove a keyword', required=False)
@click.option('--keywords', '-k', count=True ,default=True, help='Show all the saved keywords', required=False)
def search(argument, set, remove, keywords):
    path = Path(__file__).parent
    dataBase = kvk.KvK(f'{path}/dataBase.kvk')
    if set != None:
        try:
            var = dataBase.get(set)
        except:
            dataBase.addClass(set)
            dataBase.addAttr(className=set, attrName='link', attrContent=argument)
        else:
            if var != None:
                dataBase.editAttr(className=set, oldAttrName='link', newAttrName='link', attrContent=argument)
            else:
                dataBase.addClass(set)
                dataBase.addAttr(className=set, attrName='link', attrContent=argument)
    elif remove != None:
        try:
            var = dataBase.get(remove)
            print(var)
        except:
            pass
        else:
            if var != None:
                print('removing')
                dataBase.removeClass(remove)
    elif argument != None:
        try:
            var = dataBase.get(argument)
        except:
            pass
        else:
            if var != None:
                argument = dataBase.get('link', className=argument)
        try:
            argument.index('http://')
        except:
            try:
                argument.index('https://')
            except:
                argument = argument.replace(' ', '+')
                webbrowser.open(f'https://www.google.com/search?q={argument}')
            else:
                webbrowser.open(argument)
        else:
            webbrowser.open(argument)
    elif keywords:
        try:
            savedKeywords = dataBase.read()
        except:
            print('Now keyword saved yet')
        else:
            toPrint = 'Saved keywords:\n'
            for classCont in savedKeywords:
                for className in classCont:
                    for attr in classCont[className]:
                        link = (classCont[className])[attr]
                        toPrint += f'\t {className} -> {link}\n'
            print(toPrint)
