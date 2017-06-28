"""
Evennia settings file.

The available options are found in the default settings file found
here:

/home/coret/Desktop/mud-devel/evennia/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "MageMUD"

#SLOW EXITS#
#BASE_EXIT_TYPECLASS = "evennia.contrib.slow_exit.SlowExit"

MULTISESSION_MODE=0

######################################################################
# Django web features
######################################################################
INSTALLED_APPS += ('web.chargen',
		'web.character',
                'web.ff',)
DEBUG = True
# The secret key is randomly seeded upon creation. It is used to sign
# Django's cookies. Do not share this with anyone. Changing it will
# log out all active web browsing sessions. Game web client sessions
# may survive.
SECRET_KEY = 'Tg"%FpD1+Px_sy0eIobz*92H)S@,jOE6|R=Y;~Vc'

WEBSERVER_PORTS = [(80, 5001)]

######################################################################
# Contrib config
######################################################################

GAME_INDEX_LISTING = {
    'game_status': 'pre-alpha',
    # Optional, comment out or remove if N/A
    'game_website': 'http://www.streetwitch.com',
    'short_description': 'Graphical MUD based on Mage: the Ascension.',
    # Optional but highly recommended. Markdown is supported.
    'long_description': (
        "People have said that Mage: the Ascension could never be a MUD..<br><br>"
        "Let's prove them wrong!<br><br>The server is always open through the webclient. "
        "But we only role play when all our schedules are free.<br>"
        "Before you login, make a character with the web chargen: <a href=\"http://mud.streetwitch.com/chargen/\">http://www.streetwitch.com/chargen</a>"    
        "<br>Without the web client graphics will not be vissible, but you still can telnet into the game as usual."),
    'listing_contact': 'adventmagic@gmail.com',
    # At minimum, specify this or the web_client_url options. Both is fine, too.
    'telnet_hostname': 'mud.streetwitch.com',
    'telnet_port': 4000,
    # At minimum, specify this or the telnet_* options. Both is fine, too.
    'web_client_url': 'http://www.streetwitch.com/webclient',
}

