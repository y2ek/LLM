# 高效 Prompt 的两个关键原则:编写清晰、具体的指令和给予模型充足思考时间。
from tool import get_completion
prompt = f"""
告诉我华为公司生产的GT Watch Plus运动手表的相关信息
"""
response = get_completion(prompt)
print(response)