import discord
# 반복 작업을 위한 패키지
from discord.ext import tasks
# 현재 시간을 받아와 구조체에 넣어주는 용도로 사용할 패키지
import datetime
# 중복 전송을 방지하기 위해 사용할 패키지
import time


class chatbot(discord.Client):
    # 1초에 한번 수행될 작업
    # 여기 함수는 에러가 나도 에러 메시지가 출력되지 않으므로 주의.
    @tasks.loop(seconds=1)
    async def every_hour_notice(self):
        if datetime.datetime.now().minute == 0 and datetime.datetime.now().second == 0:
            await client.get_guild("Input Your Server ID as Int").get_channel("Input Your Channel ID as Int").send("현재 {}시 {}분 입니다.".format(datetime.datetime.now().hour, datetime.datetime.now().minute))

            # 1초 sleep하여 중복 전송 방지
            time.sleep(1)

    # on_ready는 봇을 다시 구성할 때도 호출 됨 (한번만 호출되는 것이 아님.)
    async def on_ready(self):
        game = discord.Game("TEST")
        await client.change_presence(status=discord.Status.online, activity=game)
        print("READY")

        self.every_hour_notice.start()


if __name__ == "__main__":
    client = chatbot()
    client.run("Your Discord Bot Token")
