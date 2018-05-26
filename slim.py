import sublime
import sublime_plugin

view_settings = {}
window_settings = {}

def print_debug(msg):
    print(msg)

class UnfocusCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            ToggleViewCommand(self.view).unslim()
        except Exception as e:
            print_debug("got exception: {}".format(e))
        try:
            ToggleWindowCommand(self.view).unslim()
        except Exception as e:
            print_debug("got exception: {}".format(e))

class FocusCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ToggleViewCommand(self.view).slim()
        ToggleWindowCommand(self.view).slim()

class ToggleViewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.id() in view_settings and view_settings[self.view.id()]['slimmed']:
            print_debug('unslimming view {}'.format(self.view.id()))
            self.unslim()
        else:
            print_debug('slimming view {}'.format(self.view.id()))
            self.slim()

    def slim(self):
        if not self.view.id() in view_settings:
            print_debug('encountered new view {}'.format(self.view.id()))
            view_settings[self.view.id()] = {'slimmed': False}
        curr_settings = view_settings[self.view.id()]
        # if curr_settings['slimmed']:
        #     print_debug('view {} already slimmed, aborting'.format(self.view.id()))
        #     return

        self.view.settings().set('line_numbers', False)
        self.view.settings().set('gutter', False)
        curr_settings['slimmed'] = True

    def unslim(self):
        if not self.view.id() in view_settings:
            print_debug('encountered new view {}'.format(self.view.id()))
            view_settings[self.view.id()] = {'slimmed': False}
        curr_settings = view_settings[self.view.id()]
        # if curr_settings['slimmed']:
        #     print_debug('view {} already slimmed, aborting'.format(self.view.id()))
        #     return
        
        self.view.settings().set('line_numbers', True)
        self.view.settings().set('gutter', True)
        curr_settings['slimmed'] = False

class ToggleWindowCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.window().id() in window_settings and window_settings[self.view.window().id()]['slimmed']:
            print_debug('unslimming window {}'.format(self.view.window().id()))
            self.unslim()
        else:
            print_debug('slimming window {}'.format(self.view.window().id()))
            self.slim()

    def slim(self):
        if not self.view.window().id() in window_settings:
            print_debug('encountered new window {}'.format(self.view.window().id()))
            window_settings[self.view.window().id()] = {'slimmed': False}
        curr_settings = window_settings[self.view.window().id()]
        # if curr_settings['slimmed']:
        #     print_debug('window {} already slimmed, aborting'.format(self.view.window().id()))
        #     return

        self.view.window().set_menu_visible(False)
        # self.view.window().set_sidebar_visible(False)
        self.view.window().set_tabs_visible(False)
        self.view.window().set_status_bar_visible(False)
        self.view.window().set_minimap_visible(False)
        curr_settings['slimmed'] = True

    def unslim(self):
        if not self.view.window().id() in window_settings:
            print_debug('encountered new window {}'.format(self.view.window().id()))
            window_settings[self.view.window().id()] = {'slimmed': False}
        curr_settings = window_settings[self.view.window().id()]
        # if not curr_settings['slimmed']:
        #     print_debug('window {} already unslimmed, aborting'.format(self.view.window().id()))
        #     return

        self.view.window().set_menu_visible(True)
        # self.view.window().set_sidebar_visible(True)
        self.view.window().set_tabs_visible(True)
        self.view.window().set_status_bar_visible(True)
        self.view.window().set_minimap_visible(True)
        curr_settings['slimmed'] = False
