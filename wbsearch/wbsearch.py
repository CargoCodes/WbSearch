import webbrowser, click, KvK
from pathlib import Path

@click.command(help='Argument: url, word(s) or keyword. To search multiple words, wrap them around with double quotes or put "\\" before each space\n\nVersion: 2.1.3')
@click.argument('argument')
@click.option('--set', '-s', help='Set keywords to access your links', required=False)
@click.option('--remove', '-r', help='Remove a keyword', required=False)
def search(argument, set, remove):
    path = Path(__file__).parent
    dataBase = KvK.KvK(f'{path}/dataBase.kvk')
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
