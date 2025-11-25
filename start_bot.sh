#!/bin/bash
cd /app/tarot-bot
nohup python main.py > /tmp/tarot_bot.log 2>&1 &
echo "Tarot Bot started! PID: $!"
echo "Check logs: tail -f /tmp/tarot_bot.log"
