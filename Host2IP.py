import argparse
import socket
import pandas as pd

print("""

 __    __                        __       ______   ______  _______  
/  |  /  |                      /  |     /      \ /      |/       \ 
$$ |  $$ |  ______    _______  _$$ |_   /$$$$$$  |$$$$$$/ $$$$$$$  |
$$ |__$$ | /      \  /       |/ $$   |  $$____$$ |  $$ |  $$ |__$$ |
$$    $$ |/$$$$$$  |/$$$$$$$/ $$$$$$/    /    $$/   $$ |  $$    $$/ 
$$$$$$$$ |$$ |  $$ |$$      \   $$ | __ /$$$$$$/    $$ |  $$$$$$$/  
$$ |  $$ |$$ \__$$ | $$$$$$  |  $$ |/  |$$ |_____  _$$ |_ $$ |      
$$ |  $$ |$$    $$/ /     $$/   $$  $$/ $$       |/ $$   |$$ |      
$$/   $$/  $$$$$$/  $$$$$$$/     $$$$/  $$$$$$$$/ $$$$$$/ $$/       
                                                                    
                                                                    
                                                    0xsu3ks

""")

def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror as e:
        return f"Unable to resolve hostname. Error: {e}"

# Argument parser
parser = argparse.ArgumentParser(description='Resolve hostnames to IP addresses.')
parser.add_argument('--file', required=True, help='File containing hostnames, one per line.')
parser.add_argument('--output', required=False, help='Output Excel file.')

args = parser.parse_args()

# Read hostnames from a file
with open(args.file, 'r') as file:
    hostnames = file.read().splitlines()

# Dataframe for storing results
df = pd.DataFrame(columns=["Hostname", "IP Address"])

# Resolve each hostname and store in dataframe
for hostname in hostnames:
    ip = resolve_hostname(hostname)
    df = df.append({"Hostname": hostname, "IP Address": ip}, ignore_index=True)

# Write dataframe to Excel file
if args.output:
    df.to_excel(args.output, index=False)
