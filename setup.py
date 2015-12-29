import re
import sys

from setuptools import find_packages, setup


def _read_long_description():
    try:
        with open('readme.rst') as fd:
            return fd.read()
    except Exception:
        return None


with open('hide_env.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(),
        re.MULTILINE
    ).group(1)

with open('requirements/base.txt', 'r') as fd:
    requirements = fd.read().strip().split('\n')

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass

setup(
    name='hide-env',
    version=version,
    url='http://github.com/relekang/hide-env',
    author='Rolf Erik Lekang',
    author_email='me@rolflekang.com',
    description='Hide environment variables from output.',
    long_description=_read_long_description(),
    packages=find_packages(exclude='tests'),
    license='MIT',
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        hide-env=hide_env:main
    ''',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)
