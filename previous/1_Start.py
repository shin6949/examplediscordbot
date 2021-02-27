# discord 라이브러리 사용 선언
import discord


class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, Activity
        game = discord.Game("내용")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        # message.author.bot = message의 author가 bot이냐 아니냐를 질의하여 True or False로 표시
        # 즉, if는 True일 때 : 밑에 들여쓰기 된 내용을 시행하므로, author가 Bot일 경우 아래의 코드를 실행
        if message.author.bot:
            # return None = 아무 것도 Return 하지 않음. 함수의 수행을 끝내는 역할을 함.
            # 즉, return None이 실행된다면, 순차 지향인 코드에서는 아랫 줄의 코드를 실행하지 않게 됨.
            return None

        # message.content = message의 내용
        # == "!바보" = 왼쪽의 값이 "!바보"와 완벽 일치하면 True, 아니면 False를 리턴
        # 즉, 메시지의 내용이 "!바보"라고 하면 : 밑에 들여쓰기 된 내용을 시행하게 됨.
        if message.content == "!바보":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "너도 바보"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None


# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 클래스 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run("Your Discord Bot Token")
