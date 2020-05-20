# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        query = CMD_HELP.get(args)
        if query:
            string = (
                "**Query**:\n\n"
                f"    `{args}`\n\n"
            )
            if args == "anti_spambot":
                string += f"**Usage**:\n{query}"
            else:
                string += "**Command**:\n\n"
                for cmd, usage in query.items():
                    string += f">`{cmd}`\n"
                    string += f"**Usage**:\n{usage}\n\n"
        else:
            usage = None
            for module in CMD_HELP:
                for key, value in CMD_HELP.get(module).items():
                    if args == key:
                        usage = value
                        break
                if usage is not None:
                    string = (
                        "**Query**:\n\n"
                        f"    >`{args}`\n\n"
                        f"**Usage**:\n\n"
                        f"{usage}"
                    )
                    break
                else:
                    continue
            else:
                await event.edit(
                    f"`There is no command or module`:  **{args}**.")
                return False
        await event.edit(string)
    else:
        string = (
            "**Usage**:\n\n"
            "    >`.help` [module]\n\n"
            f"**Loaded Modules [{len(CMD_HELP)}]**:\n\n"
        )
        for key in CMD_HELP:
            string += (f"`{key}`    ")
        await event.edit(string)
