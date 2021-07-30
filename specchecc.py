import platform
import sqlite3
import psutil
import json
from sqlite3 import Error

class specchecc:

    
    

    def connection_handler(db_file):

        try:
            conn = sqlite3.connect(db_file)
            
            
        except Error as e:
           print(f" 🟥 error  :  {e}")

           return e

        

   

    def checkifexists(CPU_stepping):
        try:
        
            conn = sqlite3.connect("cpu_speedtraq.db")    
            cur = conn.cursor()
            cur.execute("SELECT rowid FROM cpu_table WHERE CPU_stepping = (?)" , (CPU_stepping,))
            data = cur.fetchall()

            if len(data) == 0:
                #print(f'There is no component named {CPU_stepping}')
                return False
            else:
                #print(f'Component {CPU_stepping} found with rowid {data[0]}')
                return True

            conn.commit()
            
            return cur.lastrowid
        except Error as e:
            print(f"🟥 error in check  :  {e}")

    
    def loadfromfile(file,component: int):

        with open(file , "r") as read_file:
           content =  json.load(read_file)
           if component == 1:
                processor = content["processor stepping"]
                processor = processor.split(',',1)[0]
                return processor
           elif component == 2:
               RAM = content["RAM"]
               return RAM
           
           else :
               print("please specify component")

    
    def compare():

        flag = 0
        resultString = []    
        resultString.append("------------------ 🦄 SPECCHECC ------------------\n")
        req_processor =  specchecc.loadfromfile("req.json" , 1)
        cur_processor = platform.processor()
        cur_processor = cur_processor.split(',',1)[0]
        
        conn = sqlite3.connect("cpu_speedtraq.db")
        cur = conn.cursor()
        cur.execute(''' SELECT bTotal_timeb_sec FROM cpu_table WHERE CPU_stepping = ? ''' , (req_processor,))
        
        row = cur.fetchone()
        req_time = row[0]
        
        if(specchecc.checkifexists(cur_processor) != False):
            cur.execute(''' SELECT bTotal_timeb_sec FROM cpu_table WHERE CPU_stepping = ? ''' , (cur_processor,))
            row = cur.fetchone()
            cur_time = row[0]
            
            if(cur_time <= req_time):
                resultString.append("🟢 CPU check passed❕ \n")
                flag = flag+ 1
            
            else:
                resultString.append(f"🟡 This CPU is not recomended to  run this  program (recommended : {req_processor}) \n⚠️  Performance may be affected! \n")


        else:
           resultString.append("⚠️ current processor doesnt exist in database, outcome uknown \n")
           resultString.append(f"Recommended processor is {req_processor} or aboveb \n")
           resultString.append("🟡 Performance may be affected! \n")
           




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



        req_RAM = specchecc.loadfromfile("req.json" , 2)

        cur_RAM = psutil.virtual_memory()

        cur_RAM = cur_RAM.total
     
        req_RAM = float(req_RAM.split('G',1)[0])

        cur_RAM = get_size(cur_RAM)

        cur_RAM = float(cur_RAM.split('G',1)[0])

        if cur_RAM >= req_RAM :

            resultString.append( "🟢 RAM check passed❕ \n")
            flag = flag + 1
        
        elif cur_RAM < req_RAM :

            resultString.append(f"⚠️  NOT ENOUGH RAM! (required:{req_RAM})\n")
            

        if(flag == 0 ):
            resultString.append("🔴 All Checks Failed! ☠️\n")
        
        elif(flag == 1):
            resultString.append("one Check Failed! \n")

        else:
            resultString.append("🟢 All Checks Passed 🤖\n")
                             
        resultString.append("__________________________________________________")
        print(''.join(map(str,resultString)))

        
        

if __name__ == "__main__":
  
    

    database = r"cpu_speedtraq.db"
    specchecc.connection_handler(database) 
    specchecc.compare()



