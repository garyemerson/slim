import sublime
import sublime_plugin

toggled = False
line = None
gutter = None
menu = None
sidebar = None
tabs = None
status = None
minimap = None

class barCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.settings().set("line_numbers", True)
        self.view.settings().set("gutter", True)

        self.view.window().set_menu_visible(True)
        # self.view.window().set_sidebar_visible(True)
        self.view.window().set_tabs_visible(True)
        self.view.window().set_status_bar_visible(True)
        self.view.window().set_minimap_visible(True)

class fooCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global toggled
        if toggled:
            self.untoggle()
            toggled = False
        else:
            self.toggle()
            toggled = True

    def toggle(self):
        global line
        global gutter
        global menu
        global sidebar
        global tabs
        global status
        global status
        global minimap

        line = self.view.settings().get("line_numbers")
        self.view.settings().set("line_numbers", False)
        gutter = self.view.settings().get("gutter")
        self.view.settings().set("gutter", False)

        menu = self.view.window().is_menu_visible()
        self.view.window().set_menu_visible(False)
        sidebar = self.view.window().is_sidebar_visible()
        self.view.window().set_sidebar_visible(False)
        tabs = self.view.window().get_tabs_visible()
        self.view.window().set_tabs_visible(False)
        status = self.view.window().is_status_bar_visible()
        self.view.window().set_status_bar_visible(False)
        minimap = self.view.window().is_minimap_visible()
        self.view.window().set_minimap_visible(False)

    def untoggle(self):
        global line
        global gutter
        global menu
        global sidebar
        global tabs
        global status
        global status
        global minimap

        self.view.settings().set("line_numbers", line)
        self.view.settings().set("gutter", gutter)

        self.view.window().set_menu_visible(menu)
        self.view.window().set_sidebar_visible(sidebar)
        self.view.window().set_tabs_visible(tabs)
        self.view.window().set_status_bar_visible(status)
        self.view.window().set_minimap_visible(minimap)
