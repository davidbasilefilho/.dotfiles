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
    ["#1e1e2e", "#1e1e2e"],
    ["#00000000", "#00000000"], # Transparent
]

keys = [
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
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "s", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "t", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "n", lazy.layout.grow_up(), desc="Grow window up"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
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
        lazy.spawn([home + "/.config/rofi/scripts/launcher_t1"]),
        desc="Open Rofi",
    ),
    Key(
        [mod, "shift"],
        "p",
        lazy.spawn([home + "/.config/rofi/scripts/powermenu_t1"]),
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
            # Key(
            #     [],
            #     "s",
            #     lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
            #     desc="Emacsclient Eshell",
            # ),
            Key(
                [],
                "v",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
                desc="Emacsclient Vterm",
            ),
        ],
    ),
    KeyChord(
        [mod],
        "v",
        [
            Key(
                [],
                "-",
                lazy.spawn("amixer sset Master 10%-"),
                desc="Decrease volume by 10%",
            ),
            Key(
                [],
                "+",
                lazy.spawn("amixer sset Master 10%+"),
                desc="Increase volume by 10%",
            )
        ]
    )
]

group_names = "WWW DEV SCHOOL MUS GFX".split()
groups = [
    Group(group_names[0], layout="max"),
    Group(group_names[1], layout="columns"),
    Group(group_names[2], layout="columns"),
    Group(group_names[3], layout="max"),
    Group(group_names[4], layout="columns"),
]

for i, name in enumerate(group_names):
    indx = str(i + 1)
    keys += [
        Key([mod], indx, lazy.group[name].toscreen()),
        Key([mod, "shift"], indx, lazy.window.togroup(name)),
    ]

layout_theme = {
    "border_width": 4,
    "margin": 8,
    "border_focus": colors[7],
    "border_normal": colors[0]
}

layouts = [
    layout.Columns(
        **layout_theme,
        border_on_single = True
    ),
    layout.Max(
        **layout_theme
    ),
    layout.Floating(
        **layout_theme
    ),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(**layout_theme, border_on_single = True),
    # layout.Spiral(**layout_theme),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

decoration_radius = 4

decoration_group_black = {
    "decorations": [
        RectDecoration(
            colour=colors[11],
            radius=decoration_radius,
            filled=True,
            padding_y=0,
            group=True,
        )
    ],
    "padding": 6,
}

decoration_group_yellow = {
    "decorations": [
        RectDecoration(
            colour=colors[6],
            radius=decoration_radius,
            filled=True,
            padding_y=0,
            group=True,
        )
    ],
    "padding": 6,
}

decoration_group_blue = {
    "decorations": [
        RectDecoration(
            colour=colors[7],
            radius=decoration_radius,
            filled=True,
            padding_y=0,
            group=True,
        )
    ],
    "padding": 6,
}

widget_defaults = dict(
    font="Ubuntu Nerd Font Bold",
    fontsize=12,
    padding=2,
    background=colors[12],
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    background=colors[12],
                    **decoration_group_black,
                ),
                widget.GroupBox(
                    # fontsize=12,
                    margin_y=3,
                    background=colors[12],
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
                    background=colors[12],
                    **decoration_group_black,
                    foreground=colors[0],
                ),
                widget.Sep(
                    linewidth=0,
                    background=colors[12],
                    padding=16,
                    foreground=colors[0],
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    foreground=colors[3],
                    scale=0.7,
                    background=colors[12],
                    **decoration_group_black,
                ),
                widget.CurrentLayout(foreground=colors[3], **decoration_group_black, background=colors[12]),
                widget.Sep(
                    linewidth=0, padding=6, foreground=colors[0], background=colors[12]
                ),
                widget.WindowName(
                    foreground=colors[7], background=colors[12]
                ),
                widget.Systray(background=colors[7], **decoration_group_blue),
                widget.Sep(
                    linewidth=0, foreground=colors[0], background=colors[12]
                ),
                widget.Volume(
                    foreground=colors[7],
                    background=colors[12],
                    fmt="Vol: {}",
                    padding=5,
                ),
                # widget.PulseVolume(
                #               foreground = colors[7],
                #                emoji = True,
                #                limit_max_volume = True,
                #                padding = 5
                #              ),
                widget.Sep(
                    linewidth=0, padding=6, foreground=colors[0], background=colors[12]
                ),
                widget.Clock(
                    foreground=colors[3],
                    background=colors[12],
                    format="%H:%M | %d/%m/%Y",
                    **decoration_group_black,
                ),
                widget.Sep(
                    linewidth=0,
                    **decoration_group_black,
                    foreground=colors[3],
                    background=colors[12]
                ),
            ],
            24,
            margin=8,
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
        Match(title='Confirmation'),
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
