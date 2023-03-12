import os
import socket
import subprocess
from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import Drag, Group, Key, Match, Screen
from libqtile.command import lazy
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras import widget
from libqtile.bar import Bar
from libqtile.widget import Spacer
from libqtile.config import Screen

mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser("~")


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


myTerm = "alacritty"

keys = [
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "t", lazy.spawn(myTerm)),
    Key(
        [mod], "d", lazy.spawn("/home/wizard/.config/rofi/launchers/type-2/launcher.sh")
    ),
    Key(
        [mod],
        "x",
        lazy.spawn("/home/wizard/.config/rofi/powermenu/type-2/powermenu.sh"),
    ),
    Key(
        [mod],
        "r",
        lazy.spawn("dmenu_run -nb '#2e3440' -nf '#d8dee9' -sb '#d8dee9' -sf '#2e3440' -fn 'Fantasque Sans Mono Nerd Font-22'")),
    Key([mod], "Escape", lazy.spawn("xkill")),
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod], "KP_Enter", lazy.spawn(myTerm)),
    Key([mod, "shift"], "Return", lazy.spawn("thunar")),
    Key([mod, "shift"], "r", lazy.restart()),
    Key(["mod1"], "f", lazy.spawn("firefox")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "n", lazy.next_layout()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
]

groups = []

group_names = [
    "1",
    "2",
    "3",
    "4",
    "5",
]

group_labels = [
    "󰼏",
    "󰼐",
    "󰼑",
    "󰼒",
    "󰼓",
]

group_layouts = [
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "treetab",
    "floating",
]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
            Key(["mod1"], "Tab", lazy.screen.next_group()),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                lazy.group[i.name].toscreen(),
            ),
        ]
    )


def init_layout_theme():
    return {
        "margin": 10,
        "border_width": 2,
        "border_focus": "#8fbcbb",
        "border_normal": "#2e3440",
    }


layout_theme = init_layout_theme()


