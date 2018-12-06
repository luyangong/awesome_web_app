import os
import re
import shutil


def copy_file(source_dir, out_dir, regex):
    """
    :param source_path: 源文件夹（绝对路径）
    :param out_dir: 新文件夹（绝对路径）
    :param regex: 正则表达式
    :return: None
    """
    for root, dirs, files in os.walk(source_dir):
        if root.endswith('test'):
            continue
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
    dirname1 = os.path.dirname(__file__)
    dirname = os.path.join(dirname1, 'backage')
    print(dirname)
    os.chdir('../www')
    regex = re.compile(r'\w+(?!.pyc)')
    source_path = os.path.abspath('.')
    copy_file(source_path, dirname, regex)
    os.chdir(dirname1)
    print(shutil.make_archive('archive', 'zip', dirname))
