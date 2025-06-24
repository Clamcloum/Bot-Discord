import discord
from discord.ext import commands
from discord import app_commands
import asyncio
from ollama import *
import os
from dotenv import load_dotenv

TOKEN = os.getenv("TOKEN")
OLLAMA_MODEL = 'mistral-fr'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=r'/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def embed(ctx):
    """Demande un message à l'utilisateur, puis l'envoie dans un embed."""
    await ctx.send("📝 Quel message veux-tu embed ? Réponds dans les 30 secondes.")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        reply = await bot.wait_for("message", timeout=30.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("⏰ Temps écoulé ! Essaie à nouveau avec `!embed`.")
        return

    embed = discord.Embed(
        title="A l'attention de tous",
        description=reply.content,
        color=discord.Color.blurple()
    )
    embed.set_footer(text=f"Par {ctx.author.display_name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)

    await ctx.send(embed=embed)

@app_commands.describe(prompt="Ta question à Ollama")
@bot.command()
async def ask(ctx, *, prompt: str):
    await ctx.send("⏳ Je réfléchis...⏳")
    result = await asyncio.to_thread(interroger_ollama, prompt, OLLAMA_MODEL)
    await ctx.send(f"🧠 **Réponse** : {result}")

bot.run(TOKEN)