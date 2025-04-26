from setuptools import setup, find_packages

setup(
    name="netraven",
    version="0.1",
    packages=find_packages(),  # <- NO where= here. find automatically!
    install_requires=[
        "pandas",
        "requests",
        "colorama"
    ],
    entry_points={
        'console_scripts': [
            'netraven_run = netraven.__main__:main'
        ]
    }
)
