from conan import ConanFile
from conan.tools.files import copy
from conan.tools.cmake import CMake, cmake_layout

class AlgorithmsWithCConan(ConanFile):
    name = "algorithms_with_c"
    version = "1.0.0"
    license = "MIT"  # Ajuste conforme sua licença
    author = "Ivan Carlos"
    url = "https://github.com/ivancarlos/algorithms_with_c"
    description = "Algorithms implemented in C89"
    topics = ("algorithms", "c89", "data-structures")
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "include/*", "source/*", "CMakeLists.txt"

    def layout(self):
        cmake_layout(self)

    def package(self):
        copy(self, "*.h", src=self.source_folder + "/include",
             dst=self.package_folder + "/include", keep_path=True)
        copy(self, "*.c", src=self.source_folder + "/source",
             dst=self.package_folder + "/src", keep_path=True)

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.srcdirs = ["src"]
