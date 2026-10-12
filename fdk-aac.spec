Name:           fdk-aac
Version:        3.0.0
Release:        %autorelease
Summary:        Fraunhofer FDK AAC Codec Library

License:        FDK-AAC
URL:            https://github.com/mstorsjo/fdk-aac
Source0:        %url/archive/v%{version}/fdk-aac-%{version}.tar.gz

BuildSystem:    cmake
BuildOption(conf): -DCMAKE_INSTALL_LIBDIR=%{_lib}/fdk-aac

BuildRequires:  gcc-c++

%description
The Fraunhofer FDK AAC Codec Library ("FDK AAC Codec") is software that
implements the MPEG Advanced Audio Coding ("AAC") encoding and decoding
scheme for digital audio.

%package        devel
Summary:        Development files for fdk-aac
Requires:       fdk-aac%{?_isa} = %{version}-%{release}

%description    devel
The fdk-aac-devel package contains libraries and header files for
developing applications that use fdk-aac.

%prep
%autosetup -p1

%install -a
mv %{buildroot}%{_libdir}/fdk-aac/cmake/ %{buildroot}%{_libdir}/cmake/

# ld.so.conf.d file
mv %{buildroot}%{_libdir}/fdk-aac/pkgconfig/ %{buildroot}%{_libdir}/pkgconfig/
install -m 0755 -d  %{buildroot}%{_sysconfdir}/ld.so.conf.d/
echo -e "%{_libdir}/fdk-aac/ \n" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/fdk-aac-%{_lib}.conf

%ldconfig_scriptlets

%files
%doc ChangeLog
%license NOTICE
%config %{_sysconfdir}/ld.so.conf.d/fdk-aac-%{_lib}.conf
%dir %{_libdir}/fdk-aac/
%{_libdir}/fdk-aac/libfdk-aac.so.2*
%{_libdir}/fdk-aac/libfdk-xhe-aac.so.0*

%files devel
%{_libdir}/cmake/fdk-aac/
%{_libdir}/cmake/fdk-xhe-aac/
%{_libdir}/pkgconfig/fdk-aac.pc
%{_libdir}/pkgconfig/fdk-xhe-aac.pc
%{_includedir}/fdk-aac/
%{_includedir}/fdk-xhe-aac/
%{_libdir}/fdk-aac/libfdk-aac.so
%{_libdir}/fdk-aac/libfdk-xhe-aac.so

%changelog
%autochangelog