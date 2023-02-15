import os
import socket
import subprocess
from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import Drag, Group, Key, Match, Screen
from libqtile.command import lazy
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras import widget
from libqtile.bar import Bar
from libqtile.widget import Spacer

# mod4 or mod = super key
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


myTerm = "kitty"  # My terminal of choice

keys = [
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "t", lazy.spawn("kitty")),
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key([mod], "Escape", lazy.spawn("xkill")),
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod], "KP_Enter", lazy.spawn("kitty")),
    # Key([mod], "x", lazy.spawn(home + "/.config/rofi/bin/powermenu")),
    Key(
        [mod],
        "r",
        lazy.spawn(
            "dmenu_run -nb '#282828' -nf '#ebdbb2' -sb '#d65d0e' -sf '#282828' -fn 'Cozette-18'"
        ),
    ),
    Key([mod, "shift"], "Return", lazy.spawn("pcmanfm")),
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
    # CHANGE FOCUS
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
    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),
    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    # Treetab controls
    Key(
        [mod, "control"],
        "k",
        lazy.layout.section_up(),
        desc="Move up a section in treetab",
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.section_down(),
        desc="Move down a section in treetab",
    ),
    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
]

groups = []

# FOR QWERTY KEYBOARDS
group_names = [
    "1",
    "2",
    "3",
    "4",
    "5",
]

group_labels = [
    "",
    "",
    "",
    "",
    "",
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
            # CHANGE WORKSPACES
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
            Key(["mod1"], "Tab", lazy.screen.next_group()),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
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
        "margin": 8,
        "border_width": 0,
        "border_focus": "#cba6f7",
        "border_normal": "#b4befe",
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

# COLORS FOR THE BAR


def init_colors():
    return [
        ["#282828", "#282828"],  # color 0 bg
        ["#1d2021", "#1d2021"],  # color 1 black
        ["#ebdbb2", "#ebdbb2"],  # color 2 fg white
        ["#cc241d", "#cc241d"],  # color 3 red
        ["#98971a", "#98971a"],  # color 4 green
        ["#458588", "#548588"],  # color 5 blue
        ["#d65d0e", "#d65d0e"],  # color 6 orange
        ["#b16286", "#b16286"],  # color 7 pink
        ["#d79921", "#d79921"],  # color 8 yellow
        ["#bdae93", "#bdae93"],  # color 9 cream
        ["#504945", "#504935"],  # color 10 medgrey
        ["#b0b5bd", "#b0b5bd"],  # color 11 grey
    ]


colors = init_colors()


def base(fg="text", bg="dark"):
    return {"foreground": colors[2], "background": colors[0]}


# WIDGETS FOR THE BAR


def init_widgets_defaults():
    return dict(
        font="Cozette",
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
            font="Cozette",
            fontsize=20,
            borderwidth=4,
            active=colors[4],
            inactive=colors[2],
            rounded=True,
            highlight_method="line",
            urgent_alert_method="block",
            urgent_border=colors[3],
            this_current_screen_border=colors[6],
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
            # custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
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
        # widget.Net(
        #     # Here enter your network name
        #     interface=["wlan0"],
        #     format="{down} ↓↑{up} ",
        #     foreground=colors[2],
        #     adding=0,
        #     decorations=[
        #         BorderDecoration(
        #             border_width=[0, 0, 3, 0],
        #             colour=colors[5],
        #         )
        #     ],
        # ),
        # widget.Sep(linewidth=1, padding=5, foreground=colors[0]),
        widget.CPU(
            format=" {load_percent}%",
            update_interval=1,
            foreground=colors[2],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e htop")},
            decorations=[
                BorderDecoration(
                    border_width=[0, 0, 3, 0],
                    colour=colors[3],
                )
            ],
        ),
        widget.ThermalSensor(
            foreground=colors[2],
            format=" {temp:.0f}{unit}",
            decorations=[
                BorderDecoration(
                    border_width=[0, 0, 3, 0],
                    colour=colors[3],
                )
            ],

        ),
        widget.Sep(linewidth=1, padding=5, foreground=colors[0]),
        widget.Memory(
            format="{MemUsed: .0f}M",
            update_interval=1,
            measure_mem="M",
            foreground=colors[2],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e htop")},
            decorations=[
                BorderDecoration(
                    border_width=[0, 0, 3, 0],
                    colour=colors[6],
                )
            ],
        ),
        widget.Sep(linewidth=1, padding=5, foreground=colors[0]),
        widget.PulseVolume(
            fmt="墳 {}",
            foreground=colors[2],
            decorations=[
                BorderDecoration(
                    border_width=[0, 0, 3, 0],
                    colour=colors[7],
                )
            ],
        ),
        widget.Sep(linewidth=1, padding=5, foreground=colors[0]),
        widget.Backlight(
            foreground=colors[2],
            backlight_name="nvidia_wmi_ec_backlight",
            format=" {percent:2.0%}",
            margin_x=8,
            decorations=[
                BorderDecoration(
                    border_width=[0, 0, 3, 0],
                    colour=colors[8],
                )
            ],
        ),
        widget.Sep(linewidth=1, padding=5, foreground=colors[0]),
        widget.Clock(
            foreground=colors[2],
            # margin_x=20,
            format=" %H:%M  %d/%m",
            decorations=[
                BorderDecoration(
                    border_width=[0, 0, 3, 0],
                    colour=colors[4],
                )
            ],
        ),
        widget.Sep(linewidth=1, padding=5, foreground=colors[0]),
        widget.UPowerWidget(
            battery_height=15,
            battery_width=30,
            border_charge_colour=colors[8],
            fill_charge=colors[4],
            border_colour=colors[8],
            fill_normal=colors[4],
            border_critical_power=colors[8],
            fill_critical=colors[6],
            fill_low=colors[8],
            text_charging="({percentage:.0f}%) {ttf} until fully charged",
            text_discarging="({percentage:.0f}%)",
            margin=5,
        ),
        widget.Systray(
            margin_x=5,
            padding_x=10,
            icon_size=20,
        ),
        widget.Sep(linewidth=1, padding=10, foreground=colors[0]),
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


# MOUSE CONFIGURATION
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

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN
@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    d["1"] = ["Kitty", "kitty"]
    d["2"] = ["Firefox", "firefox"]
    d["3"] = ["Pcmanfm", "pcmanfm", "Pcmanfm-qt", "pcmanfm-qt"]
##########################################################
    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen()

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME


main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
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
