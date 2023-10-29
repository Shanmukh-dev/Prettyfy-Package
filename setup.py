from setuptools import setup, find_packages

setup(name = "prettyfy",
      version = 0.1,
      description= "A package of the students to beautify their console",
      author= "T S Shannmukh Vshtav",
      packages=["prettyfy"],
      install_requires = ["windows-curses; sys_platform == 'win32'",],
      entry_points = {
          'console_scripts': [
              "prettyfy = prettyfy.safe_exec:safe_exec"
          ],
      },
      )