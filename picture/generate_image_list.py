import os

# 获取当前目录
current_directory = os.getcwd()

# 获取当前目录下的所有文件
files = os.listdir(current_directory)

# 用于存储图片文件的列表
image_files = []

# 遍历所有文件，筛选出图片文件
for i, file in enumerate(files, start=1):
    # 检查文件扩展名以确定是否为图片文件
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif") or file.endswith(".webp"):
        # 提取不包含扩展名的文件名作为名称
        image_name = os.path.splitext(file)[0]
        # 构建图片文件的链接
        image_url = f"./{file}"
        # 将信息添加到列表中，包括序号、名称和链接
        image_files.append(f"| {i}   | {image_name}      | [下载]({image_url}) |")

# 清空或创建Markdown文件并写入表格内容
with open("list.md", "w", encoding="utf-8") as md_file:
    # 写入Markdown表格的标题行和分隔行
    md_file.write("| #   | 名称                        | 链接                      |\n")
    md_file.write("| --- | --------------------------- | ------------------------- |\n")
    # 写入图片信息行
    md_file.write("\n".join(image_files))

if image_files:
    print("已生成图片列表到 list.md 文件")
    print("现在可以打开 list.md 文件查看")
    print("\n".join(image_files))
else:
    print("当前目录下没有图片文件")
