import discord
from bot_logic import gen_pass
from bot_logic import gen_emodji

with open("token.txt", "r") as f: # Membaca token dari file token.txt
    token = f.read() # Menyimpan token ke dalam variabel token

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$buat kata sandi'):
        await message.channel.send(gen_pass(5))
    elif message.content.startswith("$buat emotikon"):
        await message.channel.send(gen_emodji())
    else:
        await message.channel.send(message.content)

client.run(token)