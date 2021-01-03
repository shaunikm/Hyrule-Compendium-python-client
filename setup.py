import setuptools

setuptools.setup(
    name='HyruleCompendium',
    version='0.0.3',
    author='Shaunik Musukula',
    author_email='shaunik.musukula@gmail.com',
    description='Python Wrapper for the Hyrule Compendium API',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Hyrule-Compendium-API/Hyrule-Compendium-python-client',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['requests']
)
