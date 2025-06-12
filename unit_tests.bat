cd build
cmake ..
cmake --build .
ctest -C Debug --output-on-failure
