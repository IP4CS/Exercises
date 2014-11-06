'''
Tower of Hanoi
Object: to move n disks from one peg to another peg. Three pegs in total. 
Rules: Move one disk at one time; Larger disk should never fall on top of the smaller one. 
Keyword: Recursive thinking
@ytang 11/06/2014
'''

def Hanoi(n, source, helper, destination):
    if n==0:
        return 0
    else:
        #Move n-1 from source to helper
        Hanoi(n-1, source, destination, helper)
    
        #Move one disk from helper peg to destination peg
        if source[0] != []:
            disk = source[0].pop()
            destination[0].append(disk)
            print "move number %d disk from the %s peg to the %s peg.\n"  %(disk, source[1], destination[1])
            
        #move n-1 disks from helper to destination
        Hanoi(n-1, helper, source, destination)
            
n = int(raw_input("Give the number of disks \n"))
source = (range(n, 0, -1), "source")
helper = ([], "helper")
destination = ([], "destination")

Hanoi(n, source, helper, destination)

