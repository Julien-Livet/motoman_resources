from setuptools import find_packages, setup

package_name = 'motoman_resources'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/urdf',
            ['urdf/common_colors.xacro',
             'urdf/common_materials.xacro',]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='julien',
    maintainer_email='julien.livet@free.fr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
