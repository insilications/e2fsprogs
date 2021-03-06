#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : e2fsprogs
Version  : 1.46.4
Release  : 301
URL      : https://sourceforge.net/projects/e2fsprogs/files/e2fsprogs/v1.46.4/e2fsprogs-1.46.4.tar.gz
Source0  : https://sourceforge.net/projects/e2fsprogs/files/e2fsprogs/v1.46.4/e2fsprogs-1.46.4.tar.gz
Summary  : Utilities for managing ext2/ext3/ext4 filesystems
Group    : Development/Tools
License  : GPL-2.0
Requires: e2fsprogs-bin = %{version}-%{release}
Requires: e2fsprogs-data = %{version}-%{release}
Requires: e2fsprogs-info = %{version}-%{release}
Requires: e2fsprogs-lib = %{version}-%{release}
Requires: e2fsprogs-libexec = %{version}-%{release}
Requires: e2fsprogs-locales = %{version}-%{release}
Requires: e2fsprogs-man = %{version}-%{release}
Requires: e2fsprogs-services = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : acl-dev32
BuildRequires : attr-dev
BuildRequires : attr-dev32
BuildRequires : autoconf-archive-dev
BuildRequires : bison
BuildRequires : buildreq-distutils3
BuildRequires : file-dev
BuildRequires : fuse-dev
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gettext
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(udev)
BuildRequires : procps-ng
BuildRequires : systemd-dev32
BuildRequires : texinfo
BuildRequires : util-linux-dev
BuildRequires : util-linux-dev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: stateless.patch
Patch2: build.patch
Patch3: 0001-Adapt-to-autoconf-2.70-and-gettext-0.21.patch

%description
The e2fsprogs package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in ext2, ext3,
and ext4 filesystems.  E2fsprogs contains e2fsck (used to repair
filesystem inconsistencies after an unclean shutdown), mke2fs (used to
initialize a partition to contain an empty ext2 filesystem), debugfs
(used to examine the internal structure of a filesystem, to manually
repair a corrupted filesystem or to create test cases for e2fsck),
tune2fs (used to modify filesystem parameters), resize2fs to grow and
shrink unmounted ext2 filesystems, and most of the other core ext2fs
filesystem utilities.

