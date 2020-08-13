# auto_module
模块的自动化工具

# 测试命令
```
source .env/bin/activate
cd src
python main.py auto.yaml
```

# 命令模块
## copy
```
- name: copy file or directory
  copy:
    src: auto.yaml
    dest: ../auto.yaml
```
`src`和`dest`都是相对于当前文件所在目录的路径。
    
