from setuptools import setup


config = {
    "name": "hub",
    "version": "2.8.6",
    "description": "Activeloop Hub",
    "long_description": "...",
    "long_description_content_type": "text/x-rst",
    "author": "activeloop.ai",
    "author_email": "support@activeloop.ai",
    "install_requires": ["deeplake"],
    "zip_safe": False,
    "url": "https://www.github.com/activeloopai/hub",
}

setup(**config)
