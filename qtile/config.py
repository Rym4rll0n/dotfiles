
######################
#  IMPORTAR MÓDULOS  #
######################

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import sh, subprocess, time, os, random


# Para o módulo "sh" funcionar é necessário instalar o pacote "sh" usando o gerenciador de pacotes "pip":
#
# sudo pacman -S python python-pip
#
# pip install sh

#################################################################
# SCRIPT PARA O QTILE USAR O ESQUEMA DE CORES GERADO PELO PYWAL #
#################################################################

import json

def get_colors():
	with open('/home/rymarllon/.cache/wal/colors.json') as f:
		colors = json.load(f)
	bg = colors['special']['background']
	fg = colors['special']['foreground']
	cor1 = colors['colors']['color1']
	cor2 = colors['colors']['color2']
	cor3 = colors['colors']['color3']
	cor4 = colors['colors']['color4']
	cor5 = colors['colors']['color5']
	cor6 = colors['colors']['color6']
	cor7 = colors['colors']['color7']
	cor8 = colors['colors']['color8']
	cor9 = colors['colors']['color9']
	cor10 = colors['colors']['color10']
	cor11 = colors['colors']['color11']
	cor12 = colors['colors']['color12']
	cor13 = colors['colors']['color13']
	cor14 = colors['colors']['color14']
	cor15 = colors['colors']['color15']
	return bg, fg, cor1, cor2, cor3, cor4, cor5, cor6, cor7, cor8, cor9, cor10, cor11, cor12, cor13, cor14, cor15

bg, fg, cor1, cor2, cor3, cor4, cor5, cor6, cor7, cor8, cor9, cor10, cor11, cor12, cor13, cor14, cor15 = get_colors()


################################################################################################################
#
# Para pegar a paleta de cores do wallpaper e usar para modificar as cores do terminal instale o módulo "pywal":
#
#	sudo pacman -S python-pip
#
#	sudo pacman -S imagemagick
#
#	pip install pywal
#
# Para usar o comando "wal" adicione o caminho do executável no "~/.bashrc":
#
#  nano ~/.bashrc
#
#	export PATH=$PATH:~/.local/bin
#
# Para que as alterações fiquem disponível na sua sessão atual execute o comando abaixo:
#
#	source ~/.bashrc
#
# Adicione essa linha no seu "~/.bashrc" ou outro shell que você estiver usando:
#
#  nano ~/.bashrc
#
#	(cat ~/.cache/wal/sequences &)
#
# Use o pywal para pegar a paleta de cores do seu wallpaper:
#
#	wal -i ~/.Wallpapers/seu-papel-de-parede.jpg
#
################################################################################################################



##################################################################################
#  CONFIGURAÇÃO DOS ATALHOS PARA ABRIR APLICATIVOS E COMPORTAMENTO DAS JANELAS   #  
##################################################################################

mod = 'mod4'
ctrl = 'control'
alt = 'mod1'
shift = 'shift'
terminal = guess_terminal() # default qtile

