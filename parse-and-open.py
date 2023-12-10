#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Parse and Open
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 🔍
# @raycast.packageName Developer Util

# Documentation:
# @raycast.author Joe Coll
# @raycast.authorURL https://github.com/0xOsprey

import re, webbrowser, pyperclip

regex_list = {
    "eth_address": {"regex": "^0x[a-fA-F0-9]{40}$", "url": "https://parsec.fi/address/{}"},
    "eth_txn": {"regex": "^0x([A-Fa-f0-9]{64})$", "url": "https://parsec.fi/eth/tx/{}"},
    "sol_address": {"regex": "(^[1-9A-HJ-NP-Za-km-z]{32,44}$)", "url": "https://xray.helius.xyz/account/{}"},
    "sol_txn": {"regex": "^[1-9A-Za-z]{128}$", "url": "https://xray.helius.xyz/tx/{}"},
    "twitter_handle": {"regex": "^@?(\w){1,15}$", "url": "https://twitter.com/{}"},
    "ipfs": {"regex": "^Qm[1-9A-Za-z]{44}$", "url": "https://ipfsexplorer.online/ipfs/{}"},
    "url": {"regex": "^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "url": "{}"}
}

#Main

#sys.exit(1)
if __name__ == "__main__":
    if pyperclip.paste() != "":
        for key in regex_list:
            if re.search(regex_list[key]["regex"], pyperclip.paste()):
                print("Opening {}".format(regex_list[key]["url"].format(pyperclip.paste())))
                webbrowser.open(regex_list[key]["url"].format(pyperclip.paste()))
                
                exit()
        print("Error: No match for {}".format(pyperclip.paste()))
    else:
        print("Error: Clipboard is empty")