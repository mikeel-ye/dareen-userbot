from .adminHelpers import *
from .basic import *
from .constants import *
from .expand import *
#from .misc import *
from .interval import *
from .msg_types import *
from .parser import *
from .PyroHelpers import *
from .tools import *
from .utility import *


import os
import sys
from pyrogram import Client


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Uputt"])

async def join(client):
    try:
        await client.join_chat("jualankamii")
        await client.join_chat("dareensupport")
        await client.join_chat("skandallgua")
        await client.join_chat("mutualansilverswords")
        await client.join_chat("Uputtsupport")
        await client.join_chat("PesulapTelegram")
        await client.join_chat("jjdgank")
    except BaseException:
        pass
