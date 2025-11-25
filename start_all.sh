#!/bin/bash
# Start both Tarot Bot and Channel Poster

echo "🔮 Starting Tarot Bot services..."

# Start main bot in background
echo "Starting main bot (@taro208_bot)..."
python main.py &
MAIN_PID=$!
echo "Main bot started with PID: $MAIN_PID"

# Wait a bit for main bot to initialize
sleep 5

# Start channel poster in background
echo "Starting channel poster (@taro209)..."
python channel_poster.py &
POSTER_PID=$!
echo "Channel poster started with PID: $POSTER_PID"

echo "✅ Both services started!"
echo "Main bot PID: $MAIN_PID"
echo "Channel poster PID: $POSTER_PID"

# Wait for both processes
wait $MAIN_PID $POSTER_PID
