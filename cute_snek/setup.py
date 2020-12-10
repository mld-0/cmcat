from setuptools import setup

#   TODO: 2020-12-11T00:05:09AEDT require than package 'snek' is also installed?

setup(
    name='cute_snek',
    entry_points={
        'snek_types': [
            'cute = cute_snek:cute_snek',
        ],
    }
)
