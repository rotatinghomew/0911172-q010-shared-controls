# 共享对照复核

本地科研数据分析应用，使用合成记录。数据读取、描述性分析与报告序列化相互分离，便于离线复现分析结果。

## Requirements

需要 Python 3.11 或更高版本；应用仅使用标准库。

## Run and test

在本目录运行 `python -m unittest discover -s tests -v` 执行测试。运行 `python -m study_app --data data/sample.json --output report.json` 生成报告。输入记录为合成数据，可在本地修改。
