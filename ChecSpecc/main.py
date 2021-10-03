import sys

from ChecSpecc.specchecc import compare , connection_handler
from ChecSpecc.makeFile import  getSystemInfo



available_commands = {
    'init':{
        'name':'init',
        'help':"Welcome to specchecc , with the init command you can make a recc.json file holding all \n the required specifications"
    }
}

def checkspec(argv : list = None):
    if argv is None:
        argv = sys.argv[1:]

    if not len(argv) or argv[0] not in available_commands.keys():
        print('Available commands: ')
        for key, val in available_commands.items():
            print('-> {}: {}'.format(
                key, val['help']
            ))
        print('\n')
        return
    
    task_name = argv[0]

    if task_name == available_commands['init']['name']:
        getSystemInfo()


if __name__ == '__main__':
    checkspec(sys.argv[1:])

    connection_handler("cpu_speedtraq.db")
    compare()