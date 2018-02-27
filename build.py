from conan.packager import ConanMultiPackager
import os, re, platform


def get_value_from_recipe(search_string):
    with open("conanfile.py", "r") as conanfile:
        contents = conanfile.read()
        result = re.search(search_string, contents)
    return result

def get_name_from_recipe():
    return get_value_from_recipe(r'''name\s*=\s*["'](\S*)["']''').groups()[0]


if __name__ == "__main__":
    name = get_name_from_recipe()
    username = "conan"
    channel = "stable"
    login_username = "conanbot"
    upload_remote = "https://api.bintray.com/conan/conan-community/{0}".format(username)

        builder = ConanMultiPackager(
            username=username,
            channel=channel,
            login_username=login_username,
            reference=reference,
            upload=upload_remote,
            remotes=upload_remote)
    
    for version in ["3.1.4", "3.2.10", "3.3.4"]:
        reference = "{0}/{1}".format(name, version)
        builder.add(settings={"os":"Windows",
                              "compiler":"Visual Studio",
                              "compiler.version":"15",
                              "build_type":"Release",
                              "arch":"x86_64"},
                    options=None,
                    env_vars=None,
                    reference=reference)
        builder.run()
