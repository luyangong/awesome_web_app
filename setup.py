# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name='MyApp',  # 应用名
    version='1.0',  # 版本号
    packages=['myapp'],  # 包括在安装包内的Python包
    exclude_package_data={'': ['.gitignore', '*.pyc']},
    install_requires=[  # 依赖列表
        'aiohttp==3.1.3',
    ]
)
