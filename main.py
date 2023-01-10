import discord
from discord.ext import commands
import revChatGPT
import TTS
from revChatGPT.ChatGPT import Chatbot

client = commands.Bot(command_prefix='-', intents=discord.Intents.all())
chatbot = Chatbot({ "session_token": "CHATGPT_SESSION_TOKEN" })


@client.command()
async def ask(ctx, *, prompt):
  writing_message = await ctx.send("Writing...")
  response = chatbot.ask(prompt)
  message = response["message"]
  message_parts = [message[i:i+1900] for i in range(0, len(message), 1900)]
  # TTS not working yet
  if "tts_en" in ctx.message.content:
    audio_file = TTS.synthesize(text=message, voice="en")
    file = discord.File(audio_file, filename="message.wav")
    await ctx.send(file=file)
  else:
    for i, part in enumerate(message_parts):
      await ctx.send(part)
  await writing_message.delete()


client.run("DISCORD_BOT_TOKEN")
