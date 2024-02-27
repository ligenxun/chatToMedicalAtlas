# -*- coding: utf-8 -*-
# @Time : 2024/2/27 12:01 
# @Author : cys
# @Email : ligenxun@foxmail.com
# @File : chat_to_graph

'''
生成大纲，通过关键词组、描述性内容与指定结构，生成对应的大纲
'''

from AI_tools.aiToolCalls import aiToolCalls


class chat_to_graph:
    def __init__(self):
        self.ai = aiToolCalls()

    def generateText(self, text_string, qa_type="text", filePath=None):
        '''生成提示词。简单测试版本'''
        if qa_type == 'text':
            pr = f'''现在假设你是一个医院质控管理人员，请查看以下【】号中间的文本:【{text_string}】，请依据以上文本，生成以上文本的 neo4j 格式知识图谱：'''
        elif qa_type == 'file':
            pr = f'''现在假设你是一个医院质控管理人员，请查看以下文件:{filePath}，请依据以上文本，生成以上文本的 neo4j 格式知识图谱：'''
        return pr

    def generateGraph(self, text_string):

        question = self.generateText(text_string)

        return self.ai.dispatchCenter(question)


if __name__ == '__main__':
    chat_to_graph = chat_to_graph()
    print(chat_to_graph.generateGraph(
        "ceshi"))
