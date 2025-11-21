cmake_minimum_required(VERSION 3.15)
project(algorithms_with_c C)

file(GLOB SOURCES "source/*.c")
file(GLOB HEADERS "include/*.h")

add_library(${PROJECT_NAME} ${SOURCES} ${HEADERS})
target_include_directories(${PROJECT_NAME} PUBLIC include)

install(TARGETS ${PROJECT_NAME})
install(DIRECTORY include/ DESTINATION include)
