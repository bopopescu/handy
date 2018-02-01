from io import open

from setuptools import find_packages, setup

with open('handy/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

# 'setup.py publish' shortcut.
import sys,os
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

packages = ['handi']

REQUIRES = [
            'pysftp>=0.2.9',
            'urllib3>=1.21.1,<1.23',
            #'magic_wormhole>=0.10.4',
            #'thefuck>=3.25',
            'pyautogui>=0.9.36'
            #'tensorflow-gpu>=1.2.0',
            ]

keywords = ''
setup(
    name='handi',
    version=version,
    description='',
    long_description=readme,
    author='gustav0125',
    author_email='gustav0125@outlook.com',
    maintainer='gustav0125',
    maintainer_email='gustav0125@outlook.com',
    url='https://github.com/gustavkkk/handy',
    license='MIT/Apache-2.0',
    include_package_data=True,
    keywords=['utility','basics'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],
    zip_safe=False,
    packages=find_packages(),#packages,#
)