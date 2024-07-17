from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from modules import app_logger

logger = app_logger.get_logger(__name__)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! уже контейнер работает поинтрееснеее ')
    logger.warning(f"что то работает и даже логирует")

