from setuptools import setup

setup(
    name='greeter',
    entry_points={
        'console_scripts': [
            'greeter= greeter:main',
        ],
    }
)


