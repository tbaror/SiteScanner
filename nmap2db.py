import json
import xmltodict
import datetime
import argparse
import os


f = open("nmap_output.xml")
xml_content = f.read()
f.close()
#print(json.dumps(xmltodict.parse(xml_content), indent=4, sort_keys=True))
f = open("demofile3.txt", "w")
f.write(json.dumps(xmltodict.parse(xml_content), indent=4, sort_keys=True))
f.close()

nmap_results = xmltodict.parse(xml_content)


def get_scandetails():
    dt = datetime.datetime.now()
    scan_date = str(dt.year) + '_' + str(dt.month) + '_' + str(dt.day) + '_' + str(dt.hour) + '_' + str(dt.minute) + '_' + str(dt.second)
        
    site_name='"Gefen IL"'
    scan_name = 'Gefen'+ '_' + scan_date
    location_name = '"Gefen Dekel Israel,BeerSheba"'
    lon = "31.263414931238763"
    lat = "34.81140918899447"
    site_ip_range1 = '212.143.237.0/24'
    scan_time_start = nmap_results["nmaprun"]['@start']
    scan_timestr_start = nmap_results["nmaprun"]['@startstr']
    scan_args = nmap_results["nmaprun"]['@args']
    nmap_version = nmap_results["nmaprun"]['@version']
    scan_time_end = nmap_results["nmaprun"]['runstats']['finished']['@time']
    scan_timestr_end = nmap_results["nmaprun"]['runstats']['finished']['@timestr']
    scan_elapsed = nmap_results["nmaprun"]['runstats']['finished']['@elapsed']
    scan_args = scan_args.replace('"','')
    scan_args = scan_args.replace('\\','')
    print(scan_args)
    argset="--scan_name="+ scan_name + " --site_name="+site_name +  " --location_name="+location_name+ \
        " --lon="+lon+" --lat="+lat+" --site_ip_range1="+site_ip_range1+" --scan_time_start="+scan_time_start+ \
        " --scan_timestr_start="+'"'+scan_timestr_start+'"'+" --scan_time_end="+scan_time_end+" --scan_timestr_end="+'"'+scan_timestr_end+'"'+ \
        " --scan_elapsed="+scan_elapsed+" --scan_args="+'"'+scan_args+'"'+" --nmap_version="+nmap_version
    print(argset)
    os.system("python manage.py reportingest "+argset)
         
   

        




def get_address(c):
    addlen = (len(nmap_results["nmaprun"]["host"][c]['address']))
    print(addlen)
    for ad in range(addlen):
        if '@addr' in nmap_results['nmaprun']['host'][c]['address'][ad]:
            print( nmap_results['nmaprun']['host'][c]['address'][ad]['@addr']) 
            print(nmap_results['nmaprun']['host'][c]['address'][ad]['@addrtype'])
            if '@vendor' in nmap_results['nmaprun']['host'][c]['address'][ad]:
                print(nmap_results['nmaprun']['host'][c]['address'][ad]['@vendor'])
    

def get_hostname(c):
    
        if nmap_results['nmaprun']['host'][c]['hostnames']:
            print(nmap_results['nmaprun']['host'][c]['hostnames']['hostname']['@name'])
        else:
            print(c,'null')


def get_osdetection(c):
    
        if 'osfingerprint' in nmap_results['nmaprun']['host'][c]['os']:
            print(nmap_results['nmaprun']['host'][c]['os']['osfingerprint']['@fingerprint'])
        else:
            print(c,'null')
        oslen = (len(nmap_results['nmaprun']['host'][c]['os']['osmatch']))
        if oslen > 4:
            print('long:', oslen)
        
            for ostype in range(oslen):
                print('counter:',ostype)
                
                if '@accuracy' in nmap_results['nmaprun']['host'][c]['os']['osmatch'][ostype]:
                    print(nmap_results['nmaprun']['host'][c]['os']['osmatch'][ostype]['@accuracy'])
        else:
            print(nmap_results['nmaprun']['host'][c]['os']['osmatch']['@name'])
            print('null')    
            
def get_ports(c):
    ports_container = nmap_results['nmaprun']['host'][c]['ports']
    if 'port' in ports_container:
        portlen =  len(ports_container['port'])
        print(portlen)
        if portlen > 1:
            for port in range(portlen):
                if 'service' in ports_container['port'][port]:

                    if '@portid' in ports_container['port'][port] and '@product' in ports_container['port'][port]['service']:
                        pass
                        #print(ports_container['port'][port]['@portid'],ports_container['port'][port]['service']['@product'])

                if 'script' in ports_container['port'][port]:
                    if '@id' in ports_container['port'][port]['script'] and ports_container['port'][port]['script']['@id'] == 'vulners':
                        #print(ports_container['port'][port]['script']['@output'])
                        script_len = len(ports_container['port'][port]['script']['table']['table'])
                        print('script lenght', script_len)
                        
                    
                        for scr in range(script_len):
                            if 'elem' in ports_container['port'][port]['script']['table']['table'][scr]:
                                
                                elem_len = len(ports_container['port'][port]['script']['table']['table'][scr]['elem'])
                                element_base = ports_container['port'][port]['script']['table']['table'][scr]['elem']
                                for el in range(elem_len):
                                    if el == 0:
                                        print('CVSS Score:',element_base[el]['#text'])
                                    elif el == 1:
                                        if element_base[el]['#text'] == 'true':
                                            print('exploit type')
                                        elif element_base[el]['#text'] == 'false':
                                            print('vunerability type')
                                    elif el == 2:
                                        print('cve id:',element_base[el]['#text'])
                                        print('')

                                    elif el == 3:
                                        print('db type:', element_base[el]['#text'])     
                    elif '@id' in ports_container['port'][port]['script'] and ports_container['port'][port]['script']['@id'] != 'vulners':
                        print(ports_container['port'][port]['script']['@id'])
                        print(ports_container['port'][port]['script']['@output'])
                        




                        
                        
                        
                          





length = (len(nmap_results["nmaprun"]["host"]))


for x in range(length):
   # get_address(x)
    #get_hostname(x)
    #get_osdetection(x)
    #get_ports(x)
    pass
    
get_scandetails()



    