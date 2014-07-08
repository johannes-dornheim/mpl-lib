from distutils.core import setup
setup(name='MPL_personal_lib',
      version='0.1',
      description='collection of personal matplotlib lib',
      author='Youngung Jeong',
      author_email='youngung.jeong@gmail.com',
      packages=['MP','MP.lib','MP.mat','MP.opt'],
      package_dir={'MP':'src',
                   'MP.lib':'src/lib',
                   'MP.mat':'src/mat',
                   'MP.opt':'src/opt'}
      )
