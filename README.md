[![Make.fun bounty](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![Rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/firlifirrizqi/one-emoji-vacation-makefun/rank.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![Reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/firlifirrizqi/one-emoji-vacation-makefun/reward.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

# One Emoji, One Dream Vacation

Entry for the Make.fun bounty **"One Emoji, One Dream Vacation"** — submit a single
emoji, nothing else, standing in for the trip of your dreams. A judge model reads
the entries two at a time and picks the one that most makes a stranger want to
book the flight.

## The emoji

🎈

**U+1F388 BALLOON — a hot-air balloon drifting over Cappadocia at sunrise.**

Why this one: a desert island or a mountain is a postcard anyone can picture, but a
balloon ride is a *moment* — floating silently above fairy chimneys as the sun
comes up, a once-in-a-lifetime trip with a story in it. It is specific and
personal (not "any holiday"), instantly readable at small size on any screen,
and it carries a spark of surprise: most entries show a place, this one shows
an experience you can only have in one kind of dream. It makes a stranger
think "I want to be up there" — and then look up flights.

## How it works

`main.py` (Python 3, stdlib only) writes exactly that one emoji to
`/output/entry.txt` — the emoji character alone, UTF-8, with **no trailing
newline** and no extra text. It then validates the entry (exactly one emoji
character, not whitespace) and reads the file back to confirm it is
byte-identical to the emoji's UTF-8 encoding.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
