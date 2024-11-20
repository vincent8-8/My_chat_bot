from anthropic import Anthropic
import os

# API 키를 직접 입력하세요
api_key = "sk-ant-api03-..."  # 여기에 실제 API 키를 넣으세요

# Anthropic 클라이언트 초기화
anthropic = Anthropic(
    api_key=api_key
)

try:
    # 간단한 테스트 메시지 보내기
    message = anthropic.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Hello, Claude!"
            }
        ]
    )
    print("성공!")
    print("응답:", message.content[0].text)
except Exception as e:
    print("에러 발생:", str(e))