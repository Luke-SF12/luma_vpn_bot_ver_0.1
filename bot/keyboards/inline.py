from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
def inline_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🛒 Купить", callback_data="buy")],
            [InlineKeyboardButton(text="👤 Профиль", callback_data="profile")],
            [InlineKeyboardButton(text="📖 Инструкция", callback_data="instruction")],
            [InlineKeyboardButton(text="🛠 Техподдержка", callback_data="support")],
        ]
    )

# Клавиатура для выбора тарифа
def subscription_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1 месяц – 129₽", callback_data="buy_1m")],
            [InlineKeyboardButton(text="3 месяца – 369₽", callback_data="buy_3m")],
            [InlineKeyboardButton(text="6 месяцев – 699₽", callback_data="buy_6m")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")],
        ]
    )

# Клавиатура для профиля
def profile_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")],
        ]
    )

# Клавиатура для инструкции
def instruction_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="iOS", callback_data="instruction_ios")],
            [InlineKeyboardButton(text="Android", callback_data="instruction_android")],
            [InlineKeyboardButton(text="Windows", callback_data="instruction_windows")],
            [InlineKeyboardButton(text="MacOS", callback_data="instruction_macos")],
            [InlineKeyboardButton(text="Android TV", callback_data="instruction_tv")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")],
        ]
    )

# Клавиатура для техподдержки
def support_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")],
        ]
    )
