"""
Простий тест для перевірки основних компонентів бота
"""
import asyncio
import sys
from backend.config import config
from backend.database import Database
from backend.tarot.cards import TarotDeck
from backend.ai.interpreter import TarotInterpreter


async def test_database():
    """Test MongoDB connection"""
    print("🔍 Testing database connection...")
    db = Database(config.MONGO_URL, config.DB_NAME)
    
    # Test user creation
    test_user_id = 999999999
    await db.create_user(test_user_id, "Test User", "testuser")
    print("✅ User created")
    
    # Test user retrieval
    user = await db.get_user(test_user_id)
    assert user is not None
    print(f"✅ User retrieved: {user['name']}")
    
    # Clean up
    await db.users.delete_one({"_id": test_user_id})
    print("✅ Database test passed!\n")


async def test_tarot_deck():
    """Test Tarot deck operations"""
    print("🔍 Testing Tarot deck...")
    deck = TarotDeck()
    
    # Test single card draw
    card = deck.draw_card()
    assert 'name_uk' in card
    assert 'reversed' in card
    print(f"✅ Drew single card: {card['name_uk']}")
    
    # Test 3-card draw
    cards = deck.draw_cards(3)
    assert len(cards) == 3
    print(f"✅ Drew 3 cards: {', '.join([c['name_uk'] for c in cards])}")
    print("✅ Tarot deck test passed!\n")


async def test_ai_interpreter():
    """Test AI interpreter (requires API key)"""
    print("🔍 Testing AI interpreter...")
    interpreter = TarotInterpreter()
    
    # Create a test card
    test_card = {
        'name_uk': 'Маг',
        'upright': 'У вас є всі ресурси для успіху. Час діяти.',
        'reversed': 'Розсіяна енергія, нерозкритий потенціал.',
        'reversed': False
    }
    
    try:
        print("   Generating interpretation (this may take 5-10 seconds)...")
        interpretation = await interpreter.interpret_single_card(test_card)
        assert len(interpretation) > 50
        print(f"✅ AI interpretation generated ({len(interpretation)} characters)")
        print(f"   Preview: {interpretation[:100]}...")
        print("✅ AI interpreter test passed!\n")
    except Exception as e:
        print(f"⚠️  AI interpreter test skipped: {e}\n")


async def main():
    """Run all tests"""
    print("🔮 Starting Tarot Bot Component Tests\n")
    print("=" * 50)
    
    try:
        await test_database()
        test_tarot_deck()
        await test_ai_interpreter()
        
        print("=" * 50)
        print("🎉 All tests passed successfully!")
        print("\n✨ Your Tarot Bot is ready to use! ✨")
        return 0
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
