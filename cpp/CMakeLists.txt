aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR} PROB_SRCS)

add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND})

foreach(prob_path ${PROB_SRCS})
    get_filename_component(prob_name ${prob_path} NAME)
    get_filename_component(prob_ext ${prob_name} EXT)
    string(REPLACE "${prob_ext}" "" prob_no_ext ${prob_name})

    add_executable(${prob_no_ext} ${prob_path})
    add_test(${prob_no_ext} ${prob_no_ext})
    add_dependencies(check ${prob_no_ext})
endforeach()