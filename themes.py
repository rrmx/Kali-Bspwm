import os
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

banner = """
████████╗███████╗███╗   ███╗ █████╗ ███████╗
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔════╝
   ██║   █████╗  ██╔████╔██║███████║███████╗
   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║
   ██║   ███████╗██║ ╚═╝ ██║██║  ██║███████║
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
"""

def menu():
    red()
    print(banner)
    blue()
    print("\n[+] Selecione lo que desea instalar [+]")
    print("\n1 -> s4vitar 2021 ")
    print("\n2 -> s4vitar 2023 ")
    print("\n3 -> rrmx 2023 ")
    print("\n4 -> Salir ")

    option = input("\n-->> ")

    if option == "1":
        s4vitar2021()
    if option == "2":
        s4vitar2023()
    if option == "3":
        rrmx2023()
    if option == "4":
        exit()

def s4vitar2021():
    blue()
    print("\n[+] Tema de s4vitar 2021 [+]")
    green()
    print("\n")

    # Actualizar sistema
    os.system("sudo apt update -y")
    os.system("sudo apt upgrade -y")

    # Dependencias del tema
    os.system("sudo apt install kitty rofi feh scrot acpi ranger xclip wmname scrub imagemagick caja neofetch -y")
    os.system("sudo apt install bat lsd papirus-icon-theme i3lock-fancy -y")
    
    # Fuentes Hack Ner Fonts
    os.system("sudo mkdir -p /usr/local/share/fonts")
    os.system("wget https://github.com/rrmx/dotfiles/releases/download/Fonts/HackNerdFonts.zip")
    os.system("unzip HackNerdFonts.zip")
    os.system("sudo cp -f *.ttf /usr/local/share/fonts/")
    os.system("sudo rm -r HackNerdFonts.zip *.md *.ttf")

    # Instalando fastTCPscan.go
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/scripts/fastTCPscan.go")
    os.system("sudo chmod +x fastTCPscan.go")
    os.system("sudo cp -f fastTCPscan.go /usr/bin")
    os.system("sudo rm -r fastTCPscan.go")

    # Instalando wichSystem.py
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/scripts/whichSystem.py")
    os.system("sudo chmod +x whichSystem.py")
    os.system("sudo cp -f whichSystem.py /usr/bin")
    os.system("sudo rm -r whichSystem.py")

    # Tema de bspwm
    os.system("mkdir -p ~/.config/bspwm/scripts/")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/config/bspwm/bspwmrc")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/config/bspwm/scripts/bspwm_resize")
    os.system("cp -f bspwmrc ~/.config/bspwm/")
    os.system("cp -f bspwm_resize ~/.config/bspwm/scripts/")
    os.system("chmod +x ~/.config/bspwm/bspwmrc")
    os.system("chmod +x ~/.config/bspwm/scripts/bspwm_resize")
    os.system("sudo rm -r bspwm_resize bspwmrc")

    # Tema sxhkd
    os.system("mkdir -p ~/.config/sxhkd")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/config/sxhkd/sxhkdrc")
    os.system("cp -f sxhkdrc ~/.config/sxhkd/")
    os.system("sudo rm -r sxhkdrc")

    # Temas picom
    expback = input("\n Tema de picom ( 1 --> glx )  ( 2 --> xrender ). 1/2 -> ")

    if expback == "1":
        os.system("mkdir -p ~/.config/picom/")
        os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/config/picom/glx/picom.conf")
        os.system("cp -f picom.conf ~/.config/picom/")
        os.system("sudo rm -r picom.conf")

    if expback == "2":
            os.system("mkdir -p ~/.config/picom/")
            os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/config/picom/xrender/picom.conf")
            os.system("cp -f picom.conf ~/.config/picom/")
            os.system("sudo rm -r picom.conf")

    # Tema polybar
    expback = input("\n Resoluciòn de tu monitor o pantalla (1 -> HD) (2 -> FHD) (3 -> QHD) (4 -> UHD). 1/2/3/4 -> ")

    # Resolucion HD High Definition 1.280 x 720 píxeles
    if expback == "1":
            os.system("mkdir -p ~/.config/polybar/")
            os.system("wget https://github.com/rrmx/dotfiles/releases/download/s4vitar_2021/s4vitar_2021.zip")
            os.system("unzip s4vitar_2021.zip")
            os.system("mv HD polybar")
            os.system("cp -rf polybar ~/.config/")
            os.system("sudo rm -r /usr/share/fonts/truetype/*.ttf")
            os.system("sudo rm -r /usr/share/fonts/truetype/*.otf")
            os.system("sudo cp -f ~/.config/polybar/fonts/* /usr/share/fonts/truetype")
            os.system("fc-cache -v")
            os.system("sudo rm -r FHD polybar QHD s4vitar_2021.zip UHD")

    # Resolucion FHD Full HD o Full High Definition 1.920 x 1.080 píxeles
    if expback == "2":
            os.system("mkdir -p ~/.config/polybar/")
            os.system("wget https://github.com/rrmx/dotfiles/releases/download/s4vitar_2021/s4vitar_2021.zip")
            os.system("unzip s4vitar_2021.zip")
            os.system("mv FHD polybar")
            os.system("cp -rf polybar ~/.config/")
            os.system("sudo rm -r /usr/share/fonts/truetype/*.ttf")
            os.system("sudo rm -r /usr/share/fonts/truetype/*.otf")
            os.system("sudo cp -f ~/.config/polybar/fonts/* /usr/share/fonts/truetype")
            os.system("fc-cache -v")
            os.system("sudo rm -r HD polybar QHD s4vitar_2021.zip UHD")

    # Resolucion QHD Quad High Definition 2.560 x 1.440 píxeles
    if expback == "3":
            os.system("mkdir -p ~/.config/polybar/")
            os.system("wget ")
            os.system("unzip ")
            os.system("cp -rf polybar ~/.config/")
            os.system("sudo rm -r /usr/share/fonts/truetype/*.ttf")
            os.system("sudo rm -r /usr/share/fonts/truetype/*.otf")
            os.system("sudo cp -f ~/.config/polybar/fonts/* /usr/share/fonts/truetype")
            os.system("fc-cache -v")
            os.system("sudo rm -r ")

    # Resolucion UHD Ultra High Definition 3.840 x 2.160 píxeles
    if expback == "4":
            os.system("mkdir -p ~/.config/polybar/")
            os.system("wget ")
            os.system("unzip ")
            os.system("cp -rf polybar ~/.config/")
            os.system("sudo rm -r /usr/share/fonts/truetype/*.ttf")
            os.system("sudo rm -r /usr/share/fonts/truetype/*.otf")
            os.system("sudo cp -f ~/.config/polybar/fonts/* /usr/share/fonts/truetype")
            os.system("fc-cache -v")
            os.system("sudo rm -r ")

    # Tema de kitty
    os.system("mkdir -p ~/.config/kitty/")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/config/kitty/color.ini")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/config/kitty/kitty.conf")
    os.system("cp -f color.ini ~/.config/kitty/")
    os.system("cp -f kitty.conf ~/.config/kitty/")
    os.system("sudo rm -r kitty.conf color.ini")

    # Tema de nano
    os.system("mkdir -p ~/.config/nano/")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/config/nano/nanorc")
    os.system("cp -f nanorc ~/.config/nano")
    os.system("sudo rm -r nanorc")

    # Tema nvim
    os.system("mkdir -p ~/.config/nvim/colors/")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/config/nvim/colors/nord.vim")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/config/nvim/init.vim")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/config/nvim/lotusbar.vim")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/config/nvim/lotus.vim")
    os.system("cp -f nord.vim ~/.config/nvim/colors/")
    os.system("cp -f init.vim ~/.config/nvim/")
    os.system("cp -f lotus.vim ~/.config/nvim/")
    os.system("cp -f lotusbar.vim ~/.config/nvim/")
    os.system("sudo rm -r nord.vim init.vim lotus.vim lotusbar.vim")

    # Tema de rofi
    os.system("mkdir -p ~/.config/rofi/themes")
    os.system("wget ")
    os.system("unzip rofi-themes.zip")
    os.system("cp -f *.rasi ~/.config/rofi/themes")
    os.system("fc-cache -fv")
    os.system("rofi-theme-selector")
    os.system("sudo rm -r *.rasi rofi-themes.zip")

    # Instalacion de powerless10k
    os.system("mkdir -p ~/.powerlevel10k")
    os.system("sudo rm -r ~/.powerlevel10k") 
    os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k")
    os.system("echo 'source ~/.powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc")

    # Instalacion de powerlevel10k para root
    os.system("mkdir -p /root/.powerlevel10k")
    os.system("sudo rm -r /root/.powerlevel10k")
    os.system("sudo git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /root/.powerlevel10k")

    # Permiso de privilegios para zsh
    os.system("sudo chmod -R 755 /usr/local/share/zsh/site-functions")
    os.system("sudo chown -R root:root /usr/local/share/zsh/site-functions")
    os.system("sudo chmod -R 755 /usr/local/share/zsh")
    os.system("sudo chown -R root:staff /usr/local/share/zsh")

    # Permiso de ususrio de vajos previlegios para home
    os.system("sudo chown $(whoami):$(whoami) /home/$USER")
    os.system("sudo chown -R $(whoami):$(whoami) /home/$USER/.cache")
    os.system("sudo chown -R $(whoami):$(whoami) /home/$USER/.ssh")

    # Permiso de ususrio de vajos previlegios para root
    os.system("sudo chown $(whoami):$(whoami) /root")
    os.system("sudo chown -R $(whoami):$(whoami) /root/.cache")
    os.system("sudo chown -R $(whoami):$(whoami) /root/.ssh")

    # Poner de a zsh de shell
    os.system("sudo usermod --shell /usr/bin/zsh root")
    os.system("sudo usermod --shell /usr/bin/zsh $USER")

    # Instalacion de fzf
    os.system("mkdir -p ~/.fzf")
    os.system("sudo rm -r ~/.fzf")
    os.system("git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf")
    os.system("~/.fzf/install")

    # Instalacion de fzf para root
    os.system("mkdir -p /root/.fzf")
    os.system("sudo rm -r /root/.fzf")
    os.system("sudo git clone --depth 1 https://github.com/junegunn/fzf.git /root/.fzf")
    os.system("sudo /root/.fzf/install")

    # Tema p10k
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/.p10k.zsh")
    os.system("cp -f .p10k.zsh ~/.p10k.zsh")
    os.system("sudo ln -s -fv ~/.p10k.zsh /root/.p10k.zsh")
    os.system("sudo rm -r .p10k.zsh")

    # Tema zshrc
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2021/.zshrc")
    os.system("cp -f .zshrc ~/.zshrc")
    os.system("sudo ln -s -fv ~/.zshrc /root/.zshrc")
    os.system("sudo rm -r .zshrc")

    print("\n[+] Instalacion Terminada [+]\n")

