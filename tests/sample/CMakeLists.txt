set(SAMPLE_TEST_SOURCES
    sample_test.cpp
)

add_executable(SampleUnitTest ${SAMPLE_TEST_SOURCES})
target_link_libraries(SampleUnitTest
    PRIVATE
        gtest_main
)

add_test(NAME SampleUnitTest COMMAND SampleUnitTest)
