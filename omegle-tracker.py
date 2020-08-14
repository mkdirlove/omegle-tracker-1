from geolite2 import geolite2
import socket, subprocess 

cmd = r"C:\Program Files\Wireshark\tshark.exe"

process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
my_ip = socket.gethostbyname(socket.gethostname())
reader = geolite2.reader()

def get_ip_location(ip): # this function gets the ip address location as see down below
    location = reader.get(ip)
    
    try:
        country = location['country']['names']['en']
    except:
        country = 'Unknown'

    try:
        subdivision = location['subdivisions'][0]['names']['en']
    except:
        subdivision = 'Unknown'    

    try:
        city = location['city']['names']['en']
    except:
        city = 'Unknown'  

    try:
        postal = location['postal']
    except:
        postal = 'Unknown' 

    try:
        lock = location['location'] 
    except:
        lock = 'Unknown'
    
    return country, subdivision, city, postal, lock


for line in iter(process.stdout.readline, b""): # this for helps format the info 
    columns = str(line).split(" ")

    if "\\xe2\\x86\\x92" in columns and "UDP" in columns: # This if statement checks any udp connection tho you can change it to anything you like udp, tcp, ssh, ftp etc
        src_ip = columns[columns.index("\\xe2\\x86\\x92") - 1]

        if src_ip == my_ip:
            continue

        try:
            print(">>> " + src_ip, end="\t") 
            print(get_ip_location(src_ip)) 
        except:
            print("Not Found")