from setuptools import setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/talker_listener.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Workshop',
    maintainer_email='you@example.com',
    description='ROS 2 workshop example (Python)',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = my_py_pkg.talker:main',
            'listener = my_py_pkg.listener:main',
        ],
    },
)
