#!/usr/bin/env python3
"""Minimal test to verify environment"""
import sys
import os

print("=" * 60)
print("MINIMAL ENVIRONMENT TEST")
print("=" * 60)

# Check Python version
print(f"\n✅ Python: {sys.version}")

# Check env vars
print("\n📋 Environment Variables:")
required = ['TELEGRAM_BOT_TOKEN', 'OPENAI_API_KEY', 'MONGO_URL', 'DB_NAME']
for var in required:
    value = os.getenv(var)
    if value:
        print(f"  ✅ {var}: {'*' * 10} (set)")
    else:
        print(f"  ❌ {var}: NOT SET")

# Try imports
print("\n📦 Testing imports:")
try:
    import aiogram
    print(f"  ✅ aiogram: {aiogram.__version__}")
except Exception as e:
    print(f"  ❌ aiogram: {e}")

try:
    import motor
    print(f"  ✅ motor: OK")
except Exception as e:
    print(f"  ❌ motor: {e}")

try:
    from backend.config import config
    print(f"  ✅ backend.config: OK")
    print(f"     - BOT_TOKEN: {'*' * 10}")
except Exception as e:
    print(f"  ❌ backend.config: {e}")

print("\n" + "=" * 60)
print("✅ TEST COMPLETE")
print("=" * 60)
