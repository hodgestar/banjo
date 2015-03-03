from setuptools import setup, find_packages

setup(
    name="banjo",
    version="0.0.1",
    url='http://github.com/hodgestar/banjo',
    license='MIT',
    description="Banjo Hero in Pygame, a tutorial.",
    long_description=open('README.rst', 'r').read(),
    author='Simon Cross',
    author_email='hodgestar@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pygame',
        'wiring',
        'click',
    ],
    entry_points='''
        [console_scripts]
        banjo=banjo.scripts.banjo:cli
    ''',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
)
