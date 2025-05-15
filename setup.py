from setuptools import setup, find_packages

setup(
    name='ml_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'matplotlib',
        'plotly'
    ],
    author='Kene Mbamali',
    description='A simple machine learning package for classification and regression',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
)
