from setuptools import setup


config = {
    "name": "hub",
    "version": "3.0.0",
    "description": "Activeloop Deep Lake",
    "long_description": "Use deeplake instead: pip install deeplake",
    "author": "activeloop.ai",
    "author_email": "support@activeloop.ai",
    "install_requires": ["deeplake"],
    "zip_safe": False,
    "url":"https://www.github.com/activeloopai/deeplake",
}

setup(**config)