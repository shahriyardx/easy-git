from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from setuptools import find_packages, setup

current_directory = Path(__file__).parent.resolve()

long_description = (current_directory / "README.md").read_text(encoding="utf-8")

vpath = current_directory / "eg" / "__init__.py"
spec = spec_from_file_location(vpath.name[:-3], vpath)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)

setup(
    name="easy-git",
    version=mod.__version__,
    description="Common git operations made simple",  # Optional
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shahriyardx/gut",
    author="Md Shahriyar Alam",
    author_email="contact@shahriyar.dev",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={"console_scripts": ["eg = eg:cli"]},
    keywords="git",
    packages=find_packages(),
    python_requires=">=3.6, <4",
)
