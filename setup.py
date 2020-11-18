import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name='ezviz',
    version="0.1.5.5",
    license='Apache Software License',
    author='William Luke',
    author_email='william@atto-byte.com',
    description='Pilot your Ezviz cameras',
    long_description="Pilot your Ezviz cameras with this module. Please view readme on github",
    url='http://github.com/williamluke4/pyEzviz/',
    packages=setuptools.find_packages(include=['ezviz']),
    setup_requires=[
        'requests',
        'setuptools'
    ],
    install_requires=[
        'requests',
        'fake_useragent',
        'pandas'
    ],
    entry_points={
    'console_scripts': [
        'ezviz = ezviz.__main__:main'
    ]
    }
)
