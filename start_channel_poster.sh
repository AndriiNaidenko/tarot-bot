#!/bin/bash
cd /app/tarot-bot
nohup python channel_poster.py > /tmp/channel_poster.log 2>&1 &
echo "Channel Poster started! PID: $!"
echo "Check logs: tail -f /tmp/channel_poster.log"
