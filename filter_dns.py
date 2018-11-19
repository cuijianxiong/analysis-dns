import subprocess
import os
import json
import tldextract


def sh(command, print_msg=True):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = []
    for line in iter(p.stdout.readline, b''):
        line = line.rstrip().decode('utf8')
        if print_msg:
            sline = line.replace('\t',' ').replace(' ',' ').split(' ')
            val = tldextract.extract(sline[-1])
            doma = (val.domain + "." + val.suffix).lower()
            if doma not in white_list:
                e.write(line+'\n')
            

if __name__ == '__main__':
    with open('white_domain.json','r') as f:
        white_list = json.load(f)
    with open("dns.log","a",errors="ignore") as e:
        command = "tshark -i eth2 -f 'port 53' -R 'dns.qry.type == 1 and dns.flags.response == 0' -n -T fields -e frame.time -e ip.src -e ip.dst -e dns.qry.name  2> error.log "
        sh(command=command)