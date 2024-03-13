import c4d
from c4d import gui
# Welcome to the world of Python

# Main function
def main():
    for descId, bc in op.GetUserDataContainer():
        print ("*"*5,descId,"*"*5)
        for key, val in bc:
            for txt, i in c4d.__dict__.items():
                if key == i and txt[:5]=="DESC_":
                    print (txt,"=",val)
                    break
            else:
                print (key,"=",val)

# Execute main()
if __name__=='__main__':
    main()