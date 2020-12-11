from setuptools import setup

#   Ongoing: 2020-12-11T03:51:43AEDT but what actually connects cute_snek (as an option) to snek?

#   TODO: 2020-12-11T00:05:09AEDT require than package 'snek' is also installed? (since we fail to run without it?)

setup(
    name='cute_snek',
    entry_points={
        'snek_types': [
            'cute = cute_snek:cute_snek',
        ],
    }
)
