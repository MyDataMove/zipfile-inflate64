import setuptools

setuptools.setup(
    name='zipfile-inflate64',
    version='0.8.0',
    packages=setuptools.find_packages(),
    description='Patch ZipFile to support inflate64 compression',
    url='https://github.com/MyDataMove/zipfile-inflate64',
    license='Apache License, Version 2.0',
    setup_requires=[
    ],
    dependencies=[
        'inflate64>=0.3.1;python_version>"3.6"'
    ],
)
