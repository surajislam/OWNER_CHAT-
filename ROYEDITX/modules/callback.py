
from pyrogram.enums import ChatMemberStatus as CMS
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from ROYEDITX import LOCOPILOT, BOT_NAME
from ROYEDITX.database import vick
from ROYEDITX.modules.helpers import (
    CLOSE_BTN,
    BACK,
    CHATBOT_BACK,
    DEV_OP,
    HELP_BTN,
)


@LOCOPILOT.on_callback_query()
async def cb_handler(_, query: CallbackQuery):
    if query.data == "HELP":
        await query.message.edit_text(
            text=f"""❖ ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ꜰᴏʀ {BOT_NAME}\n\n⬤ /ping ➥ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ.\n⬤ /stats ➥ ᴄʜᴇᴄᴋ ᴍʏ ᴄʜᴀᴛs sᴛᴀᴛs.\n⬤ /chatbot ➥ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ [ᴡᴏʀᴋ ᴏɴʟʏ ɢʀᴏᴜᴘ]\n\n❖ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ➥ /""",
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
            disable_web_page_preview=True,
        )
    elif query.data == "CLOSE":
        await query.message.delete()
        await query.answer("❖ ᴄʟᴏsᴇᴅ ᴍᴇɴᴜ...", show_alert=True)
    elif query.data == "BACK":
        await query.message.edit(
            text=f"""❖ ʜᴇʏ ʙᴀʙʏ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ♥︎\n\n⬤ ɪ ᴀᴍ {BOT_NAME}, ᴀɪ ʙᴀsᴇ ᴄʜᴀᴛʙᴏᴛ.\n⬤ ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ғᴏʀ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ.\n\n❖ ᴛᴀᴘ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ sᴇᴇ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
    elif query.data == "🥳":
        await query.message.edit(
            text=f"""❖ ʜᴇʏ ʙᴀʙʏ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ♥︎\n\n⬤ ɪ ᴀᴍ {BOT_NAME},  ᴀɪ ʙᴀsᴇ ᴄʜᴀᴛʙᴏᴛ.\n\n❖ ɪғ ʏᴏᴜ ᴡᴀɴᴛ {BOT_NAME} ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ LAND ᴄᴏᴅᴇ.""",
            reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
            disable_web_page_preview=True,
        )
    elif query.data == "BACK_HELP":
        await query.message.edit(
            text=f"""❖ ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ꜰᴏʀ {BOT_NAME}\n\n⬤ /ping ➥ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ.\n⬤ /stats ➥ ᴄʜᴇᴄᴋ ᴍʏ ᴄʜᴀᴛs sᴛᴀᴛs.\n⬤ /chatbot ➥ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ [ᴡᴏʀᴋ ᴏɴʟʏ ɢʀᴏᴜᴘ]\n\n❖ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ➥ /""",
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
    elif query.data == "CHATBOT_BACK":
        await query.message.edit(
            text=f"""❖ ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ꜰᴏʀ {BOT_NAME}\n\n⬤ /ping ➥ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ.\n⬤ /stats ➥ ᴄʜᴇᴄᴋ ᴍʏ ᴄʜᴀᴛs sᴛᴀᴛs.\n⬤ /chatbot ➥ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ [ᴡᴏʀᴋ ᴏɴʟʏ ɢʀᴏᴜᴘ]\n\n❖ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ➥ /""",
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
    elif query.data == "addchat":
        user_id = query.from_user.id
        user_status = (await query.message.chat.get_member(user_id)).status
        if user_status not in [CMS.OWNER, CMS.ADMINISTRATOR]:
            return await query.answer(
                "❖ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴇᴠᴇɴ ᴀɴ ᴀᴅᴍɪɴ, ᴅᴏɴ'ᴛ ᴛʀʏ ᴛʜɪs ᴇxᴘʟᴏsɪᴠᴇ sʜɪᴛ !",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:
                await query.edit_message_text(f"❖ ᴄʜᴀᴛ-ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.")
            if is_vick:
                vick.delete_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(
                    f"❖ ᴄʜᴀᴛ-ʙᴏᴛ ᴇɴᴀʙʟᴇᴅ ʙʏ ➥ {query.from_user.mention}."
                )
    elif query.data == "rmchat":
        user_id = query.from_user.id
        user_status = (await query.message.chat.get_member(user_id)).status
        if user_status not in [CMS.OWNER, CMS.ADMINISTRATOR]:
            await query.answer(
                "❖ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴇᴠᴇɴ ᴀɴ ᴀᴅᴍɪɴ, ᴅᴏɴ'ᴛ ᴛʀʏ ᴛʜɪs ᴇxᴘʟᴏsɪᴠᴇ sʜɪᴛ !",
                show_alert=True,
            )
            return
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:
                vick.insert_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(
                    f"❖ ᴄʜᴀᴛ-ʙᴏᴛ ᴅɪsᴀʙʟᴇᴅ ʙʏ ➥ {query.from_user.mention}."
                )
            if is_vick:
                await query.edit_message_text("❖ ᴄʜᴀᴛ-ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.")

####



