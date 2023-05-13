^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tf2_eigen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.6.5 (2018-11-16)
------------------

0.6.4 (2018-11-06)
------------------
* improve comments
* add Eigen::Isometry3d conversions
* normalize quaternions to be in half-space w >= 0 as in tf1
* improve computation efficiency
* Contributors: Robert Haschke

0.6.3 (2018-07-09)
------------------

0.6.2 (2018-05-02)
------------------
* Adds toMsg & fromMsg for Eigen Vector3 (`#294 <https://github.com/ros/geometry2/issues/294>`_)
  - Adds toMsg for geometry_msgs::Vector3&  with dual argument syntax to
  avoid an overload conflict with
  geometry_msgs::Point& toMsg(contst Eigen::Vector3d& in)
  - Adds corresponding fromMsg for Eigen Vector3d and
  geometry_msgs::Vector3
  - Fixed typos in description of fromMsg for Twist and Eigen 6x1 Matrix
* Adds additional conversions for tf2, KDL, Eigen (`#292 <https://github.com/ros/geometry2/issues/292>`_)
  - adds non-stamped Eigen to Transform function
  - converts Eigen Matrix Vectors to and from geometry_msgs::Twist
  - adds to/from message for geometry_msgs::Pose and KDL::Frame
* Contributors: Ian McMahon

0.6.1 (2018-03-21)
------------------

0.6.0 (2018-03-21)
------------------

0.5.17 (2018-01-01)
-------------------

0.5.16 (2017-07-14)
-------------------
* fix return value to prevent warnings on windows (`#237 <https://github.com/ros/geometry2/issues/237>`_)
* fixing include directory order to support overlays (`#231 <https://github.com/ros/geometry2/issues/231>`_)
* tf2_eigen: added support for Quaternion and QuaternionStamped (`#230 <https://github.com/ros/geometry2/issues/230>`_)
* Remove an unused variable from the tf2_eigen test. (`#215 <https://github.com/ros/geometry2/issues/215>`_)
* Find eigen in a much nicer way.
* Switch tf2_eigen to use package.xml format 2. (`#216 <https://github.com/ros/geometry2/issues/216>`_)
* Contributors: Chris Lalancette, Mikael Arguedas, Tully Foote, cwecht

0.5.15 (2017-01-24)
-------------------
* fixup `#186 <https://github.com/ros/geometry2/issues/186>`_: inline template specializations (`#200 <https://github.com/ros/geometry2/issues/200>`_)
* Contributors: Robert Haschke

0.5.14 (2017-01-16)
-------------------
* Add tf2_eigen conversions for Pose and Point (not stamped) (`#186 <https://github.com/ros/geometry2/issues/186>`_)
  * tf2_eigen: added conversions for Point msg type (not timestamped) to Eigen::Vector3d
  * tf2_eigen: added conversions for Pose msg type (not timestamped) to Eigen::Affine3d
  * tf2_eigen: new functions are inline now
  * tf2_eigen test compiling again
  * tf2_eigen: added tests for Affine3d and Vector3d conversion
  * tf2_eigen: added redefinitions of non-stamped conversion function to make usage in tf2::convert() possible
  * tf2_eigen: reduced redundancy by reusing non-stamped conversion-functions in their stamped counterparts
  * tf2_eigen: added notes at doTransform-implementations which can not work with tf2_ros::BufferInterface::transform
  * tf2_eigen: fixed typos
* Don't export local include dirs (`#180 <https://github.com/ros/geometry2/issues/180>`_)
* Improve documentation.
* Contributors: Jackie Kay, Jochen Sprickerhof, cwecht

0.5.13 (2016-03-04)
-------------------
* Added missing inline
* Added unit test
  - Testing conversion to msg forward/backward
* Added eigenTotransform function
* Contributors: Davide Tateo, boris-il-forte

0.5.12 (2015-08-05)
-------------------

0.5.11 (2015-04-22)
-------------------

0.5.10 (2015-04-21)
-------------------
* fixing CMakeLists.txt from `#97 <https://github.com/ros/geometry_experimental/issues/97>`_
* create tf2_eigen.
* Contributors: Tully Foote, koji
