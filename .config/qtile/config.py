import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

mod = "mod4"
terminal = "alacritty"
browser = "brave-browser"
filemanager = "pcmanfm"

default_border_width = 6
default_margin = 8
default_radius = 8

border_focus_color = colors[7]
border_normal_color = colors[0]

home = os.path.expanduser("~")

colors = [
    ["#1E1E2E", "#1E1E2E"],
    ["#45475a", "#45475a"],
    ["#9399b2", "#9399b2"],
    ["#CDD6F4", "#CDD6F4"],
    ["#F38BA8", "#F38BA8"],
    ["#A6E3A1", "#A6E3A1"],
    ["#FAB387", "#FAB387"],
    ["#89B4FA", "#89B4FA"],
    ["#cba6f7", "#cba6f7"],
    ["#89dceb", "#89dceb"],
    ["#B4BEFE", "#B4BEFE"],
    ["#00000000", "#00000000"],
    ["#313244", "#313244"],
]

decoration_group_black = {
    "decorations": [
        RectDecoration(
            colour=colors[12],
            radius=default_radius,
            filled=True,
            padding_y=0,
            group=True,
        )
    ],
    "padding": 10,
}

decoration_group_yellow = {
    "decorations": [
        RectDecoration(
            colour=colors[6],
            radius=default_radius,
            filled=True,
            padding_y=0,
            group=True,
        )
    ],
    "padding": 10,
}

decoration_group_blue = {
    "decorations": [
        RectDecoration(
            colour=colors[7],
            radius=default_radius,
            filled=True,
            padding_y=0,
            group=True,
        )
    ],
    "padding": 10,
}

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "s", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "t", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "n", lazy.layout.up(), desc="Move focus up"),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window",
    ),
    # Move windows between left/right columns or
    # move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "s",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "t", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "n", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the
    # edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "s", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "t", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "n", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "g", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggles the fullscreen state of the window",
    ),
    Key(
        [mod, "shift"],
        "f",
        lazy.window.toggle_floating(),
        desc="Toggles the floating state of the window",
    ),
    # Open Programs
    Key([mod], "b", lazy.spawn(browser), desc="Open Browser"),
    Key([mod, "shift"], "e", lazy.spawn(filemanager), desc="Open File Manager"),
    Key(
        [mod],
        "space",
        lazy.spawn([home + "/.config/rofi/scripts/launcher_t2"]),
        desc="Open Rofi",
    ),
    Key(
        [mod, "shift"],
        "p",
        lazy.spawn([home + "/.config/rofi/scripts/powermenu_t2"]),
        desc="Open Power Menu",
    ),
    # Emacs programs launched using the key chord Super + e followed by 'key'
    KeyChord(
        [mod],
        "e",
        [
            Key(
                [],
                "e",
                lazy.spawn("emacsclient -c -a 'emacs'"),
                desc="Emacsclient Dashboard",
            ),
            Key(
                [],
                "a",
                lazy.spawn(
                    "emacsclient -c -a 'emacs' --eval '(emms)' --eval '(emms-play-directory-tree \"~/Music/\")'"
                ),
                desc="Emacsclient EMMS (music)",
            ),
            Key(
                [],
                "b",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
                desc="Emacsclient Ibuffer",
            ),
            Key(
                [],
                "d",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
                desc="Emacsclient Dired",
            ),
            Key(
                [],
                "s",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
                desc="Emacsclient Eshell",
            ),
            Key(
                [],
                "v",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
                desc="Emacsclient Vterm",
            ),
            Key(
                [],
                "w",
                lazy.spawn(
                    "emacsclient -c -a 'emacs' --eval '(doom/window-maximize-buffer(eww \"distro.tube\"))'"
                ),
                desc="Emacsclient EWW Browser",
            ),
        ],
    ),
]

group_names = "WWW DEV SCHOOL MUS GFX".split()
groups = [
    Group(group_names[0], layout="max"),
    Group(group_names[1], layout="columns"),
    Group(group_names[2], layout="columns"),
    Group(group_names[3], layout="max"),
    Group(group_names[4], layout="colums"),
]

for i, name in enumerate(group_names):
    indx = str(i + 1)
    keys += [
        Key([mod], indx, lazy.group[name].toscreen()),
        Key([mod, "shift"], indx, lazy.window.togroup(name)),
    ]

layouts = [
    layout.Columns(
        border_focus_stack=border_focus_color,
        border_focus=border_focus_color,
        border_normal_stack=border_normal_color,
        border_normal=border_normal_color,
        border_on_single=True,
        margin=default_margin,
        border_width=default_border_width,
    ),
    layout.Max(
        border_focus=border_focus_color,
        border_normal=border_normal_color,
        border_width=default_border_width,
        margin=default_margin,
    ),
    layout.Floating(
        border_focus=border_focus_color,
        border_normal=border_normal_color,
        border_width=default_border_width,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(border_focus=colors[7],
    #           border_normal=colors[0],
    #           border_width=default_border_width,
    #           margin=default_margin, border_on_single=True),
    # layout.Spiral(border_focus=primary_color,
    #               border_normal=unfocused_border_color,
    #               border_width=default_border_width,
    #               margin=default_margin)
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(
    font="Ubuntu Nerd Font Bold",
    fontsize=12,
    padding=2,
    background=colors[11],
)


def no_text(text):
    return ""


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="\ueabc",
                    fontsize=26,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal)},
                    **decoration_group_black,
                ),
                widget.GroupBox(
                    fontsize=12,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=colors[3],
                    inactive=colors[2],
                    rounded=True,
                    highlight_color=colors[1],
                    highlight_method="text",
                    this_current_screen_border=colors[7],
                    this_screen_border=colors[4],
                    other_current_screen_border=colors[7],
                    other_screen_border=colors[4],
                    foreground=colors[0],
                    **decoration_group_black,
                ),
                widget.Sep(
                    linewidth=0,
                    **decoration_group_black,
                    foreground=colors[0],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=16,
                    foreground=colors[0],
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    foreground=colors[3],
                    scale=0.6,
                    **decoration_group_black,
                ),
                widget.CurrentLayout(foreground=colors[3], **decoration_group_black),
                widget.Sep(
                    linewidth=0, padding=6, foreground=colors[0], background=colors[11]
                ),
                widget.WindowName(
                    foreground=colors[12],
                    background=colors[11],
                ),
                widget.Systray(background=colors[11], padding=5),
                widget.Sep(
                    linewidth=0, padding=6, foreground=colors[0], background=colors[11]
                ),
                widget.Volume(
                    foreground=colors[7],
                    background=colors[11],
                    fmt="Vol {}",
                    padding=5,
                ),
                # widget.PulseVolume(
                #               foreground = colors[7],
                #                background = colors[11],
                #                emoji = True,
                #                limit_max_volume = True,
                #                padding = 5
                #              ),
                widget.Sep(
                    linewidth=0, padding=6, foreground=colors[0], background=colors[11]
                ),
                widget.Clock(
                    foreground=colors[3],
                    background=colors[11],
                    format="%H:%M | %d/%m/%Y",
                    **decoration_group_black,
                ),
                widget.Sep(
                    linewidth=0,
                    **decoration_group_black,
                    foreground=colors[3],
                    background=colors[11],
                ),
            ],
            24,
            margin=default_margin,
            background=colors[11],
        ),
    ),
]

# Drag floating layouts.
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
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + "/.config/qtile/autostart.sh"])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
