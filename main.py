from telethon import TelegramClient, events


api_id = 28953352
api_hash = '1f918ea5cdb5d1e3e5e31d3be70d243b'
phone_number = '+79810397821'

client = TelegramClient('Telethon-Crypto', api_id, api_hash, system_version='4.16.30-vxCUSTOM', device_model='telethon-library')
client.start(phone_number)

specific_user_id = [5227666446, None, 6068731027]

@client.on(events.NewMessage(-1001757653881))
async def main(event):
    if event.message.sender_id in specific_user_id:
        await client.forward_messages(-1002103375046, event.message)

client.run_until_disconnected()