

import subprocess

import discord
import pyotp
import qrcode


from discord.ext import commands


addr = "MAC Address" # Enter your PC MAC Address here



def wol():
    subprocess.call(["wakeonlan", str(addr)], shell=False)  


    

secret_key = "" # define an random key here

uri = pyotp.totp.TOTP(secret_key).provisioning_uri(
    name='Discord Wake On Lan Bot',
    issuer_name='Discord Bot')

img = qrcode.make(uri) #after first run, you can delete these line
img.save('qrcode.png') #after first run, you can delete these line



totp = pyotp.TOTP(secret_key)





client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.command()
async def wake(ctx, message=None):
    if message and totp.verify(message):
        
        subprocess.call(["wakeonlan", str(addr)], shell=False)  # you need to sudo apt-get install wakeonlan on your raspberry pi / other

        await ctx.send('Magic Packet sent!')

    elif message:
        
        await ctx.send("Wrong code!")

    else:
        await ctx.send("You Forgot to enter the code!")



client.run('Token') # Enter your bot token here
