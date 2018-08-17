# conan-eigen

![conan-eigen image](/images/conan-eigen.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/eigen%3Aconan/images/download.svg?version=3.3.4%3Astable)](https://bintray.com/conan-community/conan/eigen%3Aconan/3.3.4%3Astable/link)
[![Build Status](https://travis-ci.org/conan-community/conan-eigen.svg?branch=stable%2F3.3.4)](https://travis-ci.org/conan-community/conan-eigen)

[Conan.io](https://conan.io) package for [Eigen](https://bitbucket.org/eigen/eigen) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conan-community/conan/eigen%3Aconan).

## For Users: Use this package

### Basic setup

    $ conan install eigen/3.3.4@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    eigen/3.3.4@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)