You should install the e2fsprogs package if you are using any ext2,
ext3, or ext4 filesystems (if you're not sure, you probably should
install this package).  You may also need to install it (even if you
don't use ext2/ext3/ext4) for the libuuid and libblkid libraries and
fsck tool that are included here.

%package bin
Summary: bin components for the e2fsprogs package.
Group: Binaries
Requires: e2fsprogs-data = %{version}-%{release}
Requires: e2fsprogs-libexec = %{version}-%{release}
Requires: e2fsprogs-services = %{version}-%{release}

%description bin
bin components for the e2fsprogs package.


%package data
Summary: data components for the e2fsprogs package.
Group: Data

%description data
data components for the e2fsprogs package.


%package dev
Summary: dev components for the e2fsprogs package.
Group: Development
Requires: e2fsprogs-lib = %{version}-%{release}
Requires: e2fsprogs-bin = %{version}-%{release}
Requires: e2fsprogs-data = %{version}-%{release}
Provides: e2fsprogs-devel = %{version}-%{release}
Requires: e2fsprogs = %{version}-%{release}

%description dev
dev components for the e2fsprogs package.


%package dev32
Summary: dev32 components for the e2fsprogs package.
Group: Default
Requires: e2fsprogs-lib32 = %{version}-%{release}
Requires: e2fsprogs-bin = %{version}-%{release}
Requires: e2fsprogs-data = %{version}-%{release}
Requires: e2fsprogs-dev = %{version}-%{release}

%description dev32
dev32 components for the e2fsprogs package.


%package extras
Summary: extras components for the e2fsprogs package.
Group: Default

%description extras
extras components for the e2fsprogs package.


%package info
Summary: info components for the e2fsprogs package.
Group: Default

%description info
info components for the e2fsprogs package.


%package lib
Summary: lib components for the e2fsprogs package.
Group: Libraries
Requires: e2fsprogs-data = %{version}-%{release}
Requires: e2fsprogs-libexec = %{version}-%{release}

%description lib
lib components for the e2fsprogs package.


%package lib32
Summary: lib32 components for the e2fsprogs package.
Group: Default
Requires: e2fsprogs-data = %{version}-%{release}

%description lib32
lib32 components for the e2fsprogs package.


%package libexec
Summary: libexec components for the e2fsprogs package.
Group: Default

%description libexec
libexec components for the e2fsprogs package.


%package locales
Summary: locales components for the e2fsprogs package.
Group: Default

%description locales
locales components for the e2fsprogs package.


%package man
Summary: man components for the e2fsprogs package.
Group: Default

%description man
man components for the e2fsprogs package.


%package services
Summary: services components for the e2fsprogs package.
Group: Systemd services

%description services
services components for the e2fsprogs package.


%package staticdev
Summary: staticdev components for the e2fsprogs package.
Group: Default
Requires: e2fsprogs-dev = %{version}-%{release}

%description staticdev
staticdev components for the e2fsprogs package.


%package staticdev32
Summary: staticdev32 components for the e2fsprogs package.
Group: Default
Requires: e2fsprogs-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the e2fsprogs package.


%prep
%setup -q -n e2fsprogs-1.46.4
cd %{_builddir}/e2fsprogs-1.46.4
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd %{_builddir}
cp -a %{_builddir}/e2fsprogs-1.46.4 build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630128943
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export CXXFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export FCFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export CFFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export LDFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags1 end
sd -r '\s--dirty\s' ' ' .
sd -r 'git describe' 'git describe --abbrev=0' .
%reconfigure --enable-shared \
--enable-static \
--disable-fsck \
--disable-libblkid \
--disable-uuidd \
--disable-libuuid \
--enable-elf-shlibs
make    V=1 VERBOSE=1

pushd ../build32/
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
unset CPATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
unset ASFLAGS
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
unset CFFLAGS
unset LDFLAGS
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export FCFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export FFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export CFFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
%reconfigure --enable-shared \
--enable-static \
--disable-fsck \
--disable-libblkid \
--disable-uuidd \
--disable-libuuid \
--enable-elf-shlibs  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make    V=1 VERBOSE=1
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
make -j16 check V=1 VERBOSE=1

%install
export SOURCE_DATE_EPOCH=1630128943
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
    pushd %{buildroot}/usr/lib32/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
popd
%make_install
%find_lang e2fsprogs
## Remove excluded files
rm -f %{buildroot}/usr/bin/uuidgen
rm -f %{buildroot}/usr/lib32/e2fsprogs/e2scrub_all_cron
rm -f %{buildroot}/usr/lib32/e2fsprogs/e2scrub_fail
rm -f %{buildroot}/usr/lib32/e2initrd_helper
rm -f %{buildroot}/usr/lib64/e2fsprogs/e2scrub_all_cron
rm -f %{buildroot}/usr/share/man/man1/uuidgen.1
## install_append content
%make_install install-libs
mkdir -p %{buildroot}/usr/libexec
mv %{buildroot}/usr/lib64/e2fsprogs/e2scrub_fail %{buildroot}/usr/libexec/
sed -i 's|/usr/lib64/e2fsprogs/|/usr/libexec/|' %{buildroot}/usr/lib/systemd/system/e2scrub_fail@.service
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/e2initrd_helper

%files bin
%defattr(-,root,root,-)
/usr/bin/chattr
/usr/bin/e2fsck
/usr/bin/e2label
/usr/bin/e2mmpstatus
/usr/bin/e2scrub
/usr/bin/e2scrub_all
/usr/bin/e4crypt
/usr/bin/fsck.ext2
/usr/bin/fsck.ext3
/usr/bin/fsck.ext4
/usr/bin/lsattr
/usr/bin/mklost+found
/usr/bin/resize2fs
/usr/bin/tune2fs

%files data
%defattr(-,root,root,-)
/usr/share/defaults/e2fsprogs/mke2fs.conf

%files dev
%defattr(-,root,root,-)
/usr/include/com_err.h
/usr/include/e2p/e2p.h
/usr/include/et/com_err.h
/usr/include/ext2fs/bitops.h
/usr/include/ext2fs/ext2_err.h
/usr/include/ext2fs/ext2_ext_attr.h
/usr/include/ext2fs/ext2_fs.h
/usr/include/ext2fs/ext2_io.h
/usr/include/ext2fs/ext2_types.h
/usr/include/ext2fs/ext2fs.h
/usr/include/ext2fs/ext3_extents.h
/usr/include/ext2fs/hashmap.h
/usr/include/ext2fs/qcow2.h
/usr/include/ext2fs/tdb.h
/usr/include/ss/ss.h
/usr/include/ss/ss_err.h
/usr/lib64/libcom_err.so
/usr/lib64/libe2p.so
/usr/lib64/libext2fs.so
/usr/lib64/libss.so
/usr/lib64/pkgconfig/com_err.pc
/usr/lib64/pkgconfig/e2p.pc
/usr/lib64/pkgconfig/ext2fs.pc
/usr/lib64/pkgconfig/ss.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcom_err.so
/usr/lib32/libe2p.so
/usr/lib32/libext2fs.so
/usr/lib32/libss.so
/usr/lib32/pkgconfig/32com_err.pc
/usr/lib32/pkgconfig/32e2p.pc
/usr/lib32/pkgconfig/32ext2fs.pc
/usr/lib32/pkgconfig/32ss.pc
/usr/lib32/pkgconfig/com_err.pc
/usr/lib32/pkgconfig/e2p.pc
/usr/lib32/pkgconfig/ext2fs.pc
/usr/lib32/pkgconfig/ss.pc

%files extras
%defattr(-,root,root,-)
/usr/bin/badblocks
/usr/bin/compile_et
/usr/bin/debugfs
/usr/bin/dumpe2fs
/usr/bin/e2freefrag
/usr/bin/e2image
/usr/bin/e2undo
/usr/bin/e4defrag
/usr/bin/filefrag
/usr/bin/logsave
/usr/bin/mk_cmds
/usr/bin/mke2fs
/usr/bin/mkfs.ext2
/usr/bin/mkfs.ext3
/usr/bin/mkfs.ext4
/usr/lib/udev/rules.d/96-e2scrub.rules
/usr/share/et/et_c.awk
/usr/share/et/et_h.awk
/usr/share/ss/ct_c.awk
/usr/share/ss/ct_c.sed

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libext2fs.info.gz

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcom_err.so.2
/usr/lib64/libcom_err.so.2.1
/usr/lib64/libe2p.so.2
/usr/lib64/libe2p.so.2.3
/usr/lib64/libext2fs.so.2
/usr/lib64/libext2fs.so.2.4
/usr/lib64/libss.so.2
/usr/lib64/libss.so.2.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcom_err.so.2
/usr/lib32/libcom_err.so.2.1
/usr/lib32/libe2p.so.2
/usr/lib32/libe2p.so.2.3
/usr/lib32/libext2fs.so.2
/usr/lib32/libext2fs.so.2.4
/usr/lib32/libss.so.2
/usr/lib32/libss.so.2.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/e2scrub_fail

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/chattr.1
/usr/share/man/man1/compile_et.1
/usr/share/man/man1/lsattr.1
/usr/share/man/man1/mk_cmds.1
/usr/share/man/man3/com_err.3
/usr/share/man/man5/e2fsck.conf.5
/usr/share/man/man5/ext2.5
/usr/share/man/man5/ext3.5
/usr/share/man/man5/ext4.5
/usr/share/man/man5/mke2fs.conf.5
/usr/share/man/man8/badblocks.8
/usr/share/man/man8/debugfs.8
/usr/share/man/man8/dumpe2fs.8
/usr/share/man/man8/e2freefrag.8
/usr/share/man/man8/e2fsck.8
/usr/share/man/man8/e2image.8
/usr/share/man/man8/e2label.8
/usr/share/man/man8/e2mmpstatus.8
/usr/share/man/man8/e2scrub.8
/usr/share/man/man8/e2scrub_all.8
/usr/share/man/man8/e2undo.8
/usr/share/man/man8/e4crypt.8
/usr/share/man/man8/e4defrag.8
/usr/share/man/man8/filefrag.8
/usr/share/man/man8/fsck.ext2.8
/usr/share/man/man8/fsck.ext3.8
/usr/share/man/man8/fsck.ext4.8
/usr/share/man/man8/logsave.8
/usr/share/man/man8/mke2fs.8
/usr/share/man/man8/mkfs.ext2.8
/usr/share/man/man8/mkfs.ext3.8
/usr/share/man/man8/mkfs.ext4.8
/usr/share/man/man8/mklost+found.8
/usr/share/man/man8/resize2fs.8
/usr/share/man/man8/tune2fs.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/e2scrub@.service
/usr/lib/systemd/system/e2scrub_all.service
/usr/lib/systemd/system/e2scrub_all.timer
/usr/lib/systemd/system/e2scrub_fail@.service
/usr/lib/systemd/system/e2scrub_reap.service

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libcom_err.a
/usr/lib64/libe2p.a
/usr/lib64/libext2fs.a
/usr/lib64/libss.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libcom_err.a
/usr/lib32/libe2p.a
/usr/lib32/libext2fs.a
/usr/lib32/libss.a

%files locales -f e2fsprogs.lang
%defattr(-,root,root,-)
