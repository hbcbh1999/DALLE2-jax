from setuptools import setup, find_packages

setup(
  name = 'DALLE2-jax',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Implementation DALL-E2, OpenAI\'s updated text-to-image artificial neural network, in Jax',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/DALLE2-jax',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'text-to-image'
  ],
  install_requires=[
    'einops==0.4',
    'equinox>=0.4',
    'jax>=0.3.4',
    'jaxlib>=0.1',
    'numpy'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
