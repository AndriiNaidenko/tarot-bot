#!/bin/bash
# Start both Tarot Bot and Channel Poster with proper error handling

echo "🔮 Starting Tarot Bot services..."

# Function to handle shutdown
cleanup() {
    echo "Shutting down services..."
    kill -TERM $MAIN_PID $POSTER_PID 2>/dev/null || true
    wait $MAIN_PID $POSTER_PID 2>/dev/null || true
    echo "Services stopped"
    exit 0
}

trap cleanup SIGTERM SIGINT EXIT

# Start main bot in background with logging
echo "Starting main bot (@taro208_bot)..."
python -u main.py 2>&1 | while IFS= read -r line; do echo "[MAIN] $line"; done &
MAIN_PID=$!
echo "Main bot started with PID: $MAIN_PID"

# Wait a bit for main bot to initialize
sleep 5

# Start channel poster in background with logging
echo "Starting channel poster (@taro209)..."
python -u channel_poster.py 2>&1 | while IFS= read -r line; do echo "[POSTER] $line"; done &
POSTER_PID=$!
echo "Channel poster started with PID: $POSTER_PID"

echo "✅ Both services started!"
echo "Main bot PID: $MAIN_PID"
echo "Channel poster PID: $POSTER_PID"
echo "Monitoring processes..."

# Monitor both processes - restart if they crash
while true; do
    # Check if main bot is still running
    if ! kill -0 $MAIN_PID 2>/dev/null; then
        echo "❌ Main bot (PID $MAIN_PID) crashed! Restarting..."
        python -u main.py 2>&1 | while IFS= read -r line; do echo "[MAIN] $line"; done &
        MAIN_PID=$!
        echo "Main bot restarted with PID: $MAIN_PID"
    fi
    
    # Check if poster is still running
    if ! kill -0 $POSTER_PID 2>/dev/null; then
        echo "❌ Channel poster (PID $POSTER_PID) crashed! Restarting..."
        python -u channel_poster.py 2>&1 | while IFS= read -r line; do echo "[POSTER] $line"; done &
        POSTER_PID=$!
        echo "Channel poster restarted with PID: $POSTER_PID"
    fi
    
    sleep 60  # Check every minute
done
