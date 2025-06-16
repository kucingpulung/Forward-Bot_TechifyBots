#
import os
from config import Config

class Translation(object):
  START_TXT = """<b>Halo {}

Saya adalah bot penerus pesan canggih.
Saya bisa meneruskan semua pesan dari satu channel ke channel lainnya.

Klik tombol bantuan untuk mengetahui lebih lanjut tentang saya.</b>"""

  DONATE_TXT = """<b><i>Jika kamu menyukai saya ❤️, pertimbangkan untuk memberikan donasi untuk mendukung pengembang saya 👦

UPI ID - </i></b><code>TechifyBots@UPI</code>"""

  HELP_TXT = """<b><u>🔆 BANTUAN</b></u>

<u>**📚 Perintah yang Tersedia:**</u>

<b>⏣ __/start - Periksa apakah saya aktif__ 
⏣ __/forward - Teruskan pesan__
⏣ __/unequify - Hapus pesan duplikat di channel__
⏣ __/settings - Atur pengaturanmu__
⏣ __/reset - Atur ulang pengaturanmu__
⏣ __/donate - Donasi ke pengembang__
⏣ __/stop - Batalkan proses penerusan saat ini__</b>

<b><u>💢 Fitur:</b></u>
<b>► __Teruskan pesan dari channel publik ke channelmu tanpa perlu jadi admin (jika privat, butuh izin admin)__
► __Teruskan pesan dari channel privat ke channelmu dengan userbot (user harus menjadi anggota)__
► __Keterangan (caption) khusus__
► __Tombol khusus__
► __Dukungan untuk obrolan terbatas__
► __Lewati pesan duplikat__
► __Saring jenis pesan__
► __Lewati pesan berdasarkan ekstensi, kata kunci, dan ukuran__</b>
"""

  HOW_USE_TXT = """<b><u>⚠️ Sebelum Meneruskan:</b></u>
<b>► __Tambahkan bot atau userbot__
► __Tambahkan ke minimal satu channel__ `(bot/userbot kamu harus jadi admin di sana)`
► __Kamu bisa menambahkan chat atau bot lewat /settings__
► __Jika **Dari Channel** adalah privat, userbot kamu harus menjadi anggota atau bot kamu harus jadi admin di sana juga__
► __Kemudian gunakan /forward untuk mulai meneruskan pesan__</b>"""

  ABOUT_TXT = """<b>
╔════❰ BOT PENERUS ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃Bot : Bot Penerus
║┣⪼👦Pengembang : Rahul
║┣⪼📡Dihost di : Heroku
║┣⪼🗣️Bahasa : Python3
║┣⪼📚Library : Pyrogram
║┣⪼🗒️Versi : 1.0.6
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>"""

  STATUS_TXT = """<b>
╔════❰ STATUS BOT ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼👱 Total Pengguna : <code>{}</code>
║┃
║┣⪼🤖 Total Bot : <code>{}</code>
║┃
║┣⪼🔃 Proses Forward : <code>{}</code>
║┃
║┣⪼🔍 Penghapusan Duplikat: <code>0</code>
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>""" 

  SERVER_TXT = """<b>
╔════❰ STATUS SERVER ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ Total Ruang Disk: <code>38 GB</code>
║┣⪼ Terpakai: <code>1.54 GB</code>
║┣⪼ Tersisa: <code>36.46 GB</code>
║┣⪼ CPU: <code>{}%</code>
║┣⪼ RAM: <code>{}%</code>
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪</b>"""
  
  FROM_MSG = "<b>❪ PILIH CHAT SUMBER ❫\n\nTeruskan pesan terakhir atau link pesan terakhir dari chat sumber.\n/cancel - batalkan proses ini</b>"

  TO_MSG = "<b>❪ PILIH CHAT TUJUAN ❫\n\nPilih chat tujuanmu dari tombol yang tersedia.\n/cancel - batalkan proses ini</b>"

  SKIP_MSG = "<b><u>Tentukan jumlah pesan yang ingin dilewati 📃</u></b>\n\n<b>Kamu bisa melewati sejumlah pesan pertama dan meneruskan sisanya.\n\nDefault: 0</b>\n\n<b><i>Contoh: Jika kamu masukkan 0, semua pesan diteruskan.\nJika kamu masukkan 5, 5 pesan pertama akan dilewati.</i></b>\n/cancel <b>- batalkan proses ini</b>"

  CANCEL = "<b>Proses berhasil dibatalkan!</b>"

  BOT_DETAILS = "<b><u>📄 DETAIL BOT</b></u>\n\n<b>➣ NAMA:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"

  USER_DETAILS = "<b><u>📄 DETAIL USERBOT</b></u>\n\n<b>➣ NAMA:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"  

  TEXT = """<b>╔════❰ STATUS PENERUS ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼<b>𖨠 Total Pesan: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 Pesan Diambil: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 Pesan Diteruskan: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 Pesan Duplikat: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 Pesan Dihapus: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 Pesan Dilewati: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 Pesan Disaring: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 Status Saat Ini: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 Persentase: </b> <code>{}</code>%
║╰━━━━━━━━━━━━━━━➣ 
╚════❰ <b>{}</b> ❱══❍⊱❁"""

  DUPLICATE_TEXT = """
╔════❰ STATUS UNEQUIFY ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>File Diambil:</b> <code>{}</code>
║┃
║┣⪼ <b>Duplikat Dihapus:</b> <code>{}</code> 
║╰━━━━━━━━━━━━━━━➣
╚════❰ {} ❱══❍⊱❁۪۪
"""

  DOUBLE_CHECK = """<b><u>PEMERIKSAAN GANDA 📋</b></u>

<b>Sebelum meneruskan pesan, klik tombol YES hanya setelah memeriksa hal-hal berikut</b>

<b>★ Bot kamu: {botname}</b>
<b>★ Chat sumber: {from_chat}</b>
<b>★ Chat tujuan: {to_chat}</b>
<b>★ Pesan dilewati: {skip}</b>

<i><b>° {botname} harus menjadi admin di chat tujuan</i> ({to_chat})</b>
<i><b>° Jika chat sumber privat, userbot kamu harus menjadi anggota atau bot kamu harus menjadi admin juga</b></i>

<b>Jika semua di atas sudah diperiksa, kamu bisa klik tombol YES</b>"""
