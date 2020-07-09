# discord 라이브러리 사용 선언
import discord

# 이미지 다운로드를 위한 urllib
import urllib.request


class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("내용")
        await client.change_presence(status=discord.Status.online, activity=game)
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        if message.author.bot:
            return None

        if message.content == "!embed":
            channel = message.channel

            # 이미지를 지정한 URL에서 다운로드하여, "explain.png"로 저장
            urllib.request.urlretrieve("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png", "explain.png")

            # 디스코드에 올릴 파일을 지정하고, attachment에서 사용할 이름을 "image.png"로 지정
            image = discord.File("explain.png", filename="image.png")

            # Embed 메시지 구성
            embed = discord.Embed(title="테스트", description="테스트용 메시지입니다.", color=0x00ff56)
            # 아까 지정한 파일 이름으로 해야함.
            embed.set_thumbnail(url="attachment://image.png")
            embed.add_field(name="이름", value="값", inline=True)

            # 메시지 보내기
            await channel.send(embed=embed, file=image)


if __name__ == "__main__":
    client = chatbot()
    client.run("Your Discord Bot Token")
