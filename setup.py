from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='encoding_tools',
    version="0.0.2",
    description="A package to deal with encoding.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Thomas Berdy',
    author_email='thomas.berdy@outlook.com',
    url='https://gitlab.kozlek.net/open-source/encoding_tools',
    packages=[
        'encoding_tools'
    ],
    classifiers=(
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    install_requires=(
        'chardet',
        'Unidecode',
    ),
    include_package_data=True,
    zip_safe=False,
)
