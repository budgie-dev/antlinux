#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls -a --color=auto'
alias grep='grep --color=auto'
alias clear='clear && neofetch | lolcat -a -d 6 -s 100'
PS1='\[\033[31;1m\]╭─\u@\h \W\n╰─λ \[\033[0m\]'
alias sudo='sudo '

alias pacs='pacman -S'
alias kys='pacman -Rns'
alias pacr='pacman -R'
alias pacss='pacman -Ss'
alias yays='yay -S'
alias yayss='yay -Ss'

alias neoconf='cd ~/.config/neofetch && nano config.conf'
alias bashconf='nano ~/.bashrc && source ~/.bashrc'

alias stfu='shutdown -h now'

neofetch | lolcat -d 6 -s 100 -a
