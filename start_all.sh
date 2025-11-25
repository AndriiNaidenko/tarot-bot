#!/bin/bash
# Start both Tarot Bot and Channel Poster

echo "🔮 Starting Tarot Bot services..."

# Start main bot in background
echo "Starting main bot (@taro208_bot)..."
python -u main.py &
MAIN_PID=$!
echo "Main bot PID: $MAIN_PID"

# Start channel poster in background
echo "Starting channel poster (@taro209)..."
python -u channel_poster.py &
POSTER_PID=$!
echo "Channel poster PID: $POSTER_PID"

echo "✅ Both services started!"

# Wait for both processes
wait -n $MAIN_PID $POSTER_PID

# If one crashes, exit
echo "One of the services crashed, exiting..."
exit 1
