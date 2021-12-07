import discord
from discord.ext import commands

game = discord.Game("따까리들을 감시")
bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity = game)
client = discord.Client()
print(len(client.guilds))
@bot.command(aliases = ['안녕하세요'])
async def 안녕(ctx):
    file = discord.File("주먹.png")
    await ctx.send(file=file)
    await ctx.send('명령하지 마라')
@bot.command()
async def 도움(ctx):
    file = discord.File("엿.jpg")
    await ctx.send(file=file)
    await ctx.send('나약한 자에게 줄 도움은 없다')
@bot.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.endswith("함"):
        file = discord.File("pic\함.jpg")
        await message.channel.send(file=file)
        await message.channel.send("그런 함은 침몰했습니다")
    if message.content.endswith("엄"):
        file = discord.File("pic\엄준식.gif")
        await message.channel.send(file=file)
        await message.channel.send("엄준식라이더")
    if message.content.endswith("가"):
        file = discord.File("pic\가면라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("가면라이더")
    if message.content.endswith("두"):
        file = discord.File("pic\두리안.jpg")
        await message.channel.send(file=file)
        await message.channel.send("두리안라이더")
    if message.content.endswith("딱"):
        file = discord.File("pic\딱지.jpg")
        await message.channel.send(file=file)
        await message.channel.send("딱지라이더")
    if message.content.endswith("바"):
        file = discord.File("pic\바이올린.jpg")
        await message.channel.send(file=file)
        await message.channel.send("바이올린라이더")
    if message.content.endswith("빨"):
        file = discord.File("pic\빨래.gif")
        await message.channel.send(file=file)
        await message.channel.send("빨래라이더")
    if message.content.endswith("자"):
        file = discord.File("pic\자전거.jpg")
        await message.channel.send(file=file)
        await message.channel.send("자전거라이더")
    if message.content.endswith("전"):
        file = discord.File("pic\전기톱.jpg")
        await message.channel.send(file=file)
        await message.channel.send("전기톱라이더")
    if message.content.endswith("좀"):
        file = discord.File("pic\좀비.jpg")
        await message.channel.send(file=file)
        await message.channel.send("좀비라이더")
    if message.content.endswith("중"):
        file = discord.File("pic\중력.jpg")
        await message.channel.send(file=file)
        await message.channel.send("중력라이더")
    if message.content.endswith("지"):
        file = discord.File("pic\지나가던.jpg")
        await message.channel.send(file=file)
        await message.channel.send("지나가던라이더")
    if message.content.endswith("카"):
        file = discord.File("pic\카베동.jpg")
        await message.channel.send(file=file)
        await message.channel.send("카베동라이더")
    if message.content.endswith("트"):
        file = discord.File("pic\트럼펫.jpg")
        await message.channel.send(file=file)
        await message.channel.send("트럼펫라이더")
    if message.content.endswith("하"):
        file = discord.File("pic\하이킥.jpg")
        await message.channel.send(file=file)
        await message.channel.send("하이킥라이더")
    if message.content.endswith("히"):
        file = discord.File("pic\히틀러라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("히틀러라이더")
    if message.content.endswith("신"):
        file = discord.File("pic\신호등.jpg")
        await message.channel.send(file=file)
        await message.channel.send("신호등라이더")
    if message.content.endswith("고"):
        file = discord.File("pic\고자.jpg")
        await message.channel.send(file=file)
        await message.channel.send("고자라이더")
    if message.content.endswith("야"):
        file = discord.File("pic\야구.gif")
        await message.channel.send(file=file)
        await message.channel.send("야구라이더")
    if message.content.endswith("라"):
        file = discord.File("pic\라디오.jpg")
        await message.channel.send(file=file)
        await message.channel.send("라디오라이더")
    if message.content.endswith("도"):
        file = discord.File("pic\도둑.jpg")
        await message.channel.send(file=file)
        await message.channel.send("도둑라이더")
    if message.content.endswith("요"):
        file = discord.File("pic\요리사.gif")
        await message.channel.send(file=file)
        await message.channel.send("요리사라이더")
    if message.content.endswith("냐"):
        file = discord.File("pic\야옹이.jpg")
        await message.channel.send(file=file)
        await message.channel.send("야옹이라이더")
    if message.content.endswith("니"):
        file = discord.File("pic\니그로.jpg")
        await message.channel.send(file=file)
        await message.channel.send("니그로라이더")
    if message.content.endswith("낌"):
        file = discord.File("pic\낌새.jpg")
        await message.channel.send(file=file)
        await message.channel.send("낌새를 느끼고 놀란 라이더")
    if message.content.endswith("마"):
        file = discord.File("pic\마법.jpg")
        await message.channel.send(file=file)
        await message.channel.send("마법전사유캔도")
    if message.content.endswith("발"):
        file = discord.File("pic\발차기.jpg")
        await message.channel.send(file=file)
        await message.channel.send("발차기라이더")
    if message.content.endswith("아"):
        file = discord.File("pic\아이.jpg")
        await message.channel.send(file=file)
        await message.channel.send("아이라이더")
    if message.content.endswith("과"):
        file = discord.File("pic\과거.jpg")
        await message.channel.send(file=file)
        await message.channel.send("과거의 의사는 거짓으론 속일 수 없어 라이더")
    if message.content.endswith("음"):
        file = discord.File("pic\음악.jpg")
        await message.channel.send(file=file)
        await message.channel.send("음악라이더")
    if message.content.endswith("틀"):
        file = discord.File("pic\틀딱.jpg")
        await message.channel.send(file=file)
        await message.channel.send("틀딱라이더")
    if message.content.endswith("암"):
        file = discord.File("pic\암살자.jpg")
        await message.channel.send(file=file)
        await message.channel.send("암살자라이더")
    if message.content.endswith("손"):
        file = discord.File("pic\손목시계.jpg")
        await message.channel.send(file=file)
        await message.channel.send("손목시계라이더")
    if message.content.endswith("슈"):
        file = discord.File("pic\슈.jpg")
        await message.channel.send(file=file)
        await message.channel.send("슈퍼 히어로 대전 라이더")
    if message.content.endswith("기"):
        file = discord.File("pic\기차.jpg")
        await message.channel.send(file=file)
        await message.channel.send("기차 라이더")
    if message.content.endswith("다"):
        file = discord.File("pic\다이아몬드.jpg")
        await message.channel.send(file=file)
        await message.channel.send("다이아몬드 라이더")
    if message.content.endswith("게"):
        file = discord.File("pic\게.jpg")
        await message.channel.send(file=file)
        await message.channel.send("그런 게는 죽어야 합니다")
    if message.content.endswith("굴"):
        file = discord.File("pic\굴.jpg")
        await message.channel.send(file=file)
        await message.channel.send("엄마가 섬그늘에 굴 따러 가면라이더")
    if message.content.endswith("해"):
        file = discord.File("pic\물놀이.jpg")
        await message.channel.send(file=file)
        await message.channel.send("해변가 물놀이 라이더")
    if message.content.endswith("유"):
        file = discord.File("pic\유.jpg")
        await message.channel.send(file=file)
        await message.channel.send("유ㄱ덕 라이더")
    if message.content.endswith("만"):
        file = discord.File("pic\만두.jpg")
        await message.channel.send(file=file)
        await message.channel.send("만두 라이더")
    if message.content.endswith("짜"):
        file = discord.File("pic\짜장면.jpg")
        await message.channel.send(file=file)
        await message.channel.send("짜장면 배달부 라이더")
    if message.content.endswith("무"):
        file = discord.File("pic\무면허.jpg")
        await message.channel.send(file=file)
        await message.channel.send("무면허 라이더")
    if message.content.endswith("노"):
        file = discord.File("pic\노스트라.jpg")
        await message.channel.send(file=file)
        await message.channel.send("노스트라다무스")
    if message.content.endswith("나"):
        file = discord.File("pic\나는.jpg")
        await message.channel.send(file=file)
        await message.channel.send("나는 우주의 존재 라이더")
    if message.content.endswith("왜"):
        file = discord.File("pic\왜.jpg")
        await message.channel.send(file=file)
        await message.channel.send("왜 보고만 있는거냐고 물어보는 라이더")
    if message.content.endswith("온"):
        file = discord.File("pic\온두.jpg")
        await message.channel.send(file=file)
        await message.channel.send("온두루루 킷딴디스카")
    if message.content.endswith("인"):
        file = discord.File("pic\인형극.gif")
        await message.channel.send(file=file)
        await message.channel.send("인형극 라이더")
    if message.content.endswith("관"):
        file = discord.File("pic\관짝.gif")
        await message.channel.send(file=file)
        await message.channel.send("관짝 라이더")
    if message.content.endswith("작"):
        file = discord.File("pic\작살.gif")
        await message.channel.send(file=file)
        await message.channel.send("작살에 맞은 라이더")
    if message.content.endswith("더"):
        file = discord.File("pic\더이라면가.jpg")
        await message.channel.send(file=file)
        await message.channel.send("더이라면가")
    if message.content.endswith("제"):
        file = discord.File("pic\제로투.JPG")
        await message.channel.send(file=file)
        await message.channel.send("제로투 라이더")
    if message.content.endswith("행"):
        file = discord.File("pic\행글라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("행글라이더")
    if message.content.endswith("미"):
        file = discord.File("pic\미안.jpg")
        await message.channel.send(file=file)
        await message.channel.send("미안해하는 라이더")
    if message.content.endswith("할"):
        file = discord.File("pic\그렇지.png")
        await message.channel.send(file=file)
        await message.channel.send("할 때마다 새로운 기분이고...")
    if message.content.endswith("?"):
        file = discord.File("pic\물음표.jpg")
        await message.channel.send(file=file)
        await message.channel.send("? 라이더")
    if message.content.endswith("시"):
        file = discord.File("pic\시간조종.gif")
        await message.channel.send(file=file)
        await message.channel.send("시간 조종 라이더")
    if message.content.endswith("그"):
        file = discord.File("pic\그래프라이더.gif")
        await message.channel.send(file=file)
        await message.channel.send("그래프라이더")
    if message.content.endswith("친"):
        file = discord.File("pic\친한.jpg")
        await message.channel.send(file=file)
        await message.channel.send("친한듯이 말걸지 말라")
    if message.content.endswith("오"):
        file = discord.File("pic\오렌지.jpeg")
        await message.channel.send(file=file)
        await message.channel.send("오렌지암즈 라이더")
bot.run('') #<- insert your bot token! 

