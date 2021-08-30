from setuptools import setup

setup(
    name='team2-hw2b',
    version='0.1',
    description='NCSU SE Fall 2021 HW 2B',
    author='Team 2',
    author_email='software.engineers@email.com',
    url='https://github.com/shikhanair/team2-hw2b/',
    packages=['ncsu-swe-f21-team2-hw2b'],
      long_description="""\
        Submission for Homework 2.
      """,
      classifiers=[
          "License :: MIT",
          "Programming Language :: Python",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Homework",
      ],
      keywords='se-hw se-hw2b',
      license='MIT',
      install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow'
      ],
      )
