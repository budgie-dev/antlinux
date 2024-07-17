from os import system as sys

def main():   
    print('Install Ant Linux? Y/N')
    installchoice = input()
    if installchoice == 'Y' or installchoice == 'y':
        install()
    else:
        exit()

def install():
    sys('rm -rf /home/burnmybread/.config/neofetch ~/.config/rofi')
    sys('mkdir /home/burnmybread/.config/rofi')
    sys('rm /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml')
    sys('rm /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml')
    sys('rm /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml')
    sys('rm -rf /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-screensaver.xml')
    sys('rm -rf /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-terminal.xml')
    sys('rm -rf /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml')
    sys('rm -rf /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml')
    sys('cp -r neofetch /home/burnmybread/.config/')
    sys('cp -r rofi /home/burnmybread/.config/')
    sys('mkdir /etc/dotfiles/')
    sys('cp -r wallpapers /etc/dotfiles/')
    sys('cp .bashrc /home/burnmybread/')
    sys('cp -r rose-pine-gtk /usr/share/themes/')
    sys('cp xfce/xfce4-desktop.xml /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/')
    sys('cp xfce/xfce4-keyboard-shortcuts.xml /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/')
    sys('cp xfce/xfce4-panel.xml /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/')
    sys('cp xfce/xfce4-power-manager.xml /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/')
    sys('cp xfce/xfce4-screensaver.xml /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/')
    sys('cp xfce/xfce4-terminal.xml /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/')
    sys('cp xfce/xfwm4.xml /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/')
    sys('cp xfce/xsettings.xml /home/burnmybread/.config/xfce4/xfconf/xfce-perchannel-xml/')
    sys('sudo rm /etc/resolv.conf')
    sys('cp resolv.conf /etc/')
    sys('sudo chattr +i /etc/resolv.conf')
    
if __name__ == '__main__':
    main()
