#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-partykit
Version  : 1.2.3
Release  : 16
URL      : https://cran.r-project.org/src/contrib/partykit_1.2-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/partykit_1.2-3.tar.gz
Summary  : A Toolkit for Recursive Partytioning
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-partykit-lib = %{version}-%{release}
Requires: R-AER
Requires: R-Formula
Requires: R-XML
Requires: R-inum
Requires: R-libcoin
Requires: R-mlbench
Requires: R-party
Requires: R-pmml
BuildRequires : R-AER
BuildRequires : R-Formula
BuildRequires : R-XML
BuildRequires : R-inum
BuildRequires : R-libcoin
BuildRequires : R-mlbench
BuildRequires : R-party
BuildRequires : R-pmml
BuildRequires : buildreq-R

%description
visualizing tree-structured regression and classification models. This
  unified infrastructure can be used for reading/coercing tree models from
  different sources ('rpart', 'RWeka', 'PMML') yielding objects that share
  functionality for print()/plot()/predict() methods. Furthermore, new and improved
  reimplementations of conditional inference trees (ctree()) and model-based
  recursive partitioning (mob()) from the 'party' package are provided based
  on the new infrastructure. A description of this package was published

%package lib
Summary: lib components for the R-partykit package.
Group: Libraries

%description lib
lib components for the R-partykit package.


%prep
%setup -q -c -n partykit

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549031387

%install
export SOURCE_DATE_EPOCH=1549031387
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library partykit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library partykit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library partykit
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library partykit|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/partykit/CITATION
/usr/lib64/R/library/partykit/DESCRIPTION
/usr/lib64/R/library/partykit/INDEX
/usr/lib64/R/library/partykit/Meta/Rd.rds
/usr/lib64/R/library/partykit/Meta/data.rds
/usr/lib64/R/library/partykit/Meta/demo.rds
/usr/lib64/R/library/partykit/Meta/features.rds
/usr/lib64/R/library/partykit/Meta/hsearch.rds
/usr/lib64/R/library/partykit/Meta/links.rds
/usr/lib64/R/library/partykit/Meta/nsInfo.rds
/usr/lib64/R/library/partykit/Meta/package.rds
/usr/lib64/R/library/partykit/Meta/vignette.rds
/usr/lib64/R/library/partykit/NAMESPACE
/usr/lib64/R/library/partykit/NEWS.Rd
/usr/lib64/R/library/partykit/R/partykit
/usr/lib64/R/library/partykit/R/partykit.rdb
/usr/lib64/R/library/partykit/R/partykit.rdx
/usr/lib64/R/library/partykit/data/Rdata.rdb
/usr/lib64/R/library/partykit/data/Rdata.rds
/usr/lib64/R/library/partykit/data/Rdata.rdx
/usr/lib64/R/library/partykit/demo/memory-speed.R
/usr/lib64/R/library/partykit/doc/constparty.R
/usr/lib64/R/library/partykit/doc/constparty.Rnw
/usr/lib64/R/library/partykit/doc/constparty.pdf
/usr/lib64/R/library/partykit/doc/ctree.R
/usr/lib64/R/library/partykit/doc/ctree.Rnw
/usr/lib64/R/library/partykit/doc/ctree.pdf
/usr/lib64/R/library/partykit/doc/index.html
/usr/lib64/R/library/partykit/doc/mob.R
/usr/lib64/R/library/partykit/doc/mob.Rnw
/usr/lib64/R/library/partykit/doc/mob.pdf
/usr/lib64/R/library/partykit/doc/partykit.R
/usr/lib64/R/library/partykit/doc/partykit.Rnw
/usr/lib64/R/library/partykit/doc/partykit.pdf
/usr/lib64/R/library/partykit/help/AnIndex
/usr/lib64/R/library/partykit/help/aliases.rds
/usr/lib64/R/library/partykit/help/partykit.rdb
/usr/lib64/R/library/partykit/help/partykit.rdx
/usr/lib64/R/library/partykit/help/paths.rds
/usr/lib64/R/library/partykit/html/00Index.html
/usr/lib64/R/library/partykit/html/R.css
/usr/lib64/R/library/partykit/libs/symbols.rds
/usr/lib64/R/library/partykit/pmml/airq.pmml
/usr/lib64/R/library/partykit/pmml/bbbc.pmml
/usr/lib64/R/library/partykit/pmml/iris.pmml
/usr/lib64/R/library/partykit/pmml/ttnc.pmml
/usr/lib64/R/library/partykit/pmml/ttnc2.pmml

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/partykit/libs/partykit.so
/usr/lib64/R/library/partykit/libs/partykit.so.avx2
/usr/lib64/R/library/partykit/libs/partykit.so.avx512
