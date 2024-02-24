import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def mem(ctx):
    with open('images/memlol1.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def map(ctx):
    await ctx.send(f'Переходи на эту ссылку, чтобы найти локации, где можно сдать мусор который вы собрали. Ссылка: https://recyclemap.ru')

@bot.command()
async def daily_mission(ctx):
    await ctx.send(f'Твоя сегодняшняя миссия это: Сдай мусор на 5 разных локациях. Награда: +5 баллов')

@bot.command()
async def daily_mission_done(ctx):
    await ctx.send(f'Вы успешно выполнили это задание! У вас было прибавлено 5 баллов. Не забуть сделать тоже самое завтра!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTIwMTA2Nzc0NjM3NzU5Njk1MA.GsiaxH.h9xUD30ggQ0NHICeGyAVp0kEQgtkPrKtpUH56g")