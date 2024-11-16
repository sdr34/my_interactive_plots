from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent.resolve()

README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name='my_interactive_plots',
    version='0.1.6',
    packages=find_packages(),
    include_package_data=True,
   install_requires=[
        'pandas>=1.0.0',
        'plotly>=5.0.0',
        'click>=8.0.0',
        'requests>=2.25.0',
        'sqlalchemy>=1.4.0',  
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
    long_description=README,
    long_description_content_type='text/markdown', 
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

