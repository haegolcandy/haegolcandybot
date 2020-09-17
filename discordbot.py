print("Hello World")
import discord
import os
import asyncio
import re
import random
from discord.utils import get
from discord.ext import commands
import pickle

app = commands.Bot(command_prefix='#')


token = "NzU0NTEyNzcwNDM4OTIyMjcx.X110xg.iO9xSKwD_2IaJdy5i-gThYdLN3c"
calcResult = 0

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("'#'명령어") #새로운 코드
    await app.change_presence(status=discord.Status.online, activity=game) #바뀜

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "#출력":
        await message.channel.send("Python Bot에 의해 출력됨.") #바뀜
    
    if message.content == "#레식":
        await message.channel.send("@everyone 레식할사람?")

    if message.content == "#무계급":
        await message.channel.send("@everyone 무계급할사람?")

    if message.content == "#랭크":
        await message.channel.send("@everyone 랭크할사람?")

    
    if message.content.startswith("#도움말"):
        embed=discord.Embed(title="__RAMI clan__", description="라미클랜", color=0x00ff56)
        embed.add_field(name="안녕하세요", value="처음오신 여러분들 만나서 반갑습니다.", inline=True)
        embed.add_field(name="기본적인 예의", value="경고3번째에 법정을 연 다음  그 결과에 따라 추방,서버 밴 둘다 먹여드립니다", inline=True)
        embed.add_field(name="어떤 클랜인가요?", value="빡겜할땐 빡겜 즐겜할땐 즐겜하는 클랜입니다", inline=True)
        embed.add_field(name="경고 기준", value="욕설,이유없이 게임던짐,질척거림,분위기 씹창내기", inline=True)
        await message.author.send(embed=embed)
        await message.channel.send("DM으로 도움말을 전송했어요")

    if message.content.startswith("#채팅청소"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[6:]
                await message.channel.purge(limit=int(amount))
                await message.channel.send(f"**{amount}**개의 메시지를 지웠습니다.")
            except ValueError:
                await message.channel.send("청소하실 메시지의 **수**를 입력해 주세요.")
        else:
            await message.channel.send("권한이 없습니다.")

    if(message.content.split(" ")[0] == "#킥"):
        if(message.author.guild_permissions.kick_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[25:]
                if(len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send(embed=discord.Embed(title="킥", description = f'당신은 {message.guild.name} 서버에서 킥당했습니다. 사유는 다음과 같습니다. ```{reason}```', color = 0xff0000))
                await user.kick(reason=reason)
                await message.channel.send(embed=discord.Embed(title="킥 성공", description = f"{message.author.mention} 님은 해당 서버에서 킥당하셨습니다. 사유:```{reason}```", color = 0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="에러 발생", description = str(e), color = 0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 유저를 킥할 수 있는 권한이 없습니다.", color = 0xff0000))
            return


    if message.content.startswith("#밴"):
        if message.author.guild_permissions.ban_members:
            userid = message.content[3:]
            user_id = re.findall("\d+", userid)
            userban = message.guild.get_member(int(user_id[0]))
            await message.guild.ban(userban)
            await message.channel.send(str(userban) + "님을 차단했습니다")
    
    if(message.content.split(" ")[0] == "#뮤트"):
        if(message.author.guild_permissions.manage_channels):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                await message.guild.get_channel(message.channel.category_id).set_permissions(user, send_messages=False)
                await message.channel.send(embed=discord.Embed(title="뮤트 성공!", color = 0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="에러 발생", description = str(e), color = 0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 채널을 관리 할 수 있는 권한이 없습니다.", color = 0xff0000))
            return

    
    if(message.content.split(" ")[0] == "#언뮤트"):
        if(message.author.guild_permissions.manage_channels):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                await message.guild.get_channel(message.channel.category_id).set_permissions(user, overwrite=None)
                await message.channel.send(embed=discord.Embed(title="언뮤트 성공!", color = 0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="에러 발생", description = str(e), color = 0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 채널을 관리 할 수 있는 권한이 없습니다.", color = 0xff0000))
            return
    
access_token = os.environ["BOT_TOKEN"]
app.run(access_token)
