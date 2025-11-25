import asyncio
import logging
import sys
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from backend.config import config
from backend.database import Database
from backend.bot.handlers import start, readings

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


async def main():
    """Main bot entry point"""
    # Initialize bot and dispatcher
    bot = Bot(
        token=config.TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Initialize database
    db = Database(config.MONGO_URL, config.DB_NAME)
    
    # Register routers
    dp.include_router(start.router)
    dp.include_router(readings.router)
    
    # Middleware to pass database to handlers
    @dp.update.middleware()
    async def db_middleware(handler, event, data):
        data['db'] = db
        return await handler(event, data)
    
    logger.info("🔮 Tarot Bot starting...")
    logger.info(f"Connected to MongoDB: {config.DB_NAME}")
    
    try:
        # Start polling
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()
        logger.info("Bot stopped")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
