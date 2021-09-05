""" Module to automate message deletion. """
from asyncio import sleep
import time
import random
from time import strftime
from telethon.tl.functions.account import UpdateProfileRequest
from emoji import emojize
from pagermaid import bot, log
from pagermaid.listener import listener

auto_change_name_init = False
dizzy = emojize(":dizzy:", use_aliases=True)
cake = emojize(":cake:", use_aliases=True)
all_time_emoji_name = ["clock12", "clock1230", "clock1", "clock130", "clock2", "clock230", "clock3", "clock330",
                       "clock4", "clock430", "clock5", "clock530", "clock6", "clock630", "clock7", "clock730", "clock8",
                       "clock830", "clock9", "clock930", "clock10", "clock1030", "clock11", "clock1130"]
time_emoji_symb = [emojize(":%s:" % s, use_aliases=True) for s in all_time_emoji_name]


@listener(incoming=True, outgoing=True, ignore_edited=True)
async def change_name_auto(context):
    global auto_change_name_init
    if auto_change_name_init:
        return
    else:
        auto_change_name_init = True
    await log("开始每 30 秒更新一次 last_name")
    while True:
        try:
            time_cur = strftime("%H:%M:%S:%p:%a", time.localtime())
            hour, minu, seco, p, abbwn = time_cur.split(':')
            if seco == '00' or seco == '30':
                shift = 0
                if int(minu) > 30: shift = 1
                hsym = time_emoji_symb[(int(hour) % 12) * 2 + shift]
                    last_name = '%s时%s分 %s' % (hour, minu, hsym)
                await bot(UpdateProfileRequest(last_name=last_name))
        except:
            pass
        await sleep(1)
