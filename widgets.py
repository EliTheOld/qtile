import os
import socket
from colors import colors
from libqtile import widget, qtile
from libqtile.command import lazy
from qtile_extras import widget
from common import myTerm


def init_widgets_defaults():
    return dict(
        font="Fantasque Sans Mono Nerd Font",
        fontsize=20,
        padding=6,
        foreground=colors[2],
    )


def decor(fg="text", bg="text", text="text",):
    return {"foreground": fg, "background": bg,
        "font": "Iosevka Nerd Font", "padding": 0, "fontsize": 26, "text": text}


def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.GroupBox(
            background=colors[11],
            borderwidth=4,
            active=colors[4],
            inactive=colors[9],
            rounded=True,
            padding_y=0,
            highlight_method="text",
            urgent_alert_method="block",
            urgent_border=colors[3],
            this_current_screen_border=colors[7],
            this_screen_border=colors[7],
            other_current_screen_border=colors[6],
            other_screen_border=colors[9],
            disable_drag=True,
            fontsize=20,
        ),
        widget.TextBox(
            **decor(fg=colors[11], bg=colors[10], text="")
        ),
        widget.OpenWeather(
            location='Moscow',
            format='{location_city}: {icon} {main_temp}°{units_temperature}',
            background=colors[10],
        ),
        widget.TextBox(
            **decor(fg=colors[10], bg=colors[14], text="")
        ),
        widget.CurrentLayoutIcon(
            padding=0,
            scale=0.7,
            margin_x=10,
            background=colors[14],
        ),
        widget.CurrentLayout(
            background=colors[14],
        ),
        widget.TextBox(
            **decor(fg=colors[14], bg=colors[4], text="")
        ),
        widget.Prompt(
            background=colors[4],
            foreground=colors[0],
            cursor=True,
            padding_x=5,
            record_history=True,
        ),
        widget.TextBox(
            **decor(fg=colors[4], bg=colors[0], text="")
        ),
        widget.Spacer(),
        widget.TextBox(
            **decor(fg=colors[15], bg=colors[0], text="")
        ),
        widget.CheckUpdates(
            distro="Arch_checkupdates",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
            display_format=' Updates: {updates}',
            padding=4,
            update_interval=60,
            background=colors[15],
        ),
        widget.TextBox(
            **decor(fg=colors[5], bg=colors[15], text="")
        ),
        widget.KeyboardLayout(
            configured_keyboards=['us colemak', 'ru'],
            display_map={'us colemak': 'us', 'ru': 'ru'},
            background=colors[5],
        ),
        widget.TextBox(
            **decor(fg=colors[10], bg=colors[5], text="")
        ),
        widget.CPU(
            format=" {load_percent}%",
            update_interval=1,
            background=colors[10],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e gtop")},
        ),
        widget.TextBox(
            **decor(fg=colors[14], bg=colors[10], text="")
        ),
        widget.ThermalSensor(
            format=" {temp:.0f}{unit}",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e gotop")},
            background=colors[14],
        ),
        widget.TextBox(
            **decor(fg=colors[11], bg=colors[14], text="")
        ),
        widget.Memory(
            format="{MemUsed: .0f}M",
            update_interval=1,
            measure_mem="M",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e bpytop")},
            background=colors[11],
        ),
        widget.TextBox(
            **decor(fg=colors[10], bg=colors[11], text="")
        ),
        widget.PulseVolume(
            fmt="墳 {}",
            background=colors[10],
        ),
        widget.TextBox(
            **decor(fg=colors[14], bg=colors[10], text="")
        ),
        widget.Backlight(
            backlight_name="nvidia_wmi_ec_backlight",
            format="  {percent:2.0%}",
            margin_x=8,
            background=colors[14],
        ),
        widget.TextBox(
            **decor(fg=colors[0], bg=colors[14], text="")
        ),
        widget.Clock(
            format=" %H:%M  %d/%m",
            background=colors[0],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e calcurse")},
        ),
        widget.UPowerWidget(
            battery_height=15,
            battery_width=30,
            border_charge_colour=colors[2],
            fill_charge=colors[4],
            border_colour=colors[2],
            fill_normal=colors[12],
            border_critical_power=colors[2],
            fill_critical=colors[6],
            fill_low=colors[8],
            text_charging="({percentage:.0f}%) {ttf} until fully charged",
            text_discarging="({percentage:.0f}%)",
            margin=5,
            background=colors[0],
        ),
        widget.Systray(
            margin_x=15,
            padding_x=20,
            icon_size=20,
            background=colors[0],
        ),
        widget.Sep(linewidth=1, padding=5,
                   foreground=colors[0], colour=colors[0]),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


def init_layout_theme():
    return {
        "margin": 10,
        "border_width": 2,
        "border_focus": colors[12],
        "border_normal": colors[0],
    }


