# Base class for pages
class BasePage(object):

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        self.url = app.url
