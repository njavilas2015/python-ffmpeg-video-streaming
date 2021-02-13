from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='new-ffmpeg-video-streaming',
    url='https://www.insertmendoza.com.ar/njavilas/package/streaming',
    author='Javier Avila',
    author_email='njavilas@insertmendoza.com.ar',
    # Needed to actually package something
    packages=['ffmpeg_streaming'],
    # Needed for dependencies
    install_requires=['django_minio_backend', 'django'],
    # *strongly* suggested for sharing
    version='0.2',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
