from STRABERRY.core.bot import RAJ
from STRABERRY.core.dir import dirr
from STRABERRY.core.git import git
from STRABERRY.core.userbot import Userbot
from STRABERRY.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = RAJ()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
