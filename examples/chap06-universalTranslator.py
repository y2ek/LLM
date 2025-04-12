user_messages = [
"La performance du système est plus lente que d'habitude.", # System performance is slower than normal
"Mi monitor tiene píxeles que no se iluminan.", # My monitor haspixels that are not lighting
"Il mio mouse non funziona", # My mouse is notworking
"Mój klawisz Ctrl jest zepsuty", # My keyboard hasa broken control key
"我的屏幕在闪烁" # My screen isflashing
]

import time
from tool import get_completion
for issue in user_messages:
    time.sleep(20)
    prompt = f"告诉我以下文本是什么语种，直接输出语种，如法语，无需输出标点符号:```{issue}```"
    lang = get_completion(prompt)
    print(f"原始消息 ({lang}): {issue}\n")
    prompt = f"""
    将以下消息分别翻译成英文和中文，并写成
    中文翻译：xxx
    英文翻译：yyy
    的格式：
    ```{issue}```
    """
    response = get_completion(prompt)
    print(response, "\n=========================================")