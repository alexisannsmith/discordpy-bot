import discord
import asyncpraw
import random
import urllib.parse, urllib.request, re
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix = '!')

reddit = asyncpraw.Reddit(client_id = 'client_id', client_secret = 'client_secret', user_agent = 'user_agent')
    
@client.command()
async def meme(ctx):
    subreddit = await reddit.subreddit('dankmemes+memes+prequelmemes+animemes+bikinibottomtwitter')
    all_subs =  []
    hot = subreddit.hot(limit = 100)
    
    async for submission in hot:
        all_subs.append(submission)
    
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    
    em = discord.Embed(title = name)
    em.set_image(url = url)
    
    await ctx.send(embed=em)
    
@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    responses = ['Nah, fam.',
                 'Maybe someday.',
                 'Of course not.',
                 'Hell yeah!',
                 'Not on your life, lol.',
                 'Yeah, sure, why not.',
                 'Eh, probably.',
                 'Why don\'t you ask a real person?',
                 'Not if you don\'t try.',
                 'Yee...',
                 'Do white girls like pumpkin spice? Of course!',
                 'Maybe if Obama was still President.',
                 'Only if you beg me.',
                 'No hablo ingles.',
                 'Um.',
                 'Why did you just ask that? That\'s cringe, bro.',
                 'Do you like anime? If the answer is yes, then no.',
                 'You must sacrifice your grandma first.',
                 'Spin around 3 times and clap your hands. You will find what you seek',
                 'I can\'t bother with this question now. Try again later.'
                 ]
    await ctx.send(f'Question: {question}\nThe 8ball\'s wisdom: {random.choice(responses)}')
    
@client.command()
async def yt(ctx, *, search):
    query = urllib.parse.urlencode({'search_query': search})
    html_content = urllib.request.urlopen('https://www.youtube.com/results?' + query)
    results = re.findall(r'watch\?v=(\S{11})', html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v='+ results[0])
     
@client.event
async def on_ready():
    print('Ready!')
    
client.run('token')
