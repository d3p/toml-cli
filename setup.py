from setuptools import setup

setup(
    name='toml-cli',
    version='0.3.2',
    packages=['toml_cli'],
    install_requires=[
        'typer',
        'tomlkit',
        'regex',
    ],
    entry_points={
        'console_scripts': [
            'toml = toml_cli:main',
        ]
    }
)
