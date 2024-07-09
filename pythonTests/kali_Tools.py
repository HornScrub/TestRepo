import os
import nmap

''' NMap (Network Mapper): A powerful network scanning tool used for network discovery and security auditing. 
    It can identify live hosts on a network, open ports, services running on those ports, and their versions, among other things.
    
    PortScanner class: This class in the nmap module provides a way to interact with NMap using Python. 
    It allows you to perform scans and access the results programmatically.'''

class NMapTools:

    ### FUNCTIONS ###

    ### getOpenPorts(getOpenPorts(subdomain_list : list[str]) -> dict)

    ''' This function returns a dictionary of given subdomains and their relative open ports. 
        INPUT:
            subdomain_list - a list containing subdomains represented as strings
        OUTPUT: 
            nmap_dict - a dictionary containing the input subdomains as keys and their open ports as values stored in a list'''
          
    def getOpenPorts(subdomain_list : list[str]) -> dict:
        
        #initialize the NMap scanner
        nm = nmap.PortScanner()

        #initalize the outer directory to hold subdomains and their hosts
        nmap_dict = {}

        print(nmap_dict.keys())
        
        #iterate over each subdomain for scan
        for subdomain in subdomain_list:

            print(f"Scanning: {subdomain}")
            
            # scan the subdomain with NMap. Scan results are stored within the Nmap object.
            # if the scan is sucessful, it will add the subdomain as a key.
            if nm.scan(subdomain, arguments = '-Pn'):

                nmap_dict[subdomain] = {}

                # create values for the outer directory/keys for the inner directory
                for host in nm.all_hosts():
                    nmap_dict[subdomain][host] = []

                # iterate over each host in the scan results
                for host in nm.all_hosts():
                    
                    # initialize the list of open ports for this subdomain
                    open_ports = []

                    #check for open ports in the scan results

                    # 'all_protocols()' returns a list of all protocols scanned (ex. TCP, UDP)
                    for proto in nm[host].all_protocols():

                        # 'keys()' returns a list of all ports scanned.
                        port_list = nm[host][proto].keys()
                        for port in port_list:

                            # 'state' attribute of a port shows whether it is open or closed.
                            # if a port is open, add it to the list of open ports for this subdomain.

                            # nMap object has:
                            #   a dictionary of subdomains
                            #   the subdomain dictionary has:
                            #       a dictionary of protocols scanned by nMap
                            #       'tcp' and 'udp' are the keys for the 'all_protocols()' function.
                            #       the protocol dictionary has:
                            #           a dictionary of ports scanned by nMap
                            #           'keys()' returns a list of all ports scanned.
                            #           the port dictionary has:
                            #               a 'state' attribute indicating whether the port is open or closed
                            #               'open' indicates that the port is open.

                            # 'nm[subdomain][proto][port]['state']' accesses the state of the port (open or closed) from the Nmap object

                            if nm[host][proto][port]['state'] == 'open':

                                # if a port is open, add it to the list of open ports for this subdomain.
                                open_ports.append(port)

                    nmap_dict[subdomain][host] = open_ports 

        return nmap_dict
    
class FileTools:

    ### FUNCTIONS ###

    ### writeDictionaryToTextFile(aDict : dict) -> bool)

    ''' This function creates the contents of a nested dictionary to a text file in a legible way.
        The function expects { str : { str : [int] } }
        INPUT:
            aDict - a nested dictionary
            textFileName - a string representing the name of the text file to be created
        OUTPUT:
            Bool value reflecting whether the file was opened and written to sucessfully.'''
    
    def writeDictionaryToTextFile(aDict : dict, textFileName : str) -> bool:

        # Open the file for writing. Creates a file if it doesn't exist.
        try:
            with open(textFileName, 'w') as file:
                for subdomain, host_info_dict in aDict.items():
                    file.write(f"Subdomain: {subdomain}\n")
                    for ip, port_list in host_info_dict.items():
                        file.write(f"\tHost(s): {ip}\n")
                        file.write(f"\t\tPorts: {', '.join(map(str, port_list))}\n")
                    file.write("\n")
            print(f"Data written to {textFileName} successfully.")
            return True
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
            return False
                        
