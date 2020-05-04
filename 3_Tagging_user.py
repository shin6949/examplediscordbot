# discord 라이브러리 사용 선언
import discord


class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("내용")
        await client.change_presence(status=discord.Status.online, activity=game)
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        if message.author.bot:
            return None

        if message.content == "날 태그해 줘":
            channel = message.channel

            msg = "<@{}>".format(message.author.id)
            await channel.send(msg)
            return None


if __name__ == "__main__":
    client = chatbot()
    client.run("Your Discord Bot Token")