keys = [

    	# MOVIMENTO DAS TELAS
    Key([alt], 'h', lazy.spawn('qtile-cmd -o cmd -f next_screen')),
    Key([alt], 'l', lazy.spawn('qtile-cmd -o cmd -f previous_screen')),

	# FOCUS DA JANELA
    Key([mod], 'j', lazy.layout.down(), desc='Foco na janela de baixo'),
    Key([mod], 'k', lazy.layout.up(), desc='Foco na janela de cima'),
    Key([mod], 'h', lazy.layout.left(), desc='Foco na janela da esquerda'),
    Key([mod], 'l', lazy.layout.right(), desc='Foco na janela da direita'),
    Key([mod], "space", lazy.layout.next(), desc='Foco na próxima janela'),

	# MOVIMENTO DA JANELA FOCADA
    Key([mod, shift], 'j', lazy.layout.shuffle_down(), desc='Move a janela pra baixo'),
    Key([mod, shift], 'k', lazy.layout.shuffle_up(), desc='Move a janela pra cima'),
    Key([mod, shift], 'h', lazy.layout.swap_left(), desc='Move a janela pra esquerda'),
    Key([mod, shift], 'l', lazy.layout.swap_right(), desc='Move a janela pra direita'), 
    Key([mod, shift], 'space', lazy.layout.rotate(), desc='Move a janela para a próxima na sequência'),

	# TAMANHO DA JANELA
    Key([mod], 'equal', lazy.layout.grow(), desc='Aumenta o tamanho da janela'),
    Key([mod], 'minus', lazy.layout.shrink(), desc='Diminui o tamanho da janela'),
    Key([mod, shift], "Return", lazy.layout.toggle_split(), desc='Muda entre janelas separadas ou maximizadas'),

	# QTILE GERAL
    Key([mod], 'Tab', lazy.next_layout(), desc='Troca tipo de layout'),
    Key([mod, ctrl], 'w', lazy.window.kill(), desc='Fecha a janela focada'),
    Key([mod, 'control'], 'r', lazy.restart(), desc='Restart qtile'),
    Key([mod, "control"], 'q', lazy.shutdown(), desc='Sai do Qtile'),
    Key([mod], 'r', lazy.spawncmd(), desc='Abre o widget Prompt pra executar comando'),

	# TECLAS DE AUDIO
    Key([], 'XF86AudioPlay', lazy.spawn('playerctl play-pause'), desc='Play ou Pause'),
    Key([], 'XF86AudioNext', lazy.spawn('playerctl next'), desc='Próxima faixa'),
    Key([], 'XF86AudioPrev', lazy.spawn('playerctl previous'), desc='Faixa anterior'),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer -c 0 -q set Master 2dB+'), desc='Aumenta o volume'),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer -c 0 -q set Master 2dB-'), desc='Diminui o volume'),
    Key([], 'XF86AudioMute', lazy.spawn('pulsemixer --toggle-mute'), desc='Muta/Desmuta o volume'),

	# PROGRAMAS
    Key([mod], "Return", lazy.spawn(terminal), desc='Abre o terminal'),
    Key([mod], 'e', lazy.spawn('pcmanfm'), desc='Abre o gerenciador de arquivos'),
    Key([mod], 'f', lazy.spawn('firefox'), desc='Abre o Firefox'),
    Key([mod], 'c', lazy.spawn('chromium'), desc='Abre o Chromium'),
    Key([mod], 'q', lazy.spawn('qutebrowser'), desc='Abre o qutebrowser'),
    Key([mod], 'g', lazy.spawn('google-chrome-stable'), desc='Abre o Google Chrome'),
    Key([mod], 't', lazy.spawn('telegram-desktop'), desc='Abre o Telegram'),
    Key([mod], 'v', lazy.spawn('nvim'), desc='Abre o NeoVim'),
    Key([mod], 'n', lazy.spawn('mousepad'), desc='Abre o editor de texto Mousepad'),
    Key([mod], 'i', lazy.spawn('python3 -m idlelib.idle'), desc='Abre o console idle do Python3'),
    Key([mod], 's', lazy.spawn('flatpak run com.spotify.Client'), desc='Abre o Spotify'),
    Key([mod], 'm', lazy.spawn('clementine'), desc='Abre o Clementine'),
    Key([mod], 'o', lazy.spawn('libreoffice'), desc='Abre o LibreOffice'),
    Key([mod], 'w', lazy.spawn('steam'), desc='Abre a Steam jogos'),
    Key([alt], 't', lazy.spawn('thunderbird'), desc='Abre o Thunderbird'),
    Key([alt], 'i', lazy.spawn('inkscape'), desc='Abre o Inkscape'),
    Key([alt], 'c', lazy.spawn('code'), desc='Abre o Visual Studio Code'),
    Key([alt], 'g', lazy.spawn('gimp'), desc='Abre o Gimp'),
    Key([alt], 'm', lazy.spawn('cmus'), desc='Abre o C* MUsic Player'),
    Key([alt], 'v', lazy.spawn('vivaldi-stable'), desc='Abre o navegador Vivaldi'),
    Key([alt], 'e', lazy.spawn('microsoft-edge-dev'), desc='Abre o navegador Microsoft Edge'),
    Key([alt], 'p', lazy.spawn('pycharm'), desc='Abre o Pycharm'),
    Key([alt], 's', lazy.spawn('subl3'), desc='Abre o Sublime Text'),
    Key([shift], 'e', lazy.spawn('emacs'), desc='Abre o Emacs'),
    Key([shift], 's', lazy.spawn('rofi -show drun'), desc='Abre o menu do rofi'),
    Key([shift], 'Print', lazy.spawn('escrotum -s /home/rymarllon/Imagens/Print/%d-%m-%Y-%Hh%Mmin.png'), desc='Tira print da área selecionada'),
]

