import httplib
import urllib
import conf
import requests
import os

##Module for communicating to the slaves.
##Wraps long HTTPRequests

def send_encoder_steps(to_ip, steps, ratio):
    '''
        This will let the main RPi module know
        that it is ready for the next motor
        instruction.
    '''
    headers = {"Content-type": "application/json"}
    status = {
        'from': conf.IP[conf.MODE],
        'encoder_steps': steps,
        'turn_ratio': ratio,
    }
    print(status)
    requests.post("http://{0}:5830/".format(to_ip), data=status)
    print("INSTRUCTION received by MOTOR at " + to_ip)

def test_connection(to_ip):
    try:
        '''
            This is to test the connection with the RPI center
            module
        '''
        status  = urllib.urlencode({'from': conf.IP[conf.MODE]})
        conn = httplib.HTTPConnection(to_ip, port=5000);
        conn.request("POST", "/test", status)
        content = conn.getresponse()
        conn.close()
        return True
    except:
        return False
        print("not reached")
