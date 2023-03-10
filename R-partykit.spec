#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-partykit
Version  : 1.2.18
Release  : 62
URL      : https://cran.r-project.org/src/contrib/partykit_1.2-18.tar.gz
Source0  : https://cran.r-project.org/src/contrib/partykit_1.2-18.tar.gz
Summary  : A Toolkit for Recursive Partytioning
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-partykit-lib = %{version}-%{release}
Requires: R-Formula
Requires: R-inum
Requires: R-libcoin
Requires: R-mvtnorm
BuildRequires : R-AER
BuildRequires : R-Formula
BuildRequires : R-XML
BuildRequires : R-inum
BuildRequires : R-libcoin
BuildRequires : R-mlbench
BuildRequires : R-mvtnorm
BuildRequires : R-party
BuildRequires : R-pmml
BuildRequires : R-strucchange
BuildRequires : R-vcd
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n partykit
cd %{_builddir}/partykit

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678471564

%install
export SOURCE_DATE_EPOCH=1678471564
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/partykit/ULGcourse-2020/Data/Axams_pred.rda
/usr/lib64/R/library/partykit/ULGcourse-2020/Data/Axams_testdata.rda
/usr/lib64/R/library/partykit/ULGcourse-2020/Data/GENS_00_innsbruck-flughafen.txt
/usr/lib64/R/library/partykit/ULGcourse-2020/Data/GENS_00_innsbruck_20200410.dat
/usr/lib64/R/library/partykit/ULGcourse-2020/Data/GENS_00_innsbruck_20200411.dat
/usr/lib64/R/library/partykit/ULGcourse-2020/Data/GENS_00_innsbruck_20200412.dat
/usr/lib64/R/library/partykit/ULGcourse-2020/Data/GENS_00_innsbruck_20200413.dat
/usr/lib64/R/library/partykit/ULGcourse-2020/Data/GENS_00_innsbruck_20200414.dat
/usr/lib64/R/library/partykit/ULGcourse-2020/Data/GENS_00_innsbruck_20200415.dat
/usr/lib64/R/library/partykit/ULGcourse-2020/Data/GENS_00_innsbruck_20200416.dat
/usr/lib64/R/library/partykit/ULGcourse-2020/Data/STAGEobs_tawes_11121_defense.rda
/usr/lib64/R/library/partykit/ULGcourse-2020/Data/crps_24to4_all.rda
/usr/lib64/R/library/partykit/ULGcourse-2020/Makefile
/usr/lib64/R/library/partykit/ULGcourse-2020/airport_20200412.jpg
/usr/lib64/R/library/partykit/ULGcourse-2020/airport_20200413.jpg
/usr/lib64/R/library/partykit/ULGcourse-2020/circtree_ibk.pdf
/usr/lib64/R/library/partykit/ULGcourse-2020/code_tree.R
/usr/lib64/R/library/partykit/ULGcourse-2020/density_1.pdf
/usr/lib64/R/library/partykit/ULGcourse-2020/density_1_hist.pdf
/usr/lib64/R/library/partykit/ULGcourse-2020/density_2.pdf
/usr/lib64/R/library/partykit/ULGcourse-2020/density_2_hist.pdf
/usr/lib64/R/library/partykit/ULGcourse-2020/density_all.pdf
/usr/lib64/R/library/partykit/ULGcourse-2020/density_all_hist.pdf
/usr/lib64/R/library/partykit/ULGcourse-2020/exercises/data/CPS1985.rds
/usr/lib64/R/library/partykit/ULGcourse-2020/exercises/data/german.rds
/usr/lib64/R/library/partykit/ULGcourse-2020/exercises/data/titanic.rds
/usr/lib64/R/library/partykit/ULGcourse-2020/exercises/exercise_forest_german_credit.Rmd
/usr/lib64/R/library/partykit/ULGcourse-2020/exercises/exercise_forest_wage.Rmd
/usr/lib64/R/library/partykit/ULGcourse-2020/exercises/exercise_german_credit.Rmd
/usr/lib64/R/library/partykit/ULGcourse-2020/exercises/exercise_titanic.Rmd
/usr/lib64/R/library/partykit/ULGcourse-2020/forest.jpg
/usr/lib64/R/library/partykit/ULGcourse-2020/slides_forest.Rnw
/usr/lib64/R/library/partykit/ULGcourse-2020/slides_tree.Rnw
/usr/lib64/R/library/partykit/data/Rdata.rdb
/usr/lib64/R/library/partykit/data/Rdata.rds
/usr/lib64/R/library/partykit/data/Rdata.rdx
/usr/lib64/R/library/partykit/demo/memory-speed.R
/usr/lib64/R/library/partykit/doc/constparty.R
/usr/lib64/R/library/partykit/doc/constparty.R.R
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
/usr/lib64/R/library/partykit/pmml/airq.pmml
/usr/lib64/R/library/partykit/pmml/bbbc.pmml
/usr/lib64/R/library/partykit/pmml/iris.pmml
/usr/lib64/R/library/partykit/pmml/ttnc.pmml
/usr/lib64/R/library/partykit/pmml/ttnc2.pmml
/usr/lib64/R/library/partykit/tests/Examples/partykit-Ex.Rout.save
/usr/lib64/R/library/partykit/tests/Rplots.pdf
/usr/lib64/R/library/partykit/tests/bugfixes.R
/usr/lib64/R/library/partykit/tests/bugfixes.Rout.save
/usr/lib64/R/library/partykit/tests/constparty.R
/usr/lib64/R/library/partykit/tests/constparty.Rout.save
/usr/lib64/R/library/partykit/tests/regtest-MIA.R
/usr/lib64/R/library/partykit/tests/regtest-MIA.Rout.save
/usr/lib64/R/library/partykit/tests/regtest-cforest.R
/usr/lib64/R/library/partykit/tests/regtest-cforest.Rout.save
/usr/lib64/R/library/partykit/tests/regtest-ctree.R
/usr/lib64/R/library/partykit/tests/regtest-ctree.Rout.save
/usr/lib64/R/library/partykit/tests/regtest-glmtree.R
/usr/lib64/R/library/partykit/tests/regtest-glmtree.Rout.save
/usr/lib64/R/library/partykit/tests/regtest-honesty.R
/usr/lib64/R/library/partykit/tests/regtest-lmtree.R
/usr/lib64/R/library/partykit/tests/regtest-nmax.R
/usr/lib64/R/library/partykit/tests/regtest-nmax.Rout.save
/usr/lib64/R/library/partykit/tests/regtest-node.R
/usr/lib64/R/library/partykit/tests/regtest-node.Rout.save
/usr/lib64/R/library/partykit/tests/regtest-party-random.R
/usr/lib64/R/library/partykit/tests/regtest-party.R
/usr/lib64/R/library/partykit/tests/regtest-party.Rout.save
/usr/lib64/R/library/partykit/tests/regtest-split.R
/usr/lib64/R/library/partykit/tests/regtest-split.Rout.save
/usr/lib64/R/library/partykit/tests/regtest-weights.R
/usr/lib64/R/library/partykit/tests/regtest-weights.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/partykit/libs/partykit.so
/usr/lib64/R/library/partykit/libs/partykit.so.avx2
/usr/lib64/R/library/partykit/libs/partykit.so.avx512