def s4vitar2023():
    print("\n[+] Tema de s4vitar 2023 [+]\n")
    green()
    
    # Actualizar sistema
    os.system("sudo apt update -y")
    os.system("sudo apt upgrade -y")

    # Dependencias
    os.system("sudo apt install rofi feh xclip wmname caja bat lsd kitty scrot acpi scrub imagemagick neofetch ripgrep -y")

    # Fuentes Hack Ner Fonts
    os.system("wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/Hack.zip")
    os.system("unzip Hack.zip")
    os.system("sudo cp *.ttf /usr/local/share/fonts/")
    os.system("rm -r Hack.zip *.md *.ttf")

    # Instalando fastTCPscan.go
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2023/scripts/fastTCPscan.go")
    os.system("sudo chmod +x fastTCPscan.go")
    os.system("sudo cp fastTCPscan.go /bin")
    os.system("rm -r fastTCPscan.go")

    # Instalando wichSystem.py
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2023/scripts/whichSystem.py")
    os.system("sudo chmod +x whichSystem.py")
    os.system("sudo cp whichSystem.py /bin")
    os.system("rm -r whichSystem.py")

    # Tema de bspwm
    os.system("mkdir -p ~/.config/bspwm/scripts/")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2023/config/bspwm/scripts/bspwm_resize ")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2023/config/bspwm/bspwmrc")
    os.system("cp bspwmrc ~/.config/bspwm/")
    os.system("cp bspwm_resize ~/.config/bspwm/scripts/")
    os.system("chmod +x ~/.config/bspwm/bspwmrc")
    os.system("chmod +x ~/.config/bspwm/scripts/bspwm_resize")
    os.system("rm -r bspwm_resize bspwmrc")

    # Tema sxhkd
    os.system("mkdir -p ~/.config/sxhkd")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2023/config/sxhkd/sxhkdrc")
    os.system("cp sxhkdrc ~/.config/sxhkd/")
    os.system("rm -r sxhkdrc")

    # Temas picom
    os.system("mkdir -p ~/.config/picom/")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2023/config/picom/picom.conf")
    os.system("cp picom.conf ~/.config/picom/")
    os.system("rm -r picom.conf")

    # Tema polybar
    os.system("mkdir -p ~/.config/polybar/")
    os.system("wget ")
    os.system("unzip s4vitar_2023.zip")
    os.system("cp -r polybar ~/.config/")
    os.system("sudo rm -r /usr/share/fonts/truetype/*.ttf")
    os.system("sudo rm -r /usr/share/fonts/truetype/*.otf")
    os.system("sudo cp ~/.config/polybar/fonts/* /usr/share/fonts/truetype")
    os.system("fc-cache -v")
    os.system("sudo rm -r s4vitar_2023.zip polybar")

    # Tema de kitty
    os.system("mkdir -p ~/.config/kitty/")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2023/config/kitty/color.ini")
    os.system("wget https://raw.githubusercontent.com/rrmx/dotfiles/dotfiles/Kali-Linux/bspwm/s4vitar/2023/config/kitty/kitty.conf")
    os.system("cp color.ini ~/.config/kitty/")
    os.system("cp kitty.conf ~/.config/kitty/")
    os.system("rm -r kitty.conf color.ini")

    # Instalacion nvim
    os.system("wget https://github.com/neovim/neovim/releases/download/v0.9.5/nvim-linux64.tar.gz")
    os.system("tar -xvf nvim-linux64.tar.gz")
    os.system("sudo cp -r nvim-linux64 /opt/")
    os.system("sudo rm -r nvim-linux64.tar.gz nvim-linux64")

    # Tema nvim
    os.system("mkdir -p ~/.config/nvim/")
    os.system("git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1")

    # Tema de rofi
    os.system("mkdir -p ~/.config/rofi/themes")
    os.system("wget https://github.com/rrmx/dotfiles/releases/download/recursos/rofi-themes.zip")
    os.system("unzip rofi-themes.zip")
    os.system("cp *.rasi ~/.config/rofi/themes")
    os.system("fc-cache -fv")
    os.system("rofi-theme-selector")
    os.system("rm -r *.rasi rofi-themes.zip")

    # Instalacion de powerlevel10k 
    os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k")
    os.system("echo 'source ~/.powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc")

    # Instalacion de powerlevel10k para root
    os.system("sudo git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /root/.powerlevel10k")

    # Permiso de privilegios para zsh
    os.system("sudo chmod -R 755 /usr/local/share/zsh/site-functions")
    os.system("sudo chown -R root:root /usr/local/share/zsh/site-functions")
    os.system("sudo chmod -R 755 /usr/local/share/zsh")
    os.system("sudo chown -R root:staff /usr/local/share/zsh")

    # Permiso de ususrio de vajos previlegios para home
    os.system("sudo chown $(whoami):$(whoami) /home/$USER")
    os.system("sudo chown -R $(whoami):$(whoami) /home/$USER/.cache")
    #os.system("sudo chown -R $(whoami):$(whoami) /root/.local")
    os.system("sudo chown -R $(whoami):$(whoami) /home/$USER/.ssh")

    # Permiso de ususrio de vajos previlegios para root
    os.system("sudo chown $(whoami):$(whoami) /root")
    os.system("sudo chown -R $(whoami):$(whoami) /root/.cache")
    #os.system("sudo chown -R $(whoami):$(whoami) /root/.local")
    os.system("sudo chown -R $(whoami):$(whoami) /root/.ssh")

    # Poner de a zsh de shell
    #os.system("sudo usermod --shell /usr/bin/zsh root")
    #os.system("sudo usermod --shell /usr/bin/zsh $USER")

    # Instalacion de fzf
    os.system("git clone --depth 1 https://github.com/junegunn/fzf.git ~/.config/fzf")
    os.system("~/.config/fzf/install")

    # Instalacion de fzf para root
    os.system("sudo git clone --depth 1 https://github.com/junegunn/fzf.git /root/.config/fzf")
    os.system("sudo /root/.config/fzf/install")

    # Tema p10k
    os.system("wget ")
    os.system("cp .p10k.zsh ~/.p10k.zsh")
    os.system("sudo ln -s -fv ~/.p10k.zsh /root/.p10k.zsh")
    os.system("rm -r .p10k.zsh")

    # Tema zshrc
    os.system("wget ")
    os.system("cp .zshrc ~/.zshrc")
    os.system("sudo ln -s -fv ~/.zshrc /root/.zshrc")
    os.system("rm -r .zshrc")

    print("\n[+] Instalacion Terminada [+]\n")

