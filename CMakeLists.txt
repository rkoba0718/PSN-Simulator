cmake_minimum_required(VERSION 3.15)
project(PSNSimulator)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(MSVC)
  set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>" CACHE STRING "" FORCE)
  set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
endif()

enable_testing()

add_subdirectory(src)
add_subdirectory(tests)
