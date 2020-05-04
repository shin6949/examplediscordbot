# discord 라이브러리 사용 선언
import discord


class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("내용")
        await client.change_presence(status=discord.Status.online, activity=game)
        print("READY")

        # 봇이 들어간 서버의 수는 client -> guilds에 list 형태로 저장되어 있음.
        guild_list = client.guilds

        # 간단하게 하자면 아래와 같이 표현 가능
        print(guild_list)

        """
        하지만, 많은 서버에 들어가 있어 줄 바꿈이 필요한 경우에는 for를 이용해서 구성해야함.
        list 안에는 discord.guild.Guild 타입의 변수가 있음.
        이를 통해 정보를 불러올 수 있음. 이번 테스트에선 봇이 들어간 서버의 이름과 서버의 id를 표시하는 코드
        
        갖고 올 수 있는 서버의 정보는 아래를 참조
        URL: https://discordpy.readthedocs.io/en/latest/api.html#guild
        """
        for i in guild_list:
            print("서버 ID: {} / 서버 이름: {}".format(i.id, i.name))

    async def on_message(self, message):
        if message.author.bot:
            return None


if __name__ == "__main__":
    client = chatbot()
    client.run("Your Discord Bot Token")
