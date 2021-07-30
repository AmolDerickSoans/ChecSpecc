import sys

from specchecc import compare , connection_handler
from makeFile import  getSystemInfo



available_commands = {
    'init':{
        'name':'init',
        'help':"Welcome to specchecc , with the init command you can make a recc.json file holding all \n the required specifications"
    }
}

def main(argv):
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
    main(sys.argv[1:])

    connection_handler("cpu_speedtraq.db")
    compare()