import asyncio
from pyrogram import Client

print("""
Follow The Steps Below:

1. First go to my.telegram.org
2. Login using your Telegram account
3. Then click on API Development Tools
4. Create a new application, by entering the required details
5. Check your Telegram saved messages section to get your session
"""
)

async def main():
    api_id = int(input("ENTER API ID: "))
    api_hash = input("ENTER API HASH: ")
    async with Client("my_bot", api_id=api_id, api_hash=api_hash, in_memory=True) as app:
        await app.send_message(
            "me",
            "**Pyrogram Session String**:\n\n"
            f"`{await app.export_session_string()}`\n\n"
            "**Join @AsmSafone | @AsmSupport** 💕"
        )
        print(
            "Done, Your Pyrogram Session String Has Been Sent to Saved Messages of Your Telegram Account!"
        )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
