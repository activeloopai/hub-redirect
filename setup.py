from setuptools import setup


config = {
    "name": "hub-redirect",
    "version": "3.0.2",
    "description": "Activeloop Deep Lake",
    "long_description": "Use deeplake instead: pip install deeplake",
    "long_description_content_type": "text/x-rst",
    "author": "activeloop.ai",
    "author_email": "support@activeloop.ai",
    "install_requires": ["deeplake"],
    "zip_safe": False,
    "url": "https://www.github.com/activeloopai/deeplake",
}

setup(**config)
