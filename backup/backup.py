import os, tarfile
import re
import shutil

"""
some code copy from https://www.cnblogs.com/liangqihui/p/9219333.html
"""


def make_targz(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def make_targz_one_by_one(output_filename, source_dir):
    tar = tarfile.open(output_filename, "w:gz")
    for root, dir, files in os.walk(source_dir):
        for file in files:
            pathfile = os.path.join(root, file)
            tar.add(pathfile)
    tar.close()


def copy_file(source_dir, out_dir, regex):
    """
    :param source_path: 源文件夹（绝对路径）
    :param out_dir: 新文件夹（绝对路径）
    :param regex: 正则表达式
    :return: None
    """
    for root, dirs, files in os.walk(source_dir):
        for name in files:
            match = re.search(regex, name)
            if match:
                abs_name = os.path.join(root, name)
                out_dir_name = root.replace(source_dir, out_dir, 1)
                out_name = os.path.join(out_dir_name, name)
                if not os.path.exists(out_dir_name):
                    os.makedirs(out_dir_name)
                shutil.copy(abs_name, out_name)


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    dirname = os.path.join(dirname, 'backage')
    print(dirname)
    os.chdir('../www')
    regex = re.compile(r'(\.py)|(\.ico)')
    source_path = os.path.abspath('.')
    copy_file(source_path, dirname, regex)
