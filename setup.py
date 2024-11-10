from setuptools import setup, find_packages # type: ignore

setup(
    name='my_interactive_plots',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'plotly'
    ],
    author='Dmitry Gorschkov',
    author_email='dmgorschkov@mail.ru',
    description='A package for creating interactive plots.',
    url='https://github.com/yourusername/my_interactive_plots',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)

