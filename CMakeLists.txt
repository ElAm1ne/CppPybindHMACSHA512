cmake_minimum_required(VERSION 3.10)
project(hmac-cpp)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /EHsc")

include_directories(hmac-cpp)


add_subdirectory(hmac-cpp/pybind11)


# Specify that the source files are in the hmac-cpp subdirectory
add_executable(hmac-cpp hmac-cpp/code_blocks/example/main.cpp hmac-cpp/sha256.cpp hmac-cpp/sha512.cpp)

pybind11_add_module(hmac_cpp hmac-cpp/bindings.cpp hmac-cpp/sha256.cpp hmac-cpp/sha512.cpp)
