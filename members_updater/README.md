# 照片上传脚本中文说明

## 前置环境

一个合适版本的python，安装pip包：pypinyin==0.53.0

## 使用脚本

在项目**根目录**下，执行：`python members_updater/updater.py <year> <name> <photo_path> [-n FILENAME] [-w WEBSITE]`

例如：`python updater.py 2025 张三 /your/photo/path/pic.jpg -n myphotoname -w your.website.com` 的执行结果是：添加一名**2025**届的学生，**中文姓名**为**张三**，其照片原始文件所在路径为 **`/your/photo/path/pic.jpg`**，复制到项目照片文件夹时将其**重命名**为**myphotoname**，其**个人网站地址**为 **`your.website.com`**。

如果想要查看脚本的帮助，请在根目录下执行：`python members_updater/updater.py -h`

## 参数说明(有序)

### 必填参数

**`year`：** 入学年份。

**`name`：** 学生中文姓名。

**`photo_path`：** 照片原始文件所在路径。

### 可选参数

不需要输入时可以留空的参数列表。请注意，可选参数的输入可以使用 `-n` 的单横线简略形式，也可使用 `--filename` 的双横线完整形式作为简略形式的替换，注意对应关系即可。

**`filename(-n)`：** 照片移动后所希望的新文件名。**不包括文件类型后缀。**

**`website(-w)`：** 个人网站地址。
