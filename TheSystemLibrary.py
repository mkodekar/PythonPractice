"""
Run this from an outside terminal or cmd prompt 

you will miss the fun stuff if you run it from an ide like 

pycharm.

the output of the command is shown in the extendedterminal.png

"""
import sys as s


# s.stderr.write('This is stderr text\n')
# s.stderr.flush()
# s.stdout.write('This is stdout text\n')
# s.stdout.flush()

# print(s.argv)

# can be also done without len function
# length is for checking length.
# if len(s.argv) > 1:
#    print(s.argv[1])

def main(arg):
    if len(arg) > 1:
        print(arg[1])
    else:
        s.stderr.write('No argument supplied')
        s.stderr.flush()

main(s.argv)