web = Match(wm_class=['qutebrowser', 'firefox', 'Vivaldi-stable', 'vivaldi-stable', 'Microsoft-edge-dev', 'microsoft-edge-dev', 'Google-chrome', 'google-chrome', 'Chromium', 'chromium'])
terminal = Match(wm_class=['Xfce4-terminal', 'xfce4-terminal', 'XTerm', 'xterm', 'URxvt', 'urxvt', 'Alacritty', 'kitty', 'terminal', 'shell', 'bash', 'zsh', 'terminator'])
arq = Match(wm_class=['libreoffice', 'libreoffice-startcenter', 'libreoffice-writer', 'libreoffice-calc', 'libreoffice-impress', 'libreoffice-draw', 'libreoffice-math', 'libreoffice-base', 'files', 'Nemo', 'nemo', 'Pcmanfm', 'pcmanfm', 'Mousepad', 'mousepad', 'Gimp', 'gimp', 'org.inkscape.Inkscape', 'Inkscape'])
social = Match(wm_class=['Mail', 'Thunderbird', 'Discord', 'discord', 'TelegramDesktop', 'telegram-desktop'])
python = Match(wm_class=['jetbrains-pycharm-ce', 'Emacs', 'emacs', 'VSCodium', 'vscodium', 'code-oss', 'subl3', 'python', 'Python', 'ipython', 'py', 'Designer', 'Qt', 'idle', 'Toplevel'])
musica = Match(wm_class=['Spotify', 'spotify', 'Clementine', 'clementine', 'cmus'], title=['Spotify Premium'])
steam = Match(wm_class=['Steam', 'steam', 'WAKFU', 'game'], title=['Steam', 'steam'])

# Instale o pacote "xorg-xprop", depois digite o comando:
# xprop | grep CLASS
# Agora clique no programa aberto para exibir o nome dele no terminal.
# Use o nome do programa para incluir nas configurações do Match(wm_class=[]).

groups = [
	Group('1', label='🌐:1', matches=[web], exclusive=True, layout='max'),
	Group('2', label='🐚:2', matches=[terminal], exclusive=True, layout='monadtall'),
	Group('3', label='📂:3', matches=[arq], layout='monadwide'),
	Group('4', label='🤳:4', matches=[social], exclusive=True, layout='monadtall'),
	Group('5', label='🐍:5', matches=[python], exclusive=True, layout='max'),
	Group('6', label='📻:6', matches=[musica], exclusive=True, layout='max'),
	Group('7', label='👾:7', matches=[steam], exclusive=True, layout='max'),
	Group('8', label='🌌:8')
]

