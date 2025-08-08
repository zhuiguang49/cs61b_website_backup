import os
import shutil

# 仅处理这两个目录
TARGET_DIRS = ['assets', 'materials']

for target_dir in TARGET_DIRS:
    # 检查目录是否存在
    if not os.path.isdir(target_dir):
        print(f"目录不存在，跳过: {target_dir}")
        continue
    
    # 遍历目标目录及其子目录
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            # 只处理.html文件，排除index.html
            if file.endswith('.html') and file != 'index.html':
                # 提取文件名（不含扩展名）
                name = os.path.splitext(file)[0]
                # 原文件完整路径
                old_path = os.path.join(root, file)
                # 目标文件夹路径（与文件名同名）
                new_dir = os.path.join(root, name)
                # 目标文件路径（文件夹下的index.html）
                new_path = os.path.join(new_dir, 'index.html')
                
                try:
                    # 若目标路径已存在，无论其是文件、链接还是目录，先强制删除
                    if os.path.exists(new_dir):
                        if os.path.isfile(new_dir) or os.path.islink(new_dir):
                            os.remove(new_dir)  # 删除文件或链接
                            print(f"已删除同名文件/链接: {new_dir}")
                        else:
                            shutil.rmtree(new_dir)  # 删除目录及内容
                            print(f"已删除同名目录: {new_dir}")
                    
                    # 创建目标文件夹并移动文件
                    os.makedirs(new_dir, exist_ok=True)
                    shutil.move(old_path, new_path)
                    print(f"处理完成: {old_path} -> {new_path}")
                except Exception as e:
                    # 捕获异常并继续处理其他文件
                    print(f"处理失败 {old_path}: {str(e)}")
