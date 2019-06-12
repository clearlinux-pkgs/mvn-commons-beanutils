#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-beanutils
Version  : 1.6
Release  : 1
URL      : https://repo1.maven.org/maven2/commons-beanutils/commons-beanutils/1.6/commons-beanutils-1.6.jar
Source0  : https://repo1.maven.org/maven2/commons-beanutils/commons-beanutils/1.6/commons-beanutils-1.6.jar
Source1  : https://repo1.maven.org/maven2/commons-beanutils/commons-beanutils-core/1.8.3/commons-beanutils-core-1.8.3.jar
Source2  : https://repo1.maven.org/maven2/commons-beanutils/commons-beanutils-core/1.8.3/commons-beanutils-core-1.8.3.pom
Source3  : https://repo1.maven.org/maven2/commons-beanutils/commons-beanutils/1.6/commons-beanutils-1.6.pom
Source4  : https://repo1.maven.org/maven2/commons-beanutils/commons-beanutils/1.7.0/commons-beanutils-1.7.0.jar
Source5  : https://repo1.maven.org/maven2/commons-beanutils/commons-beanutils/1.7.0/commons-beanutils-1.7.0.pom
Source6  : https://repo1.maven.org/maven2/commons-beanutils/commons-beanutils/1.9.2/commons-beanutils-1.9.2.jar
Source7  : https://repo1.maven.org/maven2/commons-beanutils/commons-beanutils/1.9.2/commons-beanutils-1.9.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-1.1 Apache-2.0
Requires: mvn-commons-beanutils-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-beanutils package.
Group: Data

%description data
data components for the mvn-commons-beanutils package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/s/1.6
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/s/1.6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/s/1.6
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/s/1.6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/s/1.7.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/s/1.7.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/s/1.7.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/s/1.7.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/s/1.9.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/s/1.9.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/s/1.9.2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/s/1.9.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/e/1.8.3
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/e/1.8.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/e/1.8.3
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/commons-beanutils/e/1.8.3


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/commons-beanutils/e/1.8.3/commons-beanutils-1.9.2.jar
/usr/share/java/.m2/repository/commons-beanutils/e/1.8.3/commons-beanutils-1.9.2.pom
/usr/share/java/.m2/repository/commons-beanutils/s/1.6/commons-beanutils-1.6.jar
/usr/share/java/.m2/repository/commons-beanutils/s/1.6/commons-beanutils-core-1.8.3.jar
/usr/share/java/.m2/repository/commons-beanutils/s/1.7.0/commons-beanutils-1.6.pom
/usr/share/java/.m2/repository/commons-beanutils/s/1.7.0/commons-beanutils-core-1.8.3.pom
/usr/share/java/.m2/repository/commons-beanutils/s/1.9.2/commons-beanutils-1.7.0.jar
/usr/share/java/.m2/repository/commons-beanutils/s/1.9.2/commons-beanutils-1.7.0.pom
