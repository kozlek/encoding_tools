from setuptools import setup, find_packages

setup(
    name='encoding_tools',
    version=__import__('encoding_tools').__version__,
    description=__import__('encoding_tools').__doc__,
    long_description=open('README.md').read(),
    author='Thomas Berdy',
    author_email='thomas.berdy@outlook.com',
    url='https://gitlab.kozlek.net/open-source/encoding_tools',
    packages=find_packages(),
    classifiers=[
        'Development Status :: Beta',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'chardet',
        'Unidecode',
    ],
    include_package_data=True,
    zip_safe=False,
)
