cmake_minimum_required(VERSION 3.14)
project(TP4_DistributedSystem CXX)

set(CMAKE_CXX_STANDARD 17)

# Find the required libraries
find_package(cpr REQUIRED)
find_package(nlohmann_json REQUIRED)
find_package(Eigen3 REQUIRED)

# Create the Boss executable
add_executable(boss boss.cpp)
# Link CPR and JSON, and include Eigen
target_link_libraries(boss PRIVATE cpr::cpr nlohmann_json::nlohmann_json Eigen3::Eigen)

# Create the Minion executable
add_executable(minion minion.cpp)
target_link_libraries(minion PRIVATE cpr::cpr nlohmann_json::nlohmann_json Eigen3::Eigen)