def rrmx2023():

    print("\n[+] Tema de Rrmx 2023 [+]\n")   
    green()

    # Dependencias
    os.system("sudo apt install rofi papirus-icon-theme feh ranger xclip wmname caja neofetch pulseaudio pamixer alsa-utils -y")
    os.system("sudo apt install bat lsd kitty scrot acpi scrub imagemagick i3lock-fancy brightnessct -y")
    os.system("sudo apt install rofi papirus-icon-theme feh ranger xclip wmname caja neofetch -y")
    os.system("sudo apt install bat lsd kitty scrot acpi scrub imagemagick i3lock-fancy -y")
    os.system("sudo apt install brightnessctl alsa-utils pulseaudio pamixer -y")
    
    # Dependecias rofi
    #os.system("sudo apt install bison flex libstartup-notification0-dev check autotools-dev libglib2.0-dev libxkbcommon-dev libxkbcommon-x11-dev libjpeg-dev -y")
    #os.system("sudo apt install libpango1.0-dev librsvg2-bin librsvg2-dev libcairo2-dev -y")

    print("\n[+] INSTALACIÓN TERMINADA [+]\n")


if __name__ == '__main__':
    id = os.getuid()

    if id == 0:
        red()
        print()
        print("[!] No hay que ser root para ejecutar la herramienta")
        print()
    else:
        menu()