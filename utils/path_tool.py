""" 为整个工程提供统一的绝对路径 """

import os

def get_project_root() -> str:
    """ 获取工程所在的根目录 """

    # 获取当前代码文件绝对的路径
    current_file = os.path.abspath(__file__)
    # 获取工程的根目录(当前代码文件路径向上跳两级)
    current_dir = os.path.dirname(current_file)
    project_root = os.path.dirname(current_dir)
    return project_root

def get_abs_path(relative_path: str) -> str:
    """ 传递相对路径，返回绝对路径 """

    project_root = get_project_root()
    return os.path.join(project_root, relative_path)



if __name__ == "__main__":
    print(get_abs_path("config\config.txt"))