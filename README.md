# conan-eigen

![conan-eigen image](/images/conan-eigen.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/eigen%3Aconan/images/download.svg)](https://bintray.com/conan-community/conan/eigen%3Aconan/_latestVersion)
[![Build status](https://ci.appveyor.com/api/projects/status/jyeh443gn0l0f3bi/branch/stable/3.3.5?svg=true)](https://ci.appveyor.com/project/danimtb/conan-eigen/branch/stable/3.3.5)

[Conan.io](https://conan.io) package for [Eigen](https://bitbucket.org/eigen/eigen) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conan-community/conan/eigen%3Aconan).

## For Users: Use this package

### Basic setup

    $ conan install eigen/3.3.5@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    eigen/3.3.5@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)
