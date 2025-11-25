#!/usr/bin/env python3
"""
Diagnostic script to test all components locally
Run this before deploying to Railway
"""
import os
import sys
from pathlib import Path

print("=" * 60)
print("🔮 TAROT BOT - DIAGNOSTIC CHECK")
print("=" * 60)

# Change to script directory
os.chdir(Path(__file__).parent)

# Set test environment variables
os.environ['TELEGRAM_BOT_TOKEN'] = '8551518470:AAG6AbFJwSwqphvIu_xIDHQ4N0v2eO3mEkg'
os.environ['OPENAI_API_KEY'] = 'sk-test-key'
os.environ['MONGO_URL'] = 'mongodb://localhost:27017'
os.environ['DB_NAME'] = 'tarot_bot'

errors = []

print("\n1️⃣ Testing Python version...")
print(f"   Python: {sys.version}")
if sys.version_info < (3, 8):
    errors.append("Python version too old (need 3.8+)")
else:
    print("   ✅ Python version OK")

print("\n2️⃣ Testing file structure...")
required_files = [
    'main.py',
    'channel_poster.py',
    'requirements.txt',
    'backend/__init__.py',
    'backend/config.py',
    'backend/database.py',
    'backend/ai/interpreter.py',
    'backend/tarot/cards.py',
    'data/tarot_cards.json'
]

for file in required_files:
    if Path(file).exists():
        print(f"   ✅ {file}")
    else:
        print(f"   ❌ {file} - MISSING!")
        errors.append(f"Missing file: {file}")

print("\n3️⃣ Testing imports...")
try:
    from backend.config import config
    print("   ✅ backend.config")
except Exception as e:
    print(f"   ❌ backend.config: {e}")
    errors.append(f"config import: {e}")

try:
    from backend.database import Database
    print("   ✅ backend.database")
except Exception as e:
    print(f"   ❌ backend.database: {e}")
    errors.append(f"database import: {e}")

try:
    from backend.tarot.cards import TarotDeck
    print("   ✅ backend.tarot.cards")
except Exception as e:
    print(f"   ❌ backend.tarot.cards: {e}")
    errors.append(f"tarot.cards import: {e}")

try:
    from backend.ai.interpreter import TarotInterpreter
    print("   ✅ backend.ai.interpreter")
except Exception as e:
    print(f"   ❌ backend.ai.interpreter: {e}")
    errors.append(f"ai.interpreter import: {e}")

print("\n4️⃣ Testing main.py...")
try:
    import main
    print("   ✅ main.py imports successfully")
except Exception as e:
    print(f"   ❌ main.py: {e}")
    errors.append(f"main.py import: {e}")

print("\n5️⃣ Testing channel_poster.py...")
try:
    import channel_poster
    print("   ✅ channel_poster.py imports successfully")
except Exception as e:
    print(f"   ❌ channel_poster.py: {e}")
    errors.append(f"channel_poster.py import: {e}")

print("\n6️⃣ Testing Tarot deck...")
try:
    from backend.tarot.cards import TarotDeck
    deck = TarotDeck()
    cards = deck.draw_cards(3)
    print(f"   ✅ Tarot deck loaded: {len(deck.cards)} cards")
    print(f"   ✅ Drew 3 cards successfully")
except Exception as e:
    print(f"   ❌ Tarot deck: {e}")
    errors.append(f"Tarot deck: {e}")

print("\n" + "=" * 60)
if errors:
    print("❌ DIAGNOSTIC FAILED - Issues found:")
    for i, error in enumerate(errors, 1):
        print(f"   {i}. {error}")
    print("\n⚠️  Fix these issues before deploying to Railway!")
    sys.exit(1)
else:
    print("✅ ALL CHECKS PASSED!")
    print("✅ Bot is ready for Railway deployment")
    print("=" * 60)
    sys.exit(0)
