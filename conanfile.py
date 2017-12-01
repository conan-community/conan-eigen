#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os
from glob import glob


class EigenConan(ConanFile):
    name = "eigen"
    url = "http://eigen.tuxfamily.org"
    description = "Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms."
    license = "http://eigen.tuxfamily.org/index.php?title=Main_Page#License"

    def source(self):
        source_url = "https://bitbucket.org/eigen/eigen"
        tools.get("{0}/get/{1}.tar.gz".format(source_url, self.version))
        os.rename(glob("eigen-eigen-*")[0], "sources")
        #Rename to "sources" is a convention to simplify later steps

    def package(self):
        self.copy(pattern="*", dst="include/Eigen", src="sources/Eigen")

    def package_id(self):
        self.info.header_only()
