from setuptools import setup, find_packages

def get_requirements(file_path : str) -> list[str]:
    """
    This function reads a requirements file and returns a list of packages.
    It ignores any lines that start with '-e' or are comments.
    """
    requirements = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if line and not line.startswith('-e') and not line.startswith('#'):
                requirements.append(line)
    return requirements

setup(
    name='mlprojects', 
    version='0.0.1', 
    author='Ashraf',
    author_email='ashrafdcc1502@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
    
)