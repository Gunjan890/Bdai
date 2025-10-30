from L2RMUSIC.core.bot import Ashish
from L2RMUSIC.core.dir import dirr
from L2RMUSIC.core.git import git
from L2RMUSIC.core.userbot import Userbot
from L2RMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Ashish()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
