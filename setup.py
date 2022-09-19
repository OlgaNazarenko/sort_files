from setuptools import setup, find_namespace_packages

setup(
    name='sorting_folder',
    version='1.0',
    description='Sorting of the folder',
    url='https://github.com/olganazarenko/Clean_folder.git',
    author='The lost person in Python',
    author_email='olga.nazarenko31@gmail.com',
    license='MIT',
    packages=find_namespace_packages()
    entry_points={'console_scripts': ['clean-folder = sorting_folder.test_sorting:main']}
)
