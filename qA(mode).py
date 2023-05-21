""" input file to calculate the distance
5  4
9  9"""
try:
    input_file=open("d.txt")
    try:
        for line in input_file:
        
             part=line.rsplit()
             v=int(part[0])
             t=int(part[1])
             d=v*t
             print("The distance when v= ",v,"and t= ",t,"is ",d)
    finally:
        input_file.close()
    
except IOError:
     print(" could not open input file")
     
except Exception as exceptObj:
    print("error",str(exceptObj))
    
    
