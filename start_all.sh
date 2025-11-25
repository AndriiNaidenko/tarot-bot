#!/bin/bash
# Start both Tarot Bot and Channel Poster with proper error handling

set -e  # Exit on error

echo "🔮 Starting Tarot Bot services..."

# Function to handle shutdown
cleanup() {
    echo "Shutting down services..."
    kill $MAIN_PID $POSTER_PID 2>/dev/null
    exit 0
}

trap cleanup SIGTERM SIGINT

# Start main bot in background
echo "Starting main bot (@taro208_bot)..."
python -u main.py 2>&1 | sed 's/^/[MAIN] /' &
MAIN_PID=$!
echo "Main bot started with PID: $MAIN_PID"

# Wait a bit for main bot to initialize
sleep 5

# Start channel poster in background
echo "Starting channel poster (@taro209)..."
python -u channel_poster.py 2>&1 | sed 's/^/[POSTER] /' &
POSTER_PID=$!
echo "Channel poster started with PID: $POSTER_PID"

echo "✅ Both services started!"
echo "Main bot PID: $MAIN_PID"
echo "Channel poster PID: $POSTER_PID"

# Monitor both processes
while true; do
    # Check if main bot is still running
    if ! kill -0 $MAIN_PID 2>/dev/null; then
        echo "❌ Main bot crashed! Restarting..."
        python -u main.py 2>&1 | sed 's/^/[MAIN] /' &
        MAIN_PID=$!
        echo "Main bot restarted with PID: $MAIN_PID"
    fi
    
    # Check if poster is still running
    if ! kill -0 $POSTER_PID 2>/dev/null; then
        echo "❌ Channel poster crashed! Restarting..."
        python -u channel_poster.py 2>&1 | sed 's/^/[POSTER] /' &
        POSTER_PID=$!
        echo "Channel poster restarted with PID: $POSTER_PID"
    fi
    
    sleep 30  # Check every 30 seconds
done
