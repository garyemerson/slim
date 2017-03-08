import sublime
import sublime_plugin

view_settings = {}

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
        if self.view.id() in view_settings and view_settings[self.view.id()]["toggled"]:
            self.untoggle()
        else:
            self.toggle()

    def toggle(self):
        if not self.view.id() in view_settings:
            view_settings[self.view.id()] = {"toggled": False, "line": None, "gutter": None, "menu": None, "sidebar": None, "tabs": None, "status": None, "minimap": None}

        curr_view_settings = view_settings[self.view.id()]

        curr_view_settings["toggled"] = True
        curr_view_settings["line"] = self.view.settings().get("line_numbers")
        self.view.settings().set("line_numbers", False)
        curr_view_settings["gutter"] = self.view.settings().get("gutter")
        self.view.settings().set("gutter", False)

        curr_view_settings["menu"] = self.view.window().is_menu_visible()
        self.view.window().set_menu_visible(False)
        curr_view_settings["sidebar"] = self.view.window().is_sidebar_visible()
        self.view.window().set_sidebar_visible(False)
        curr_view_settings["tabs"] = self.view.window().get_tabs_visible()
        self.view.window().set_tabs_visible(False)
        curr_view_settings["status"] = self.view.window().is_status_bar_visible()
        self.view.window().set_status_bar_visible(False)
        curr_view_settings["minimap"] = self.view.window().is_minimap_visible()
        self.view.window().set_minimap_visible(False)

    def untoggle(self):
        curr_view_settings = view_settings[self.view.id()]
        self.view.settings().set("line_numbers", curr_view_settings["line"])
        self.view.settings().set("gutter", curr_view_settings["gutter"])

        self.view.window().set_menu_visible(curr_view_settings["menu"])
        self.view.window().set_sidebar_visible(curr_view_settings["sidebar"])
        self.view.window().set_tabs_visible(curr_view_settings["tabs"])
        self.view.window().set_status_bar_visible(curr_view_settings["status"])
        self.view.window().set_minimap_visible(curr_view_settings["minimap"])
        curr_view_settings["toggled"] = False
