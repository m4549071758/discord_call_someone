import discord
import random

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("logged in as " + client.user.name)
    print("------")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # Execure When Mentioned
    if client.user in message.mentions:
        role = message.guild.get_role() # roleID
        role_members = role.members

        selected_member = random.choice(role_members)
        selected_member_id = selected_member.id

        await message.channel.send(f"<@{selected_member_id}>さんが選択されました。")

client.run("YOUR_TOKEN")