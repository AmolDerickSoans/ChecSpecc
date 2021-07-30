import platform
import psutil
import json
import subprocess
import re
from subprocess import Popen, PIPE
from sqlite3.dbapi2 import Error

__author__ = "Amol Soans"

def get_size(bytes, suffix="B"):
                """
                Scale bytes to its proper format
                e.g:
                    1253656 => '1.20MB'
                    1253656678 => '1.17GB'
                """
                factor = 1024
                for unit in ["", "K", "M", "G", "T", "P"]:
                    if bytes < factor:
                        return f"{bytes:.2f}{unit}{suffix}"
                    bytes /= factor

def getRAM():
    cur_RAM = psutil.virtual_memory()
    cur_RAM = cur_RAM.total
    return get_size(cur_RAM)
        
def get_processor_name():
    try :
        if platform.system() == "Windows":
            proc = Popen(["wmic","cpu","get", "name"], stdout = PIPE)
            line = proc.stdout.readline()
            line2 = proc.stdout.readline()
            proc_name = f'{line2.rstrip()}'
            return proc_name[2:-1]
            
            
            
            """ root_winmgmts = GetObject("winmgmts:root\cimv2")
            cpus = root_winmgmts.ExecQuery("Select * from Win32_Processor")
            return cpus[0].Name
                   """
                
        ##needs changes
        elif platform.system() == "Darwin":

            return subprocess.run(['/usr/sbin/sysctl', "-n", "machdep.cpu.brand_string"]).strip()

        ##needs changes
        elif platform.system() == "Linux":

            command = "cat /proc/cpuinfo"

            return subprocess.run(command, shell=True).strip()

        else:
            return 0

    except Error as e:
        print(e)
        return e

def getSystemInfo():
    try :
        info = {}
        info['processor name'] = get_processor_name()
        info['processor stepping']=platform.processor()
        info['RAM'] = getRAM()
        info['platform']=platform.system()
        info['architecture']=platform.machine()
        info['version'] = platform.version()
        out_file = open("recc.json", "w") 
        return json.dump(info , out_file ,indent= 6)

    except Exception as e:
        print(e)
        return e


if __name__ == "__main__":
    
    getSystemInfo()
    
   
