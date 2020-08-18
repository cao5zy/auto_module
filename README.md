# auto_module
这是一个帮助开发人员建立本地工作流水线，实现自动化的工具。先给一个简单例子。
```
tasks:
  - name: 监控文件变动
    watch:
      paths:
        - path: ./src/
          - ext:
            - .js
      tasks:
        - name: 执行eslint
          command:
            cmd: ./node_modules/.bin/eslint --fix ./src/*.js
```
上面建立了一个简单的流水线，即监控`./src/`下的所有`.js`文件，如果有文件发生了变化，那么立即执行`eslint`命令。
用过ansible的同学一定会发现，上面的写法和ansible的playbook很类似。的确是这样，这个功能模块的定义就是模仿对应的ansible模块，但是目前`auto-dev`所提供的功能模块很有限。

# 测试命令
```
source .env/bin/activate
cd src
python main.py auto.yaml
```

# 功能模块
## watch
## synchronize
## file
## copy
```
- name: copy file or directory
  copy:
    src: auto.yaml
    dest: ../auto.yaml
```
`src`和`dest`都是相对于当前文件所在目录的路径。
## command
