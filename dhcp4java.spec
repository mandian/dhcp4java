%{?_javapackages_macros:%_javapackages_macros}

Summary:	A Java DHCP API suitable for client, server, relay... development
Name:		dhcp4java
Version:	1.00
Release:	1
License:	LGPLv2.1+
Group:		Development/Java
URL:		https://sourceforge.net/projects/dhcp4java/
#Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{name}-%{version}/%{name}-%{version}.src.zip
# svn checkout svn://svn.code.sf.net/p/dhcp4java/code/trunk dhcp4java-code
# cp -far dhcp4java-code dhcp4java-1.00
# find dhcp4java-1.00 -name \.svn -type d -exec rm -fr ./{} \; 2> /dev/null
# find dhcp4java-1.00 -name \.jar -type f -delete 2> /dev/null
# tar Jcf dhcp4java-1.00.tar.xz dhcp4java-1.00
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	ant

%description
A Java DHCP API suitable for client, server, relay... development.

This API is used in the "dhcpd-j" server.

%files
%{_javadir}/%{name}*.jar
%doc src/org/dhcp4java/examples/

#----------------------------------------------------------------------------

%package javadoc
Summary:	API documentation for %{oname}

%description javadoc
API documentation for %{oname}.

%files javadoc
%doc %{_javadocdir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q
# Delete all pre-build binaries
find . -name "*.jar" -delete
find . -name "*.class" -delete

%build
%ant jar javadoc-api

# fix jar-not-indexed warning
pushd _dist
%jar -i %{name}-%{version}.jar
popd

# javadoc
unzip _dist/dhcp4java-1.00.javadoc.zip

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/
install -pm 0644 _dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc-api/* %{buildroot}%{_javadocdir}/%{name}

