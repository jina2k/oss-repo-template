cmake_minimum_required(VERSION 3.10)

#name
project(buildBlocks)

#make libs
add_library(libst STATIC source/block.c)
add_library(libsh SHARED source/block.c)

#add exec
add_executable(static_block program.c)
add_executable(dynamic_block program.c)

#link libs
target_link_libraries(static_block libst)
target_link_libraries(dynamic_block libsh)