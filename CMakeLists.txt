cmake_minimum_required(VERSION 3.10)
project(hmac-cpp)
set(CMAKE_CXX_STANDARD 11)

if(MSVC)
    add_compile_options(/EHsc)
else()
    add_compile_options(-Wall -Wextra -pedantic)
endif()

include_directories(hmac-cpp)

add_subdirectory(hmac-cpp/pybind11)

add_executable(hmac-cpp hmac-cpp/code_blocks/example/main.cpp hmac-cpp/sha256.cpp hmac-cpp/sha512.cpp)
pybind11_add_module(hmac_cpp hmac-cpp/bindings.cpp hmac-cpp/sha256.cpp hmac-cpp/sha512.cpp)
