# CMake generated Testfile for 
# Source directory: /home/vdorbala/catkin_ws/src/geometry2/tf2
# Build directory: /home/vdorbala/catkin_ws/build/tf2
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_tf2_gtest_test_cache_unittest "/home/vdorbala/catkin_ws/build/tf2/catkin_generated/env_cached.sh" "/scratch/miniconda3/envs/py38/bin/python3" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/vdorbala/catkin_ws/build/tf2/test_results/tf2/gtest-test_cache_unittest.xml" "--return-code" "/home/vdorbala/catkin_ws/devel/.private/tf2/lib/tf2/test_cache_unittest --gtest_output=xml:/home/vdorbala/catkin_ws/build/tf2/test_results/tf2/gtest-test_cache_unittest.xml")
add_test(_ctest_tf2_gtest_test_static_cache_unittest "/home/vdorbala/catkin_ws/build/tf2/catkin_generated/env_cached.sh" "/scratch/miniconda3/envs/py38/bin/python3" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/vdorbala/catkin_ws/build/tf2/test_results/tf2/gtest-test_static_cache_unittest.xml" "--return-code" "/home/vdorbala/catkin_ws/devel/.private/tf2/lib/tf2/test_static_cache_unittest --gtest_output=xml:/home/vdorbala/catkin_ws/build/tf2/test_results/tf2/gtest-test_static_cache_unittest.xml")
add_test(_ctest_tf2_gtest_test_simple "/home/vdorbala/catkin_ws/build/tf2/catkin_generated/env_cached.sh" "/scratch/miniconda3/envs/py38/bin/python3" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/vdorbala/catkin_ws/build/tf2/test_results/tf2/gtest-test_simple.xml" "--return-code" "/home/vdorbala/catkin_ws/devel/.private/tf2/lib/tf2/test_simple --gtest_output=xml:/home/vdorbala/catkin_ws/build/tf2/test_results/tf2/gtest-test_simple.xml")
subdirs("gtest")
