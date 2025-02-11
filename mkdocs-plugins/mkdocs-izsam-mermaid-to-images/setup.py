from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup(
    include_package_data=True,
    name='mkdocs-izsam-mermaid-to-images',
    version='1.0.8',
    description='MkDocs plugin to convert Mermaid code blocks to images.',
    long_description_content_type='text/markdown',
    long_description=README + '\n\n' + HISTORY,
    keywords=['MkDocs', 'Mermaid', 'Mermaid to images'],
    license='MIT',
    packages=find_packages(),
    url='',
    download_url='',
    author='Alessandro De Luca',
    author_email='al.deluca@izs.it',
    python_requires='>=3.8',    
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-izsam-mermaid-to-images = mkdocs_izsam_mermaid_to_images.plugin:MermaidToImagePlugin',
        ]
    }
)