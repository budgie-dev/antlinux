from os import system as sys

def main():   
    print('Install Ant Linux? Y/N')
    installchoice = input()
    if installchoice == 'Y' or 'y':
        install()
    else:
        exit()

def install():
    sys('./remove.sh')
    sys('./cp.sh')
    sys('./pacpkgs.sh')
    sys('./dns.sh')

if __name__ == '__main__':
    main()
