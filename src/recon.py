# Reconnaissance module
import nmap

def run_recon(target):
    # Use Nmap to scan the network
    nm = nmap.PortScanner()
    nm.scan(target, '22-443')
    return nm.all_hosts()
