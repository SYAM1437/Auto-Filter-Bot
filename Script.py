class script(object):

    START_TXT = """<b>👋 ʜᴇʏ {}, <i>{}</i>

✨ I’m a powerful Auto-Filter + Link Shortener Bot for your Telegram group.

➤ Instantly fetch and filter your movies or files.
➤ Attach your own link shortener & start earning!
➤ Just add me as an admin in your group and let me handle the rest. 🚀

♻️ Smart. Fast. Reliable.</b>"""

    MY_ABOUT_TXT = """<b>🔧 𝙰𝙱𝙾𝚄𝚃 𝙱𝙾𝚃</b>

★ ᴘʟᴀᴛꜰᴏʀᴍ : <a href='https://www.heroku.com'>Heroku</a>  
★ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href='https://www.mongodb.com'>MongoDB</a>  
★ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org'>Python</a>  
★ ꜱᴅᴋ/ʟɪʙʀᴀʀʏ : <a href='https://t.me/HydrogramNews'>Hydrogram</a>"""

    MY_OWNER_TXT = """<b>👑 𝙱𝙾𝚃 𝙾𝚆𝙽𝙴𝚁</b>

★ ɴᴀᴍᴇ : ᴴᴬ ᴮᵒᵗˢ  
★ ᴜꜱᴇʀɴᴀᴍᴇ :   @ANIMEUNIVERSETEUGU
★ ᴄᴏᴜɴᴛʀʏ : 🇱🇰 INDIA"""

    STATUS_TXT = """<b>📊 𝘽𝙊𝙏 𝙎𝙏𝘼𝙏𝙐𝙎</b>

👤 Total Users: <code>{}</code>  
😎 Premium Users: <code>{}</code>  
👥 Groups Using: <code>{}</code>  
📦 DB Usage: <code>{}</code>

🗂 1st DB Files: <code>{}</code>  
🧠 DB1 Used: <code>{}</code>

🗂 2nd DB Files: <code>{}</code>  
🧠 DB2 Used: <code>{}</code>

⚡ Uptime: <code>{}</code>"""

    NEW_GROUP_TXT = """#️⃣ <b>New Group Added</b>

🏷 Title: {}  
🆔 ID: <code>{}</code>  
🔗 Username: {}  
👥 Members: <code>{}</code>"""

    NEW_USER_TXT = """🆕 <b>New User Joined</b>

★ Name: {}  
★ ID: <code>{}</code>"""

    NOT_FILE_TXT = """❗ Hey {},  
I couldn’t find "<b>{}</b>" in my database. 😢

🔍 Please:
• Check your spelling  
• Use relevant keywords  
• Make sure it’s released"""

    EARN_TXT = """<b>💸 ᴇᴀʀɴ ᴡɪᴛʜ ʏᴏᴜʀ ʙᴏᴛ 💼</b>

1️⃣ Add me as admin in your group.  
2️⃣ Create an account on <a href='https://telegram.me/how_to_download_channel/14'>mdisklink.link</a> or any other shortener.  
3️⃣ Use the command below to connect:

<code>/set_shortlink mdisklink.link YOUR_API_KEY</code>

🎯 Earn per download using your shortener.  
✅ Free for everyone to use!</b>"""

    HOW_TXT = """<b>🔗 CONNECT YOUR SHORTENER</b>

📌 Format:  
<code>/set_shortlink shortener.site your_api_key</code>

📌 Example:  
<code>/set_shortlink mdisklink.link abc123xyz098apikey</code>

📎 To check your current shortener:  
<code>/get_shortlink</code>

❗ NOTE:  
Don't use this command as Anonymous Admin. Switch to normal mode to execute commands properly.</b>"""

    IMDB_TEMPLATE = """<b>🔎 I Found:</b> <code>{query}</code>

🎬 <b>Title:</b> <a href="{url}">{title}</a>  
🎭 <b>Genres:</b> {genres}  
📅 <b>Year:</b> <a href="{url}/releaseinfo">{year}</a>  
🌟 <b>Rating:</b> <a href="{url}/ratings">{rating} / 10</a>  
🗣 <b>Languages:</b> {languages}  
⏱ <b>Runtime:</b> {runtime} mins  

🧑 Requested by: {message.from_user.mention}  
📺 Powered by: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<i>{file_name}</i>\n\nJoin: https://t.me/ANIMEUNIVERSETEUGU"""

print("🚫 Please avoid resharing elsewhere") 
print("©️ ʙʏ ʏᴏᴜʀ ғᴀᴠ ʙᴏᴛ""" ")
