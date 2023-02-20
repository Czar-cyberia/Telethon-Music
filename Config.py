import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "10376773"))
    API_HASH = os.environ.get("API_HASH", "a230ffcf78ae0763748259371983135e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5132362444:AAE8iRnai1EPyUbZANyeC5jcRJie_awQFd4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu0Jz4htGZT8VKojaT6gKpzl4TGCk-oEm5a1LNeSDyJQrqQavCSSqG7vk7YGeeDNRN5MjntXK8cb7ofzpWDgOFs0tRRFhBb5ZI1_lCZhXCFU3KHiliBX6ewuPvqWn7fs11fqQXUrv3GlhHnBx6qadUtXGIshkNIyKc30rxK6rFVwLfFqdneRJ4RS3042swNiphkjW5Fga4L8RrRC2O6NqYPCT88acBKX6dtIfcsqTwKKZ4adFRIzXYlCVl7bjV1cYvnre4_tWduIX27mFDxqsMky3aO7t7RIT_0WvTX2BgRuiBI_mWzdQoS75-gaUlJVhYrt47R0KSidb_TuC7bbOMs8")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Group_song_robobot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5193860202")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', False) # Change it to "True"
