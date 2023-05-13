# CMake generated Testfile for 
# Source directory: /home/vdorbala/catkin_ws/src/geometry2/tf2_kdl
# Build directory: /home/vdorbala/catkin_ws/build/tf2_kdl
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_tf2_kdl_rostest_test_test.launch "/home/vdorbala/catkin_ws/build/tf2_kdl/catkin_generated/env_cached.sh" "/scratch/miniconda3/envs/py38/bin/python3" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/vdorbala/catkin_ws/build/tf2_kdl/test_results/tf2_kdl/rostest-test_test.xml" "--return-code" "/scratch/miniconda3/envs/py38/bin/python3 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/vdorbala/catkin_ws/src/geometry2/tf2_kdl --package=tf2_kdl --results-filename test_test.xml --results-base-dir \"/home/vdorbala/catkin_ws/build/tf2_kdl/test_results\" /home/vdorbala/catkin_ws/src/geometry2/tf2_kdl/test/test.launch ")
add_test(_ctest_tf2_kdl_rostest_test_test_python.launch "/home/vdorbala/catkin_ws/build/tf2_kdl/catkin_generated/env_cached.sh" "/scratch/miniconda3/envs/py38/bin/python3" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/vdorbala/catkin_ws/build/tf2_kdl/test_results/tf2_kdl/rostest-test_test_python.xml" "--return-code" "/scratch/miniconda3/envs/py38/bin/python3 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/vdorbala/catkin_ws/src/geometry2/tf2_kdl --package=tf2_kdl --results-filename test_test_python.xml --results-base-dir \"/home/vdorbala/catkin_ws/build/tf2_kdl/test_results\" /home/vdorbala/catkin_ws/src/geometry2/tf2_kdl/test/test_python.launch ")
subdirs("gtest")
