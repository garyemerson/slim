import sublime
import sublime_plugin

view_settings = {}
window_settings = {}

def printd(msg):
    print(msg)

class ToggleFullCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.settings().set('line_numbers', True)
        self.view.settings().set('gutter', True)

        self.view.window().set_menu_visible(True)
        # self.view.window().set_sidebar_visible(True)
        self.view.window().set_tabs_visible(True)
        self.view.window().set_status_bar_visible(True)
        self.view.window().set_minimap_visible(True)

class FocusCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ToggleViewCommand(self.view).slim()
        ToggleWindowCommand(self.view).slim()

class ToggleViewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.id() in view_settings and view_settings[self.view.id()]['slimmed']:
            printd('unslimming view {}'.format(self.view.id()))
            self.unslim()
        else:
            printd('slimming view {}'.format(self.view.id()))
            self.slim()

    def slim(self):
        if not self.view.id() in view_settings:
            printd('encountered new view {}'.format(self.view.id()))
            view_settings[self.view.id()] = {'slimmed': False, 'line': None, 'gutter': None}
        curr_settings = view_settings[self.view.id()]
        if curr_settings['slimmed']:
            printd('view {} already slimmed, aborting'.format(self.view.id()))
            return

        curr_settings['line'] = self.view.settings().get('line_numbers')
        curr_settings['gutter'] = self.view.settings().get('gutter')
        self.view.settings().set('line_numbers', False)
        self.view.settings().set('gutter', False)
        curr_settings['slimmed'] = True

    def unslim(self):
        curr_settings = view_settings[self.view.id()]
        self.view.settings().set('line_numbers', curr_settings['line'])
        self.view.settings().set('gutter', curr_settings['gutter'])
        curr_settings['slimmed'] = False

class ToggleWindowCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.window().id() in window_settings and window_settings[self.view.window().id()]['slimmed']:
            printd('unslimming window {}'.format(self.view.window().id()))
            self.unslim()
        else:
            printd('slimming window {}'.format(self.view.window().id()))
            self.slim()

    def slim(self):
        if not self.view.window().id() in window_settings:
            printd('encountered new window {}'.format(self.view.window().id()))
            window_settings[self.view.window().id()] = {'slimmed': False, 'menu': None, 'sidebar': None, 'tabs': None, 'status': None, 'minimap': None}
        curr_settings = window_settings[self.view.window().id()]
        if curr_settings['slimmed']:
            printd('window {} already slimmed, aborting'.format(self.view.window().id()))
            return

        curr_settings['menu'] = self.view.window().is_menu_visible()
        curr_settings['sidebar'] = self.view.window().is_sidebar_visible()
        curr_settings['tabs'] = self.view.window().get_tabs_visible()
        curr_settings['status'] = self.view.window().is_status_bar_visible()
        curr_settings['minimap'] = self.view.window().is_minimap_visible()
        self.view.window().set_menu_visible(False)
        self.view.window().set_sidebar_visible(False)
        self.view.window().set_tabs_visible(False)
        self.view.window().set_status_bar_visible(False)
        self.view.window().set_minimap_visible(False)
        curr_settings['slimmed'] = True

    def unslim(self):
        curr_settings = window_settings[self.view.window().id()]
        self.view.window().set_menu_visible(curr_settings['menu'])
        self.view.window().set_sidebar_visible(curr_settings['sidebar'])
        self.view.window().set_tabs_visible(curr_settings['tabs'])
        self.view.window().set_status_bar_visible(curr_settings['status'])
        self.view.window().set_minimap_visible(curr_settings['minimap'])
        curr_settings['slimmed'] = False