layouts = [
    layout.RatioTile(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
]


def init_colors():
    return [
        ["#2e3440", "#2e3440"],  # color 0 bg
        ["#1d2021", "#1d2021"],  # color 1 black
        ["#eceff4", "#eceff4"],  # color 2 fg white
        ["#bf616a", "#bf616a"],  # color 3 red
        ["#a3be8c", "#a3be8c"],  # color 4 green
        ["#5e81ac", "#5e81ac"],  # color 5 blue
        ["#d08770", "#d08770"],  # color 6 orange
        ["#b48ead", "#b48ead"],  # color 7 pink
        ["#ebcb8b", "#ebcb8b"],  # color 8 yellow
        ["#d8dee9", "#d8dee9"],  # color 9 cream
        ["#434c5e", "#434c5e"],  # color 10 medgrey
        ["#4c566a", "#4c566a"],  # color 11 grey
        ["#8fbcbb", "#8fbcbb"],  # color 12 grey
        ["#88c0d0", "#88c0d0"],  # color 13 grey
    ]


colors = init_colors()


def base(fg="text", bg="dark"):
    return {"foreground": colors[2], "background": colors[0]}


def init_widgets_defaults():
    return dict(
        font="Fantasque Sans Mono Nerd Font",
        fontsize=16,
        padding=6,
        background=colors[0],
    )


widget_defaults = init_widgets_defaults()


def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.Sep(linewidth=1, padding=5, foreground=colors[0]),
        widget.GroupBox(
            **base(bg=colors[0]),
            borderwidth=4,
            active=colors[12],
            inactive=colors[2],
            rounded=True,
            padding_y=0,
            highlight_method="line",
            urgent_alert_method="block",
            urgent_border=colors[3],
            this_current_screen_border=colors[13],
            this_screen_border=colors[6],
            other_current_screen_border=colors[6],
            other_screen_border=colors[9],
            disable_drag=True,
        ),
        widget.TaskList(
            highlight_method="block",
            fontsize=10,
            icon_size=15,
            margin_y=3,
            rounded=True,
            margin_x=10,
            border=colors[10],
            foreground=colors[2],
            txt_floating="🗗",
            txt_minimized=">_ ",
            borderwidth=1,
        ),
        widget.Spacer(),
        widget.CurrentLayoutIcon(
            padding=0,
            scale=0.7,
            margin_x=10,
            decorations=[
                BorderDecoration(
                    border_width=[0, 0, 3, 0],
                    colour=colors[5],
                )
            ],
        ),
        widget.CurrentLayout(
            decorations=[
                BorderDecoration(
                    border_width=[0, 0, 3, 0],
                    colour=colors[5],
                )
            ],
        ),
        widget.Spacer(),
        widget.TextBox(
            text='',
            font="Iosevka Nerd Font",
            background=colors[0],
            foreground=colors[3],
            padding=0,
            fontsize=26
        ),
        widget.CPU(
            format=" {load_percent}%",
            update_interval=1,
            foreground=colors[0],
            background=colors[3],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e htop")},
            # decorations=[
            #     BorderDecoration(
            #         border_width=[0, 0, 3, 0],
            #         colour=colors[3],
            #     )
            # ],
        ),
        widget.TextBox(
            text='',
            font="Iosevka Nerd Font",
            background=colors[3],
            foreground=colors[13],
            padding=0,
            fontsize=26
        ),
        widget.ThermalSensor(
            foreground=colors[0],
            format=" {temp:.0f}{unit}",
            background=colors[13],
            # decorations=[
            #     BorderDecoration(
            #         border_width=[0, 0, 3, 0],
            #         colour=colors[3],
            #     )
            # ],
        ),
        # widget.Sep(linewidth=1, padding=5, foreground=colors[0]),
        widget.TextBox(
            text='',
            font="Iosevka Nerd Font",
            background=colors[13],
            foreground=colors[6],
            padding=0,
            fontsize=26
        ),
        widget.Memory(
            format="{MemUsed: .0f}M",
            update_interval=1,
            measure_mem="M",
            foreground=colors[0],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e htop")},
            background=colors[6],
            # decorations=[
            #     BorderDecoration(
            #         border_width=[0, 0, 3, 0],
            #         colour=colors[6],
            #     )
            # ],
        ),
        # widget.Sep(linewidth=1, padding=5, foreground=colors[0]),
        widget.TextBox(
            text='',
            font="Iosevka Nerd Font",
            background=colors[6],
            foreground=colors[7],
            padding=0,
            fontsize=26
        ),
        widget.PulseVolume(
            fmt="墳 {}",
            background=colors[7],
            foreground=colors[0],
            # foreground=colors[2],
            # decorations=[
            #     BorderDecoration(
            #         border_width=[0, 0, 3, 0],
            #         colour=colors[7],
            #     )
            # ],
        ),
        # widget.Sep(linewidth=1, padding=5, foreground=colors[0]),
        widget.TextBox(
            text='',
            font="Iosevka Nerd Font",
            background=colors[7],
            foreground=colors[8],
            padding=0,
            fontsize=26
        ),
        widget.Backlight(
            foreground=colors[0],
            backlight_name="nvidia_wmi_ec_backlight",
            format="  {percent:2.0%}",
            margin_x=8,
            background=colors[8],
            # decorations=[
            #     BorderDecoration(
            #         border_width=[0, 0, 3, 0],
            #         colour=colors[8],
            #     )
            # ],
        ),
        # widget.Sep(linewidth=1, padding=5, foreground=colors[0]),
        widget.TextBox(
            text='',
            font="Iosevka Nerd Font",
            background=colors[8],
            foreground=colors[4],
            padding=0,
            fontsize=26
        ),
        widget.Clock(
            foreground=colors[0],
            # margin_x=20,
            format=" %H:%M  %d/%m",
            background=colors[4],
            # decorations=[
            #     BorderDecoration(
            #         border_width=[0, 0, 3, 0],
            #         colour=colors[4],
            #     )
            # ],
        ),
        widget.UPowerWidget(
            battery_height=15,
            battery_width=30,
            border_charge_colour=colors[0],
            fill_charge=colors[11],
            border_colour=colors[0],
            fill_normal=colors[11],
            border_critical_power=colors[0],
            fill_critical=colors[6],
            fill_low=colors[8],
            text_charging="({percentage:.0f}%) {ttf} until fully charged",
            text_discarging="({percentage:.0f}%)",
            margin=5,
            background=colors[4],
        ),
        widget.Systray(
            margin_x=15,
            padding_x=20,
            icon_size=20,
            background=colors[4],
        ),
    ]
    return widgets_list


widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen1(),
                size=30,
                opacity=1.0,
                background="#282828",
            )
        ),
    ]


screens = init_screens()


mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []


@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    d["1"] = ["Kitty", "kitty", "alacritty", "Alacritty"]
    d["2"] = ["Firefox", "firefox"]
    d["3"] = ["Pcmanfm", "pcmanfm", "Pcmanfm-qt", "pcmanfm-qt", "thunar", "Thunar"]
    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen()


main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="Arandr"),
        Match(wm_class="feh"),
        Match(wm_class="Galculator"),
        Match(title="branchdialog"),
        Match(title="Open File"),
        Match(title="pinentry"),
        Match(wm_class="ssh-askpass"),
        Match(wm_class="lxpolkit"),
        Match(wm_class="Lxpolkit"),
        Match(wm_class="yad"),
        Match(wm_class="Yad"),
        Match(wm_class="Cairo-dock"),
        Match(wm_class="cairo-dock"),
    ],
    fullscreen_border_width=0,
    border_width=0,
)
auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "Qtile"
