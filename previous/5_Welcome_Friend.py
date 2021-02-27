# discord 라이브러리 사용 선언
import discord


def find_first_channel(channels):
    position_array = [i.position for i in channels]
    for i in channels:
        if i.position == min(position_array):
            return i


class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("내용")
        await client.change_presence(status=discord.Status.online, activity=game)
        print("READY")

    # 서버에 멤버가 들어왔을 때 수행 될 이벤트
    async def on_member_join(self, member):
        msg = "<@{}>님이 서버에 들어오셨어요. 환영합니다.".format(str(member.id))
        await find_first_channel(member.guild.text_channels).send(msg)
        return None

    # 사버에 멤버가 나갔을 때 수행 될 이벤트
    async def on_member_remove(self, member):
        msg = "<@{}>님이 서버에서 나가거나 추방되었습니다.".format(str(member.id))
        await find_first_channel(member.guild.text_channels).send(msg)
        return None

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        if message.author.bot:
            return None


if __name__ == "__main__":
    client = chatbot()
    client.run("Your Discord Bot Token")
