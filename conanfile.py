from conans import ConanFile, tools, CMake
import os
from glob import glob


class EigenConan(ConanFile):
    name = "eigen"
    version = "3.3.4"
    url = "http://bitbucket.org/eigen/eigen"
    homepage = "http://eigen.tuxfamily.org"
    description = "Eigen is a C++ template library for linear algebra: matrices, vectors, \
                   numerical solvers, and related algorithms."
    license = "Mozilla Public License Version 2.0"
    no_copy_source = True
    options = {"EIGEN_USE_BLAS": [True, False],
               "EIGEN_USE_LAPACKE": [True, False],
               "EIGEN_USE_LAPACKE_STRICT": [True, False]}
    default_options = "EIGEN_USE_BLAS=False", "EIGEN_USE_LAPACKE=False", "EIGEN_USE_LAPACKE_STRICT=False"

    @property
    def source_subfolder(self):
        return "sources"

    def source(self):
        tools.get("{0}/get/{1}.tar.gz".format(self.url, self.version))
        os.rename(glob("eigen-eigen-*")[0], self.source_subfolder)

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder)
        cmake.install()
        self.copy("COPYING.*", dst="licenses", src=self.source_subfolder,
                  ignore_case=True, keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['include/eigen3']
        if self.options.EIGEN_USE_BLAS:
            self.cpp_info.defines.append("EIGEN_USE_BLAS")

        if self.options.EIGEN_USE_LAPACKE:
            self.cpp_info.defines.append("EIGEN_USE_LAPACKE")

        if self.options.EIGEN_USE_LAPACKE_STRICT:
            self.cpp_info.defines.append("EIGEN_USE_LAPACKE_STRICT")
