import argparse
import requests
import pycurl
from daemonize import Daemonize
from time import sleep

status = requests.get('http://ukr.net/') 
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--foreground",  action="store_true")
args = parser.parse_args()

def getstatus():
    return status
def getUserData():
    c = pycurl.Curl()
    c.setopt(pycurl.URL, 'https://ukr.net')
    c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
    c.setopt(pycurl.USERPWD, 'username:userpass')
    c.perform()
        
if __name__ == "__main__":
    if args.foreground:
        pid = "/tmp/test.pid"
        daemon = Daemonize(app="client_Daemon", pid=pid, action=getUserData)
        daemon.start();
            
    else:
        getUserData()
