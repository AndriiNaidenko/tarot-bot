#!/usr/bin/env python3
"""Test script to verify all imports work correctly"""
import sys
import os

print("=" * 60)
print("TESTING TAROT BOT IMPORTS")
print("=" * 60)

# Set minimal env vars for testing
os.environ['TELEGRAM_BOT_TOKEN'] = 'test_token'

errors = []

print("\n1. Testing backend.config...")
try:
    from backend.config import config
    print("   ✅ backend.config OK")
except Exception as e:
    print(f"   ❌ backend.config FAILED: {e}")
    errors.append(f"config: {e}")

print("\n2. Testing backend.database...")
try:
    from backend.database import Database
    print("   ✅ backend.database OK")
except Exception as e:
    print(f"   ❌ backend.database FAILED: {e}")
    errors.append(f"database: {e}")

print("\n3. Testing backend.tarot.cards...")
try:
    from backend.tarot.cards import TarotDeck
    print("   ✅ backend.tarot.cards OK")
except Exception as e:
    print(f"   ❌ backend.tarot.cards FAILED: {e}")
    errors.append(f"tarot.cards: {e}")

print("\n4. Testing backend.ai.interpreter...")
try:
    from backend.ai.interpreter import TarotInterpreter
    print("   ✅ backend.ai.interpreter OK")
except Exception as e:
    print(f"   ❌ backend.ai.interpreter FAILED: {e}")
    errors.append(f"ai.interpreter: {e}")

print("\n5. Testing backend.bot.handlers...")
try:
    from backend.bot.handlers import start, readings
    print("   ✅ backend.bot.handlers OK")
except Exception as e:
    print(f"   ❌ backend.bot.handlers FAILED: {e}")
    errors.append(f"bot.handlers: {e}")

print("\n6. Testing backend.channel modules...")
try:
    from backend.channel.news_fetcher import NewsFetcher
    from backend.channel.post_generator import PostGenerator
    print("   ✅ backend.channel OK")
except Exception as e:
    print(f"   ❌ backend.channel FAILED: {e}")
    errors.append(f"channel: {e}")

print("\n7. Testing main.py...")
try:
    import main
    print("   ✅ main.py OK")
except Exception as e:
    print(f"   ❌ main.py FAILED: {e}")
    errors.append(f"main: {e}")

print("\n8. Testing channel_poster.py...")
try:
    import channel_poster
    print("   ✅ channel_poster.py OK")
except Exception as e:
    print(f"   ❌ channel_poster.py FAILED: {e}")
    errors.append(f"channel_poster: {e}")

print("\n" + "=" * 60)
if errors:
    print("❌ FAILED - Errors found:")
    for error in errors:
        print(f"   - {error}")
    sys.exit(1)
else:
    print("✅ ALL IMPORTS SUCCESSFUL!")
    print("=" * 60)
    sys.exit(0)
