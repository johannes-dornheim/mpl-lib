from distutils.core import setup
setup(name='MPL_personal_lib',
      version='0.1',
      description='collection of personal matplotlib lib',
      author='Youngung Jeong',
      author_email='youngung.jeong@gmail.com',
      packages=['mpl_lib','mech'],
      package_dir={'mpl_lib':'src/mpl_lib','mech':'src/mech'}
)
