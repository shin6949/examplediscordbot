# discord 라이브러리 사용 선언
import discord


class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("내용")
        await client.change_presence(status=discord.Status.online, activity=game)
        print("READY")

        # 봇이 로딩되면 특정인에게 DM을 보냄
        author = await client.get_user("Your ID").create_dm()
        await author.send("on_ready가 호출되었습니다.")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        if message.author.bot:
            return None

        if message.content == "!설명":
            if message.author.dm_channel:
                await message.author.dm_channel.send("DM 채널이 있어서 그냥 보냈어요!")
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()
                await channel.send("DM 채널이 없어서 만들고 보냈어요!")


if __name__ == "__main__":
    client = chatbot()
    client.run("Your Discord Bot Token")
