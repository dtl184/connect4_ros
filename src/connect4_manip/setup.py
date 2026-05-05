from setuptools import find_packages, setup

package_name = 'connect4_manip'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='danie',
    maintainer_email='danie@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        "console_scripts": [
            "arm_manip_node = connect4_manip.arm_manip_node:main",
            'pick_and_drop_action_server = connect4_manip.pick_and_drop_action_server:main',
            'reset_board_action_server = connect4_manip.reset_board_action_server:main',
            'pick_and_place_action_server = connect4_manip.pick_and_place_action_server:main',
        ],
    },
)
