'''
Purpose: 
Aggregate ip visits in nginx log to identify top offending subnets to block


To run: 
python3 log_analyzer.py



Author: Rocky Wang
'''

from pathlib import Path
from heapq import heapify,heappop, heappush

def main():
    # read file
    print(Path().absolute())
    filename="./log_analyzer/access.log"
 
    try:
        with open(filename,"r") as f:
            log=f.read()
    except FileNotFoundError:
        print("File not found. Check the path variable and filename")
        exit()

    #print(log)
    mydict={}
    for row in log.splitlines():
        #print (row)
        index=row.find(" - - ")
        ip=row[0:index]
        #print(ip)
        if ip in mydict:
            mydict[ip]= mydict[ip]+1
        else:
            mydict[ip]=1
        #print (mydict[ip])
    '''after this, we get: mydict=
    110.2.3.4     : 100
    112.2.3.8     : 98
    ...
    '''
    myheap=[]
    for ip in mydict:
        heappush(myheap,(-1*mydict[ip],ip))

    print("#####The following is Cnt of visits, the IP######")
    for i in range(10):
        item= heappop(myheap)
        print(item[0]*-1,"   ",item[1])

    print("#####The following is Cnt of visits, count of unique IPs in the subnet, the subnet######")
## how about check data center IPs with same subnets
    #take advantage of the mydict above

    datacenterdict={}
    for ip, cnt in mydict.items():
        #print (row)
        index1=ip.find(".")
        index2=ip.find(".",index1+1,len(ip))
        index3=ip.find(".",index2+1,len(ip))
        subnet= ip[0:index3]
        #print(ip)
        if subnet in datacenterdict:
            datacenterdict[subnet]['ipcount']=datacenterdict[subnet]['ipcount']+1
            datacenterdict[subnet]['visitcount']=datacenterdict[subnet]['visitcount']+mydict[ip]
        else:
            #datacenterdict[subnet]['ipcount']=1
            #datacenterdict[subnet]['visitcount']=mydict[ip]
            datacenterdict[subnet]={'ipcount': 1, 'visitcount' : mydict[ip]}



        #print (mydict[ip])

    # put the dictionary items into the heap
    datacenterheap=[]
    for subnet in datacenterdict:
        heappush(datacenterheap,(-1*datacenterdict[subnet]['visitcount'],datacenterdict[subnet]['ipcount'],subnet))

    #find the top 10
    for i in range(10):
        item= heappop(datacenterheap)
        print(item[0]*-1,"   ",item[1],"   ",item[2])


if __name__ == "__main__":
    main()

