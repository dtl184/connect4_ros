from setuptools import find_packages, setup

package_name = 'connect4_perception'

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
        'console_scripts': ['board_perception_node = connect4_perception.board_perception_node:main',
        'block_pose_detector_node = connect4_perception.block_pose_detector_node:main',
        ],
    },
)
