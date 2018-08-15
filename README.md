# config

标签（空格分隔）： config

---

常见配置文件自动同步
## SetUp
### 安装git

### 安装Python

### 安装[watchdog](http://pythonhosted.org/watchdog/)
```
 pip install watchdog 
```
## 如何使用
### 1.GitHub上新建一个Git仓库
这里借用@[iWoz](https://github.com/iWoz)的截图
![image_1ckuvesak1b521hq38281he13ht9.png-88.4kB][1]

### 2.设置本地仓库
```
mkdir config
cd config

git init

##  ***注意***这里使用自己的git仓库，
##  ***注意***这里使用自己的git仓库
##  ***注意***这里使用自己的git仓库
git remote add origin git@github.com:Lt-grint/config.git 

## 添加子模块 这里不用改
git submodule add git@github.com:iWoz/file_sync.git

## stage all, commit and push to remote
git add -A
git commit -m "First commit."
git push -u origin master 
## 这里要确保push成功了才可以进行下一步,如果失败了可以尝试 git push origin master -f 强制推送
```
### 3.设置配置文件绝对路径
在你的Git仓库的根目录新建一个名为`file_list.txt`的文本文件，添加你的配置文件，请确保你设置的路径是绝对路径。例如
```
C:/Users/tao/.condarc
C:/Users/tao/.gitconfig
C:/Users/tao/.pip/pip.conf
```
  [1]: http://static.zybuluo.com/danerlt/w4fd2payvvt5c9scqrreigki/image_1ckuvesak1b521hq38281he13ht9.png