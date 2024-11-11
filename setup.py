from setuptools import setup, find_packages # type: ignore

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='my_interactive_plots',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
   install_requires=[
        'pandas>=1.0.0',
        'plotly>=5.0.0',
        'click>=8.0.0',
    ],
    extras_require={
        'dev': [
            'pytest',
            'click',
        ],
    },
    author='Dmitry Gorschkov',
    author_email='dmgorschkov@mail.ru',
    description='A package for creating interactive plots.',
    url='https://github.com/sdr34/my_interactive_plots',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'myplot=my_interactive_plots.cli:cli'
        ],
    },
)

