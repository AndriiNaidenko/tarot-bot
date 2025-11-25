#!/usr/bin/env python3
"""Simple healthcheck for Railway"""
import sys
import os

try:
    # Check required env vars
    required_vars = ['TELEGRAM_BOT_TOKEN']
    missing = [var for var in required_vars if not os.getenv(var)]
    
    if missing:
        print(f"❌ Missing env vars: {', '.join(missing)}")
        sys.exit(1)
    
    # Try importing main modules
    from backend.config import config
    from backend.database import Database
    
    print("✅ Healthcheck passed")
    sys.exit(0)
    
except Exception as e:
    print(f"❌ Healthcheck failed: {e}")
    sys.exit(1)
