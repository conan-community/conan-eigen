from conans import ConanFile, tools
import os
from glob import glob


class EigenConan(ConanFile):
    name = "eigen"
    version = "3.3.7"
    url = "https://github.com/conan-community/conan-eigen"
    homepage = "http://eigen.tuxfamily.org"
    description = "Eigen is a C++ template library for linear algebra: matrices, vectors, \
                   numerical solvers, and related algorithms."
    license = "MPL-2.0"
    author = "Conan Community"
    topics = ("eigen", "algebra", "linear-algebra", "vector", "numerical")
    exports = "LICENSE"
    options = {"EIGEN_USE_BLAS": [True, False],
               "EIGEN_USE_LAPACKE": [True, False],
               "EIGEN_USE_LAPACKE_STRICT": [True, False]}
    default_options = {"EIGEN_USE_BLAS": False, "EIGEN_USE_LAPACKE": False, "EIGEN_USE_LAPACKE_STRICT": False}
    no_copy_source = True

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        source_url = "http://bitbucket.org/eigen/eigen"
        sha256 = "7e84ef87a07702b54ab3306e77cea474f56a40afa1c0ab245bb11725d006d0da"
        tools.get("{0}/get/{1}.tar.gz".format(source_url, self.version), sha256=sha256)
        os.rename(glob("eigen-eigen-*")[0], self._source_subfolder)

    def package(self):
        self.copy("COPYING.*", dst="licenses", src=self._source_subfolder)
        self.copy("*", dst=os.path.join("include", "eigen3", "Eigen"), src=os.path.join(self._source_subfolder, "Eigen"))
        self.copy("*", dst=os.path.join("include", "unsupported", "unsupported", "Eigen"), src=os.path.join(self._source_subfolder, "unsupported", "Eigen"))
        os.remove(os.path.join(self.package_folder, "include", "eigen3", "Eigen", "CMakeLists.txt"))
        os.remove(os.path.join(self.package_folder, "include", "unsupported", "unsupported", "Eigen", "CMakeLists.txt"))

    def package_info(self):
        self.cpp_info.includedirs = ['include/eigen3', 'include/unsupported']
        if self.options.EIGEN_USE_BLAS:
            self.cpp_info.defines.append("EIGEN_USE_BLAS")

        if self.options.EIGEN_USE_LAPACKE:
            self.cpp_info.defines.append("EIGEN_USE_LAPACKE")

        if self.options.EIGEN_USE_LAPACKE_STRICT:
            self.cpp_info.defines.append("EIGEN_USE_LAPACKE_STRICT")

        self.env_info.Eigen3_DIR = os.path.join(self.package_folder, "share", "eigen3", "cmake")
