Name:           pCloudCC
Version:        2.0.1.1
Release:        beta4%{?dist}
Summary:        This is a simple linux console client for pCloud cloud storage.

License:        Copyright (c) 2013-2016 pCloud Ltd
URL:            https://github.com/pcloudcom/console-client
Source0:        https://github.com/pcloudcom/console-client/archive/master.zip

Patch0: 	fuseallaccess.patch

BuildRequires:  git zlib-devel boost-devel boost-static fuse-devel glibc-devel cmake gcc systemd-devel boost-system boost-program-options gcc-c++
Requires:       fuse redhat-lsb-core


%description    
pCloud Drive console-client is a console client application that creates a secure virtual hard drive on your computer that you can easily use to store, access, and work on your files in the cloud.


%prep
%setup -n console-client-master

%patch0

%build
cd $RPM_BUILD_DIR/console-client-master/pCloudCC/lib/pclsync/
make clean
make fs
cd ../mbedtls/
cmake .
make clean
make
cd ../..
cmake .
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib64 && mkdir -p $RPM_BUILD_ROOT/usr/bin
cd $RPM_BUILD_DIR/console-client-master/pCloudCC
cp libpcloudcc_lib.so $RPM_BUILD_ROOT/usr/lib64/
cp pcloudcc $RPM_BUILD_ROOT/usr/bin/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc
/usr/bin/pcloudcc
/usr/lib64/libpcloudcc_lib.so



%changelog
* Tue Apr 30 2019 bigornoo <rpm@jfoto.fr> 2.0.1.beta4
- Patch pfs.c for fuse *allow_others* option 

* Mon Apr 29 2019 bigornoo <rpm@jfoto.fr> 2.0.1.beta3
- Change name

* Wed Jan 09 2019 bigornoo <rpm@jfoto.fr> 2.0.1.beta2
- Use of git repo on Github

* Tue Jan 08 2019 bigornoo <rpm@jfoto.fr> 2.0.1.beta1
- First build
