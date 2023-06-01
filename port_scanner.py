import nmap

def scanPorts (first, last):
    # take the range of ports to 
    begin = first
    end = last
    scanner = nmap.PortScanner()
   
    for i in range(begin,end+1):
        dResult = scanner.scan(target,str(i))
        dResult = dResult['scan'][target]['tcp'][i]['state']
        print(f'port {i} is {dResult}.')



print ("PORT SCANNER USING PYTHON NMAP MODULE")
print("---------------------------------------------------------")
print()

target = input ("Enter target IP address: ")

print ("Choose 1 or 2:")
print ("1. Scan first 1000 ports")
print ("2. Scan all ports")

choice = int(input("choice: "))

if (choice == 1):
    print ("Scanning ports 1 to 1000...")
    scanPorts(0,999)
elif (choice == 2):
    print ("Scanning all ports: ")
    scanPorts(0,65535)
else:
    print ("Error - invalid option ")
    exit()
