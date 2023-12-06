from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire ",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration ",
        callback_data="registration"
    )

    my_profile = InlineKeyboardButton(
        'My profile',
        callback_data='My profile'
    )
    random_profiles_button = InlineKeyboardButton(
        'View profile',
        callback_data='Random profiles'
    )
    reference_menu = InlineKeyboardMarkup(
        'reference menu',callback_data = 'reference menu'
    )
    anime_menu = InlineKeyboardMarkup(
        'animemenu',callback_data = 'anime menu'
    )
    markup.add(reference_menu)
    markup.add(random_profiles_button)
    markup.add(my_profile)
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(anime_menu)
    return markup


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()

    python_button = InlineKeyboardButton(

        "Python ",
        callback_data="python"
    )
    mojo_button = InlineKeyboardButton(
        "Mojo ",
        callback_data="mojo"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup

async def my_profile_keyboard():
    markup=InlineKeyboardMarkup
    update_button = InlineKeyboardButton(
        'Update',
        callback_data='update_profile'
    )

    delete_button = InlineKeyboardButton(
        'Delete',
        callback_data='Delete my profile'

    )
    markup.add(delete_button)
    markup.add(update_button)
    return markup



async def like_dislike_keyboard(owner_tg_id):
    markup=InlineKeyboardMarkup
    like_button = InlineKeyboardButton(
        'Like',
        callback_data=f'liked_profile{owner_tg_id}'
    )

    dislike_button = InlineKeyboardButton(
        'Dislike',
        callback_data='random_profiles'

    )
    markup.add(dislike_button)
    markup.add(like_button)
    return markup


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    reference_button = InlineKeyboardButton(
        "Reference Link 🔗",
        callback_data="reference_link"
    )
    markup.add(reference_button)
    return markup
