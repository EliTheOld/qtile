# from config import keys
from libqtile.command import lazy
from common import myTermMain
from libqtile import layout, hook, qtile
from libqtile.config import Key, Drag

mod = "mod4"
mod1 = "alt"
mod2 = "control"

keys = []
keys.extend(
    [
        Key([mod], "f", lazy.window.toggle_fullscreen()),
        Key([mod], "q", lazy.window.kill()),
        Key([mod], "t", lazy.spawn(myTermMain)),
        Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
        Key(
            [mod], "a", lazy.spawn("/home/wizard/.config/rofi/launchers/type-3/launcher.sh")
        ),
        Key(
            [mod],
            "x",
            lazy.spawn("/home/wizard/.config/rofi/powermenu/type-2/powermenu.sh"),
        ),
        Key([mod], "Escape", lazy.spawn("xkill")),
        Key([mod], "Return", lazy.spawn(myTermMain)),
        Key([mod], "KP_Enter", lazy.spawn(myTermMain)),
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
        Key([mod], "space",
            lazy.widget["keyboardlayout"].next_keyboard(),
            desc="Next keyboard layout."),
    ]
)
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
]
