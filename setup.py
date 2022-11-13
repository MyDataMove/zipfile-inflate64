from pathlib import Path

from setuptools import find_packages, setup

readme_file = Path(__file__).parent / 'README.md'
with readme_file.open() as f:
    long_description = f.read()

setup(
    name='zipfile-inflate64',
    description="Extract Enhanced Deflate ZIP archives with Python's zipfile API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL-3.0',
    url='https://codeberg.org/miurahr/zipfile-inflate64',
    project_urls={
        'Bug Reports': 'https://codeberg.org/miurahr/zipfile-inflate64/issues',
        'Source': 'https://codeberg.org/miurahr/zipfile-inflate64',
    },
    author='Hiroshi Miura',
    author_email='miurahr@linux.com',
    keywords='zip zipfile deflate deflate64 inflate64',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python',
        'Topic :: System :: Archiving',
        'Topic :: System :: Archiving :: Compression',
    ],
    python_requires='>=3.7',
    install_requires=['inflate64'],
    packages=find_packages(),
)
