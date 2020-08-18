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
```
tasks:
  - name: watch changes
    watch:
      paths:
        - path: ./src/
          ext:
            - .js
    tasks:
      - ./lint.yaml
      - name: pack files
        command:
          cmd: yarn build
          chdir: ./
```
`watch`模块用于监视文件变动，当发现变动时，执行`tasks`中的任务。在`tasks`中，不可再次嵌套`watch`

## synchronize
```
tasks:
  - name: synchronize files in folders
    synchronize:
      src: ./src/
      dest: ../test/
```
用于同步`src`和`dest`中发生变化的文件，`src`和`dest`都是相对于当前文件所在目录的路径。

## file
```
tasks:
  - name: create folder
    file:
      path: ../new_folder
      state: directory
```
创建文件夹

## copy
```
- name: copy file or directory
  copy:
    src: auto.yaml
    dest: ../auto.yaml
```
`src`和`dest`都是相对于当前文件所在目录的路径。
## command
```
tasks:
  - name: run pylint
    command:
      cmd: pylint *.py
      chdir: ./modules/
      env: source .env/bin/activate
      chenvdir: ../
```
用于执行命令。`cmd`和`chdir`为执行的命令以及命令所在的路径。`env`和`chenvdir`为执行cmd之前需要执行的命令，例如`pylint`是安装在虚拟环境中，先要启动虚拟环境。
