# chatToMedicalAtlas

项目核心：基于医疗领域知识图谱的问答系统，同时使用了chatGPT、chatGLM4等方式生成医学知识图谱。

其中整理好的文件转知识图谱相对通用，主要强化：利用chatGPT、chatGLM4等大语言模型，处理医疗公开资料、临床路径、卫健委诊疗指标规范要求等方面资料，生成医疗知识图谱。

核心需求在于，医院项目现场大部分情况下都是内网环境，无法直接使用chatGPT等模型，同时因为运算资源非常有限的情况下，无法直接部署llms大模型，需要使用
大模型生成的‘结论’；同时医学实际业务的使用，要求内容更加精准，不能出现AI的‘幻觉’（胡编乱造），所以需要固化成一个结论模型，进行人工复查后，再进行使用。

问答系统除了使用常规的知识图谱进行检索回答外，还可使用较小的llms模型进行问答（后续计划）。


# 项目效果 #
以下两张图是系统实际运行效果：
![系统运行效果图](https://github.com/zhihao-chen/QASystemOnMedicalGraph/blob/master/img/%E6%95%88%E6%9E%9C%E5%9B%BE.png)

# 项目运行方式
运行环境：Python3
数据库：neo4j
预训练词向量：[https://github.com/Embedding/Chinese-Word-Vectors](https://github.com/Embedding/Chinese-Word-Vectors)

1. 搭建知识图谱：
```bash
python build_grapy.py
```
大概几个小时，耐心等待。
2. 启动问答测试：
```bash
python kbqa_test.py
```
3. 启动大模型生成：python 
```bash
python chat_to_graph.py
```

# 医疗知识图谱
数据源：39健康网、国家卫健委、各省卫健委相关医学指标部分。包括15项信息，其中7类实体，约3.7万实体，21万实体关系。

**【后续推翻优化】本系统的知识图谱结构如下：**

![知识图谱结构](https://github.com/zhihao-chen/QASystemOnMedicalGraph/blob/master/img/%E7%9F%A5%E8%AF%86%E5%9B%BE%E8%B0%B1.png)


**【后续推翻优化】1.1 知识图谱实体类型**

| 实体类型     | 中文含义 | 实体数量 | 举例                   |
| ------------ | -------- | -------- | ---------------------- |
| Disease      | 疾病     | 14336    | 乙肝，癫痫             |
| Alias        | 别名     | 8877     | 小儿褐黄病综合征，广疮 |
| Symptom      | 症状     | 5622     | 手足烦热，四肢麻木     |
| Part         | 发病部位 | 82       | 手部，上肢             |
| Department   | 所属科室 | 82       | 感染科，外科           |
| Complication | 并发症   | 3201     | 落枕，流感             |
| Drug         | 药品     | 4625     | 西黄胶囊，司帕沙星     |
| Total        | 总计     | 36825    |                        |

**【后续推翻优化】1.2 知识图谱实体关系类型**

| 实体关系类型     | 中文含义   | 关系数量 | 举例                         |
| ---------------- | ---------- | -------- | ---------------------------- |
| ALIAS_IS         | 别名是     | 52578    | 癫痫 别名是 羊角风           |
| HAS_SYMPTOM      | 症状有     | 62105    | 乙肝 症状有 肝功能异常       |
| PART_IS          | 发病部位是 | 26660    | 乙肝 发病部位是 肝           |
| DEPARTMENT_IS    | 所属科室是 | 33867    | 乙肝 所属科室是 传染科       |
| HAS_COMPLICATION | 并发症有   | 25183    | 乙肝 并发症有 肝硬化         |
| HAS_DRUG         | 可用药品   | 35914    | 乙肝 可用药品 恩替卡韦分散片 |
| TOTAL            | 总计       | 210018   |  约210018对关系                            |

**【后续推翻优化】1.3 知识图谱疾病属性**

| 疾病属性  | 中文含义 | 举例               |
| --------- | -------- | ------------------ |
| age       | 发病人群 | 老人，小孩         |
| insurance | 是否医保 | 医保               |
| infection | 是否传染 | 有传染性           |
| checklist | 检查项目 | 肝功能检查         |
| treatment | 治疗方法 | 药物治疗、心理治疗 |
| period    | 治愈周期 | 一周               |
| rate      | 治愈率   | 0.1%               |
| money     | 费用     | 1000-2000元        |

# 问题意图识别
基于特征词分类的方法来识别用户查询意图

| 意图类型         | 中文含义         | 举例               |
| ---------------- | ---------------- | ------------------ |
| query_disease    | 查询疾病         | 肝肿大是什么病     |
| query_symptom    | 查询症状         | 慢性乙肝有什么表现 |
| query_cureway    | 查询治疗方案     | 肚子一直痛怎么办   |
| query_checklist  | 查询检查项目     | 乙肝需要做哪些检查 |
| query_department | 查询所属科室     | 乙肝去哪个科       |
| query_rate       | 查询治愈率       | 乙肝能治好吗       |
| query_period     | 查询治愈周期     | 乙肝多久能治好     |
| disease_describe | 查询疾病所以属性 | 慢性咽炎           |



本文知识图谱构建部分参考：[QASystemOnMedicalKG](https://github.com/zhihao-chen/QASystemOnMedicalGraph)
