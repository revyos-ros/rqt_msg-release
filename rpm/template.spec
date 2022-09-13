%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-rqt-msg
Version:        1.1.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rqt_msg package

License:        BSD
URL:            http://wiki.ros.org/rqt_msg
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python%{python3_pkgversion}-catkin_pkg
Requires:       ros-galactic-python-qt-binding >= 0.2.19
Requires:       ros-galactic-rclpy
Requires:       ros-galactic-rqt-console
Requires:       ros-galactic-rqt-gui
Requires:       ros-galactic-rqt-gui-py
Requires:       ros-galactic-rqt-py-common
Requires:       ros-galactic-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
A Python GUI plugin for introspecting available ROS message types. Note that the
msgs available through this plugin is the ones that are stored on your machine,
not on the ROS core your rqt instance connects to.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/galactic"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Tue Sep 13 2022 Audrow Nash <audrow@openrobotics.org> - 1.1.0-1
- Autogenerated by Bloom

* Tue Aug 31 2021 Dirk Thomas <dthomas@osrfoundation.org> - 1.0.5-1
- Autogenerated by Bloom

* Tue Apr 27 2021 Dirk Thomas <dthomas@osrfoundation.org> - 1.0.4-1
- Autogenerated by Bloom

* Tue Apr 20 2021 Dirk Thomas <dthomas@osrfoundation.org> - 1.0.3-2
- Autogenerated by Bloom

* Mon Apr 12 2021 Dirk Thomas <dthomas@osrfoundation.org> - 1.0.3-1
- Autogenerated by Bloom

* Mon Mar 08 2021 Dirk Thomas <dthomas@osrfoundation.org> - 1.0.2-2
- Autogenerated by Bloom

