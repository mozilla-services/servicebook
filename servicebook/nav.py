from flask import g

from flask_nav import Nav, register_renderer
from flask_nav.elements import View, Navbar, Link
from flask_bootstrap.nav import BootstrapRenderer


class RightNavbar(Navbar):
    pass


# XXX todo: allow the addition of navbar-right ul/li groups
class CustomRenderer(BootstrapRenderer):
    pass


class MyNav(Nav):
    def init_app(self, app):
        register_renderer(app, None, CustomRenderer)
        super(MyNav, self).init_app(app)


def build_nav():
    user = g.user
    if user is None:
        link = Link('Github Login', '/login')
    else:
        link = Link('%s (logout)' % str(user), '/logout')

    return Navbar(View('Mozilla QA ~ Service Book', '.home'),
                  link)


nav = MyNav()
nav.register_element('frontend_top', build_nav)
