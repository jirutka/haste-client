from distutils.core import setup

setup(
    name='haste-client',
    version='1.0',
    scripts=['haste'],
    url='https://github.com/jirutka/haste-client',
    license='MIT',
    author='Jakub Jirutka',
    author_email='jakub@jirutka.cz',
    description='CLI client for Haste server (hastebin.com) written in Python.',
    long_description=open('README.md').read(),
    requires=[
        'requests',
        'docopt'
    ]
)
