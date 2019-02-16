import sublime
import sublime_plugin

class UnfocusCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #print("edit is: {}".format(edit))
        unslim_view(self.view)
        unslim_window(self.view.window())

class FocusCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #print("edit is: {}".format(edit))
        slim_view(self.view)
        slim_window(self.view.window())

def slim_view(view):
    view.settings().set('line_numbers', False)
    view.settings().set('gutter', False)

def unslim_view(view):
    view.settings().set('line_numbers', True)
    view.settings().set('gutter', True)

def slim_window(window):
    window.set_menu_visible(False)
    # window.set_sidebar_visible(False)
    window.set_tabs_visible(False)
    window.set_status_bar_visible(False)
    window.set_minimap_visible(False)

def unslim_window(window):
    window.set_menu_visible(True)
    # window.set_sidebar_visible(True)
    window.set_tabs_visible(True)
    window.set_status_bar_visible(True)
    window.set_minimap_visible(True)