for i in groups:
    keys.extend([
        # mod4 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod4 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])


############################################################################
# OS LAYOUTS SÃO USADOS PARA DEFINIR COMO JANELAS DOS APLICATVOS VÃO ABRIR #
############################################################################

layout_config = dict(
#    border_focus = borda,
    margin = 1,
    border_width = 3
)

layouts = [
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Columns(),
    layout.Matrix(columns=3, **layout_config),
    layout.MonadTall(**layout_config),
    layout.MonadWide(**layout_config),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]



######################################################################
#           AQUI VOCÊ CONFIGURA O TIPO DA FONTE E TAMANHO            #
######################################################################

widget_defaults = dict(
    font='Cantarell Bold',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


############# NECESSÁRIO INSTALAR ALGUMAS FONTES ########################
#
# sudo pacman -S cantarell-fonts
# sudo pacman -S ttf-joypixels
# sudo pacman -S ttf-font-awesome otf-font-awesome awesome-terminal-fonts
#########################################################################



###################################
# CONFIGURAÇÃO DA BARRA DE STATUS #
###################################



screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale=0.70),
                widget.GroupBox(
                    highlight_method = 'block',
                    highlight_color='1f004d',
                    inactive = '751aff',
                    this_current_screen_border = '8533ff',
                    this_screen_border = '944dff',
                    other_current_screen_border = '8533ff',
                    other_screen_border = '944dff',
                    font_shadow='e9e9e9',
                    disable_drag=True,
                ),
                widget.Prompt(prompt='Executar: '),
                widget.WindowName(fmt='🐧{}🐧', for_current_screen=True),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Volume(emoji=True),
                widget.Sep(foreground='23064f', padding=1, size_percent=100, linewidth=3),
                widget.Clock(format='%a %d/%m/%Y %H:%M'),
                widget.Sep(foreground='23064f', padding=1, size_percent=100, linewidth=3),
                widget.QuickExit(default_text='', countdown_format='{} segundos'),
            ], 25, margin=[3,5,2,5], background='1f004d'
        ), wallpaper='~/.wallpaper/wpp-img-exemplo.png', wallpaper_mode='fill'
    ),
    Screen(
    	bottom=bar.Bar(
    		[
    			widget.CPU(),
    			widget.CurrentLayoutIcon(scale=0.70),
    			widget.Spacer(length=bar.STRETCH),
    			widget.Systray(),
                widget.CheckUpdates(
                    display_format='Atualizações:{updates}',
                	update_interval=180
                ),
    			#widget.ThermalSensor(fmt='🌡️CPU:{}'),
    			widget.TextBox('📡'),
    			widget.NetGraph(),
    		], 23, margin=[2,5,3,5], background='1f004d'[::-1]
    	), wallpaper='~/.wallpaper/wpp-img-exemplo.png', wallpaper_mode='fill'
    ),
]

############### PACOTES NECESSÁRIOS ##############
#
# sudo pacman -S alsa-utils pulseaudio pavucontrol
# sudo pacman -S alsa-oss alsa-lib
# sudo pacman -S xsensors lm_sensors
# pip install psutil
##################################################



######################
# JANELAS FLUTUANTES #
######################

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#################################
# INICIAR PROGRAMAS COM O QTILE #
#################################

@hook.subscribe.startup_complete
def start_complete():
	home = os.path.expanduser('~/.config/qtile/scripts/autostart.py')
	subprocess.call([home])

@hook.subscribe.startup_once
def start_once():
	subprocess.call(['xrandr', '-s', '1024x768'])



################################################################################################################
# Você pode adicionar alguns programas que deseja iniciar junto com o qtile no arquivo "autostart.py" e depois chame esse script externo na configuração do qtile:
#
#	nano ~/.config/qtile/scripts/autostart.py
#
# #!/bin/bash
#
# picom --corner-radius 10 &
# dunst &
# #picom &
# xrandr -s 1024x768 &
# #wal -i ~/.Wallpapers/seu-papel-de-parede.jpg &
# #~/.cache/wal/colors.sh &
#
# Dê permissão para executar o script "autostart.py":
#
#	cd ~/.config/qtile/scripts && chmod +x autostart.py
#
################################################################################################################
