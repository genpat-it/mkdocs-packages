# mkdocs_izsam_mermaid_to_images/plugin.py

import os
import subprocess
import tempfile
import json  # Import the json module
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class MermaidToImagePlugin(BasePlugin):
    config_scheme = (
        ('output_dir', config_options.Type(str, default='mermaid_images')),
        ('image_format', config_options.Choice(['png', 'svg'], default='svg')),
        ('image_class', config_options.Type(str, default='mmd')),
        ('mermaid_config', config_options.Type(dict, default={})),
        ('scale', config_options.Type(int, default=1)),
    )

    def on_page_markdown(self, markdown, page, config, files):
        """
        This method is called on each page's markdown content.
        It converts Mermaid diagrams to images and replaces the code blocks with image references.
        """
        # Determine the output directory relative to the current page
        page_dir = os.path.dirname(page.file.abs_dest_path)
        output_dir = os.path.join(page_dir, self.config['output_dir'])
        os.makedirs(output_dir, exist_ok=True)

        # Find Mermaid code blocks and convert them to images
        new_markdown = []
        in_mermaid_block = False
        mermaid_code = []

        for line in markdown.split('\n'):
            if line.strip() == '```mermaid':
                in_mermaid_block = True
                mermaid_code = []
            elif line.strip() == '```' and in_mermaid_block:
                in_mermaid_block = False
                # Convert Mermaid code to image
                image_path = self.convert_mermaid_to_image('\n'.join(mermaid_code), output_dir)
                # Replace code block with image reference
                relative_image_path = os.path.relpath(image_path, page_dir)
                image_class = self.config['image_class']
                new_markdown.append(f'<img alt="Mermaid Diagram" src="{relative_image_path}" class="{image_class}">')
            elif in_mermaid_block:
                mermaid_code.append(line)
            else:
                new_markdown.append(line)

        return '\n'.join(new_markdown)

    def convert_mermaid_to_image(self, mermaid_code, output_dir):
        """
        This method converts Mermaid code to an image using mermaid.cli.
        """
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mmd') as temp_file:
            temp_file.write(mermaid_code.encode('utf-8'))
            temp_file_path = temp_file.name

        image_format = self.config['image_format']
        output_file_path = os.path.join(output_dir, os.path.basename(temp_file_path) + f'.{image_format}')

        # Create a temporary config file for Mermaid
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as config_file:
            config_file.write(json.dumps(self.config['mermaid_config']).encode('utf-8'))
            config_file_path = config_file.name

        # Prepare the mermaid-cli command
        command = ['mmdc', '-i', temp_file_path, '-o', output_file_path, '-c', config_file_path]

        # Only add the scale option if the output format is 'png'
        if image_format == 'png':
            scale = self.config.get('scale', 1)
            command.extend(['--scale', str(scale)])

        # Run mermaid.cli to convert the Mermaid code to an image
        subprocess.run(command, check=True)

        # Clean up the temporary files
        os.remove(temp_file_path)
        os.remove(config_file_path)

        return output_file_path