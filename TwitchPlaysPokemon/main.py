# IMPORTS
from twitchio import Message
from twitchio.ext import commands
from dotenv import dotenv_values
from time import sleep
import requests
    
# LIST TO GRAB THE ENVIRONMENT VARIABLES
secrets = dotenv_values(".env")

# KEY BINDINGS FOR EASIER KEY ACCESS
KEY_BINDINGS={
    'START':'Start',
    
    'SELECT':'Select',
    
    'A':'A',
    
    'B':'B',
    
    'L':'L',
    
    'R':'R',
    
    'UP':'Up',
    
    'DOWN':'Down',
    
    'LEFT':'Left',
    
    'RIGHT':'Right'
}

# SIMULATING A KEYPRESS FOR mGBA THORUGH API
def press(key):
    
    requests.post(f"http://localhost:5000/mgba-http/button/tap?key={key}")

# MAIN CLASS
class Bot(commands.Bot):
    
    def __init__(self):
        
        super().__init__(token=secrets['ACCESS_TOKEN'], prefix='!', initial_channels=[secrets['INITIAL_CHANNEL']])
        
        self.game_start = False # FOR MANAGING THE START AND STOP COMMANDS
    
    async def event_ready(self): # WHEN BOT IS READY IT'LL PRINT THE USERNAME AND THE USER_ID IN THE CONSOLE
        
        print(f'Logged in as | {self.nick}')
        
        print(f'User id is | {self.user_id}')
    
    async def event_message(self, message: Message) -> None: # TO CAPTURE THE TWITCH CHAT
        
        if message.echo:
            return
        
        print(f"{message.author.name}: {message.content}")
        
        await self.handle_commands(message) # LETTING THE BOT KNOW THAT WE WANT OUR OWN COMMANDS


bot = Bot() # OBJECT OF THE CLASS

# COMMAND: STARTING THE GAME CONTROL
@bot.command(name='START_THE_GAME')
async def START_THE_GAME(ctx: commands.Context):
    
    t=10 # TIME TO START THE GAME CONTROL
    
    if ctx.author.name == secrets['USERNAME']: # THIS CHECKS IF THE COMMAND INITIATOR IS THE CHANNEL OWNER, OR NOT
        
        if bot.game_start == False:
        
            await ctx.send('[GAME MASTER]: GAME STARTING IN 10 SECONDS!\nPlayers! Get Ready.')
        
            sleep(1)
        
            while t: # COUNTS TO 10 BEFORE STARTING THE GAME CONTROLS
        
                _, secs = divmod(t, 60) 
        
                timer = '{:02d}'.format(secs) 
        
                await ctx.send(f'[GAME MASTER]: {timer}s left') 
        
                sleep(1) 
        
                t -= 1 
        
            await ctx.send('[GAME MASTER]: GAME STARTED!\nGood Luck Players!')
        
            bot.game_start = True # STARTING THE CONTROLLER
        
        else: 
            
            await ctx.send(f'[GAME MASTER]: Mr.{ctx.author.name}, GAME ALREADY STARTED!\nNo Need to Start It Again :)')
     else:

        await ctx.send(f'[GAME MASTER]: You don\'t have the permission to start the game.')

# COMMAND: STOPPING THE GAME CONTROL
@bot.command(name='STOP_THE_GAME')
async def STOP_THE_GAME(ctx: commands.Context):

    if ctx.author.name == secrets['USERNAME']: # THIS CHECKS IF THE COMMAND INITIATOR IS THE CHANNEL OWNER, OR NOT

        if bot.game_start:

            await ctx.send(f'[GAME MASTER]: GAME STOPPED BY Mr.{ctx.author.name}\nThanks for Playing with Us.\nWe Hope You Had Fun!')
            
            bot.game_start = False # IF VALIDATION IS CORRECT THEN STOP THE GAME CONTROL

        else:
            
            await ctx.send(f'[GAME MASTER]: GAME IS ALREADY STOPPED Mr.{ctx.author.name}')
     else:

        await ctx.send(f'[GAME MASTER]: You don\'t have the permission to stop the game.')
            

# COMMAND: mGBA-START BUTTON   
@bot.command(name='START')
async def START(ctx: commands.Context):
    if bot.game_start == True:
        press(KEY_BINDINGS['START'])

# COMMAND: mGBA-SELECT BUTTON
@bot.command(name='SELECT')
async def SELECT(ctx: commands.Context):
    if bot.game_start == True:
        press(KEY_BINDINGS['SELECT'])

# COMMAND: mGBA-A BUTTON
@bot.command(name='A')
async def A(ctx: commands.Context):
    if bot.game_start == True:
        press(KEY_BINDINGS['A'])

# COMMAND: mGBA-B BUTTON
@bot.command(name='B')
async def B(ctx: commands.Context):
    if bot.game_start == True:
        press(KEY_BINDINGS['B'])

# COMMAND: mGBA-L_TRIGGER BUTTON
@bot.command(name='L')
async def L(ctx: commands.Context):
    if bot.game_start == True:
        press(KEY_BINDINGS['L'])

# COMMAND: mGBA-R_TRIGGER BUTTON
@bot.command(name='R')
async def R(ctx: commands.Context):
    if bot.game_start == True:
        press(KEY_BINDINGS['R'])

# COMMAND: mGBA-UP BUTTON
@bot.command(name='UP')
async def UP(ctx: commands.Context):
    if bot.game_start == True:
        press(KEY_BINDINGS['UP'])

# COMMAND: mGBA-DOWN BUTTON
@bot.command(name='DOWN')
async def DOWN(ctx: commands.Context):
    if bot.game_start == True:
        press(KEY_BINDINGS['DOWN'])

# COMMAND: mGBA-LEFT BUTTON
@bot.command(name='LEFT')
async def LEFT(ctx: commands.Context):
    if bot.game_start == True:
        press(KEY_BINDINGS['LEFT'])

# COMMAND: mGBA-RIGHT BUTTON
@bot.command(name='RIGHT')
async def RIGHT(ctx: commands.Context):
    if bot.game_start == True:
        press(KEY_BINDINGS['RIGHT'])

# LET THE BOT RUN WILD!
bot.run()
