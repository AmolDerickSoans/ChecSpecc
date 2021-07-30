import platform
import psutil
import json
import subprocess
import PyInquirer
import os
import distutils
from distutils import spawn
#import nvidia_smi
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

def getGPU():
    if platform.system() == "Windows":
        nvidia_smi = spawn.find_executable('nvidia-smi')
        if nvidia_smi is None:
            nvidia_smi = "%s\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe" % os.environ['systemdrive']
        
        else:
            nvidia_smi = "nvidia-smi"

        if(nvidia_smi == "nvidia-smi"):
            try:
            # p = Popen([nvidia_smi,"--query-gpu=index,uuid,utilization.gpu,memory.total,memory.used,memory.free,driver_version,name,gpu_serial,display_active,display_mode,temperature.gpu", "--format=csv,noheader,nounits"], stdout=PIPE)
                p = Popen([nvidia_smi,"--query-gpu=name", "--format=csv,noheader,nounits"], stdout=PIPE)
                stdout, stderror = p.communicate()

            except:
                return []

            output = stdout.decode('UTF-8')
            output = output.strip()
            return output
        
        else:
            return  "Using Intel or AMD card Cannot get info"
    
    else:
        return "Doesnt work in linux or darwin"
        


    
    



def getCPU_stepping():
    stepping = platform.processor()  
    stepping = stepping.split(',', 1)[0]
    return stepping
     



        
def getCPU():
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
    """ try :
        info = {}
        info['processor name'] = getCPU()
        info['processor stepping']=platform.processor()
        info['RAM'] = getRAM()
        info['platform']=platform.system()
        info['architecture']=platform.machine()
        info['version'] = platform.version()
        out_file = open("recc.json", "w") 
        return json.dump(info , out_file ,indent= 6)

    except Exception as e:
        print(e)
        return e """

        ##CLI for init


    

    style = PyInquirer.style_from_dict({
        PyInquirer.Token.QuestionMark: '#E91E63 bold',
        PyInquirer.Token.Selected: '#673AB7 bold',
        PyInquirer.Token.Instruction: '',  # default
        PyInquirer.Token.Answer: '#2196f3 bold',
        PyInquirer.Token.Question: '',
    })


    print("Setting Up Recomended Specifications File for  🦄  Specchecc : \n")

    questions = [
        {
            'type':'input',
            'name': 'CPU',
            'message': 'Recommended CPU',
            'default': getCPU()
        },

        {
            'type':'input',
            'name': 'CPU stepping',
            'message': 'CPU Stepping code',
            'default': getCPU_stepping()
        },
        {
            'type':'input',
            'name': 'RAM',
            'message': 'Recommended system RAM',
            'default': getRAM()
        },
        {
            'type':'input',
            'name': 'GPU',
            'message': 'Recommended GPU (Nvidia)',
            'default': getGPU(

            )
        },
        {
            'type':'input',
            'name': 'Comments',
            'message': 'Any Other Comments you want to add.',
            'default': 'These are the specs of the development machine '
        }
    ]

    answers = PyInquirer.prompt(questions, style=style)

    try :
        out_file = open("recc.json", "w") 
        json.dump(answers , out_file ,indent= 6)

    except Exception as e:
        print("🔺 error:{e}")



if __name__ == "__main__":
    getSystemInfo()

    
        
   
   
