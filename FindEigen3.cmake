find_package(Eigen3 3.3 QUIET CONFIG)
if(TARGET Eigen3::Eigen)
    return()
endif()

# else check pkgconfig and conan
find_package(PkgConfig QUIET)
pkg_check_modules(PC_Eigen3 QUIET Eigen3)

find_path(Eigen3_INCLUDE_DIR
        NAMES "signature_of_eigen3_matrix_library"
        HINTS
            ${Eigen3_DIR}
            ${Eigen3_ROOT_DIR}
        PATHS
            ${CONAN_EIGEN_ROOT}
            ${PC_eigen3_INCLUDE_DIRS}
        PATH_SUFFIXES eigen3)

find_file(Eigen3_version_file
        NAME "Eigen/src/Core/util/Macros.h"
        PATHS ${Eigen3_INCLUDE_DIR})

file(STRINGS ${Eigen3_version_file} version_vars
        REGEX "EIGEN_WORLD_VERSION [0-9]|EIGEN_MAJOR_VERSION [0-9]|EIGEN_MINOR_VERSION [0-9]")

list(TRANSFORM version_vars REPLACE "#define EIGEN_(WORLD|MAJOR|MINOR)_VERSION ([0-9])" "\\2")
list(JOIN version_vars "." Eigen3_VERSION)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Eigen3
        REQUIRED_VARS Eigen3_INCLUDE_DIR
        VERSION_VAR Eigen3_VERSION)

if(Eigen3_FOUND)
    set(Eigen3_INCLUDE_DIRS ${Eigen3_INCLUDE_DIR})
    add_library(Eigen3::Eigen INTERFACE IMPORTED)
    target_include_directories(Eigen3::Eigen INTERFACE ${Eigen3_INCLUDE_DIR})
endif()