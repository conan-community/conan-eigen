from conan.packager import ConanMultiPackager
from conans import tools


if __name__ == "__main__":
    builder = ConanMultiPackager()
    if tools.os_info.is_windows:
        builder.add(settings={"compiler":"Visual Studio", "compiler.version": "16",
                              "arch": "x86", "build_type": "Release"},
                    options={}, env_vars={}, build_requires={})
    elif tools.os_info.is_linux:
        builder.add(settings={"compiler":"gcc", "compiler.version": "8",
                              "arch": "x86_64", "build_type": "Release"},
                    options={}, env_vars={}, build_requires={})
    builder.run()