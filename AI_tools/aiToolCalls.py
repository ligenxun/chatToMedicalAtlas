# -*- coding: utf-8 -*-
# @Time : 2024/2/2 17:15 
# @Author : cys
# @Email : ligenxun@foxmail.com
# @File : aiToolCalls
'''
调用ai工具，负责对接ai工具的调用（如openai、文心一言等对接方切换，就在这里进行）
使用：传入文本，返回处理后的文本
'''


class aiToolCalls:
    def __init__(self):
        self.aiType = 'openAI'

    def openAI(self, text):
        from AI_tools.openAI_chat import chat_openai as chat

        return chat().chat(text).choices[0].message.content # 取出返回内容的内容结论部分

    def GLM(self, text):
        pass

    def baidu(self, text):
        pass

    def Claude(self, text):
        pass
    # 调度中心
    def dispatchCenter(self, text):
        if self.aiType == 'openAI':
            return self.openAI(text)
        elif self.aiType == 'GLM':
            return self.GLM(text)
        elif self.aiType == 'baidu':
            return self.baidu(text)
        elif self.aiType == 'Claude':
            return self.Claude(text)
