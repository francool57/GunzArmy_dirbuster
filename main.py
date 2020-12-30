#!/usr/bin/python
import requests
import argparse
import sys
import multiprocessing as mp
import psutil

if sys.version_info.major == 2:
    print('Python3 required!')
    exit()

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", dest="url", help="Define Url")
parser.add_argument("-w", "--wordlist", dest="wordlist", help="Define wordlist")
parser.add_argument("-x", "--extencion", dest="extencion", help="Define extencion")
#parser.add_argument("-h", "--help", dest="help")
args = parser.parse_args()

parser.print_help()

def main(): 


    if len(sys.argv) == 0 or len(sys.argv) == 1 or len(sys.argv) == 2: #or not str(sys.argv).find("-u", "-w"):
        parser.print_help()
        exit()
    else: pass

    print('\n----------------------------------------------------------------')
    print(f' Url: {args.url}')
    print(f' Wordlist: {args.wordlist}')
    print('----------------------------------------------------------------\n')

    file = open(args.wordlist, 'r') 
    count = 0
    CT = 0
    ct_tm = int(0)
    for line in file: 
        count += 1
        ct_tm += 1
        CT += 1
        if ct_tm == 1000:
            ct_tm = 0
            print(f'Tested: {CT}')

        global ul
        global ula
        if not str(args.url).endswith('/') and str(args.url).startswith("http://") or str(args.url).startswith('https://') and str(args._get_kwargs()) != str(args._get_kwargs()).startswith('[(\'extencion\', None)'):
            ul = args.url + '/' +  line.strip()
            aa = str(args.extencion).split(',')
            if count == len(str(args.extencion).split(',')):
                count = 0
            else:pass
            
            ula = args.url + '/' + line.strip() + '.' + aa[count]
            code = requests.get(ul)
            code1 = requests.get(ula)
            if code.status_code == 201 or code.status_code == 301:
                print(f"{ul} ==> {code.status_code}")
            else: pass 
            if code1.status_code == 201 or code1.status_code == 301:
                print(f"{ula} ==> {code1.status_code}")
            else: pass
            continue
        elif not str(args.url).endswith('/') and str(args.url).startswith("http://") or str(args.url).startswith('https://'):
            ul = args.url + '/' +  line.strip()
        elif str(args.url).endswith('/') and not str(args._get_kwargs()).startswith('[(\'extencion\', None)') and str(args.url).startswith("http://") or str(args.url).startswith('https://'):
            ul = args.url + line.strip()
            aa = str(args.extencion).split(',')
            if count == len(str(args.extencion).split(',')):
                count = 0
            else:pass
            ula = args.url + line.strip() + '.' + aa[count]
            code = requests.get(ul)
            code1 = requests.get(ula)
            if code.status_code == 201 or code.status_code == 301:
                print(f"{ul} ==> {code.status_code}")
            else: pass
            if code1.status_code == 201 or code1.status_code == 301:
                print(f"{ula} ==> {code1.status_code}")
            else: pass
            continue
        elif str(args.url).endswith('/') and str(args.url).startswith("http://") or str(args.url).startswith('https://'):
            ul = args.url + line.strip()
        elif not str(args.url).endswith('/') and not str(args.url).startswith("http://") or not str(args.url).startswith('https://'):
            ul = 'http://' + args.url + '/' + line.strip()
        elif not str(args._get_kwargs()).startswith('[(\'extencion\', None)') and not str(args.url).endswith('/') and not str(args.url).startswith("http://") or not str(args.url).startswith('https://'):
            ul = 'http://' + args.url + '/' + line.strip()
            print(1)
            aa = str(args.extencion).split(',')
            if count == len(str(args.extencion).split(',')):
                count = 0
            else:pass
            ula = 'http://' + args.url + '/' +line.strip() + '.' + aa[count]
            code = requests.get(ul)
            code1 = requests.get(ula)
            if code.status_code == 201 or code.status_code == 301:
                print(f"{ul} ==> {code.status_code}")
            else: pass
            if code1.status_code == 201 or code1.status_code == 301:
                print(f"{ula} ==> {code1.status_code}")
            else: pass
            continue
        code = requests.get(ul)
        if code.status_code == 201 or code.status_code == 301 or code.status_code == 201 or code.status_code == 300 or code.status_code == 202:
            print(f"{ul} ==> {code.status_code}")
        else: pass
        import time

    print('----------------------------FINISHED----------------------------')

def spawn():
    procs = list()
    n_cpus = psutil.cpu_count()
    for cpu in range(n_cpus):
        affinity = [cpu]
        d = dict(affinity=affinity)
        p = mp.Process(target=run_child, kwargs=d)
        p.start()
        procs.append(p)
    for p in procs:
        p.join()
        #print('joined')

def run_child(affinity):
    proc = psutil.Process()  # get self pid
    #print('PID: {pid}'.format(pid=proc.pid))
    aff = proc.cpu_affinity()
    #print('Affinity before: {aff}'.format(aff=aff))
    proc.cpu_affinity(affinity)
    aff = proc.cpu_affinity()
    #print('Affinity after: {aff}'.format(aff=aff))


if __name__ == '__main__':
    spawn()
    try:
        main()
    except KeyboardInterrupt:
        print('----------------------------STOPPED----------------------------')
    except requests.exceptions.ConnectionError:
        print('Failed to establish connection.')

