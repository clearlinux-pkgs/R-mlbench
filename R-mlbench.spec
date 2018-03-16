#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mlbench
Version  : 2.1.1
Release  : 1
URL      : https://cran.r-project.org/src/contrib/mlbench_2.1-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mlbench_2.1-1.tar.gz
Summary  : Machine Learning Benchmark Problems
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mlbench-lib
BuildRequires : clr-R-helpers

%description
benchmark problems, including, e.g., several data sets from the
        UCI repository.

%package lib
Summary: lib components for the R-mlbench package.
Group: Libraries

%description lib
lib components for the R-mlbench package.


%prep
%setup -q -c -n mlbench

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521209819

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521209819
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mlbench
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mlbench
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mlbench
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library mlbench|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mlbench/CITATION
/usr/lib64/R/library/mlbench/DESCRIPTION
/usr/lib64/R/library/mlbench/INDEX
/usr/lib64/R/library/mlbench/Meta/Rd.rds
/usr/lib64/R/library/mlbench/Meta/data.rds
/usr/lib64/R/library/mlbench/Meta/features.rds
/usr/lib64/R/library/mlbench/Meta/hsearch.rds
/usr/lib64/R/library/mlbench/Meta/links.rds
/usr/lib64/R/library/mlbench/Meta/nsInfo.rds
/usr/lib64/R/library/mlbench/Meta/package.rds
/usr/lib64/R/library/mlbench/NAMESPACE
/usr/lib64/R/library/mlbench/NEWS
/usr/lib64/R/library/mlbench/R/mlbench
/usr/lib64/R/library/mlbench/R/mlbench.rdb
/usr/lib64/R/library/mlbench/R/mlbench.rdx
/usr/lib64/R/library/mlbench/data/BostonHousing.rda
/usr/lib64/R/library/mlbench/data/BostonHousing2.rda
/usr/lib64/R/library/mlbench/data/BreastCancer.rda
/usr/lib64/R/library/mlbench/data/DNA.rda
/usr/lib64/R/library/mlbench/data/Glass.rda
/usr/lib64/R/library/mlbench/data/HouseVotes84.rda
/usr/lib64/R/library/mlbench/data/Ionosphere.rda
/usr/lib64/R/library/mlbench/data/LetterRecognition.rda
/usr/lib64/R/library/mlbench/data/Ozone.rda
/usr/lib64/R/library/mlbench/data/PimaIndiansDiabetes.rda
/usr/lib64/R/library/mlbench/data/PimaIndiansDiabetes2.rda
/usr/lib64/R/library/mlbench/data/Satellite.rda
/usr/lib64/R/library/mlbench/data/Servo.rda
/usr/lib64/R/library/mlbench/data/Shuttle.rda
/usr/lib64/R/library/mlbench/data/Sonar.rda
/usr/lib64/R/library/mlbench/data/Soybean.rda
/usr/lib64/R/library/mlbench/data/Vehicle.rda
/usr/lib64/R/library/mlbench/data/Vowel.rda
/usr/lib64/R/library/mlbench/data/Zoo.rda
/usr/lib64/R/library/mlbench/help/AnIndex
/usr/lib64/R/library/mlbench/help/aliases.rds
/usr/lib64/R/library/mlbench/help/mlbench.rdb
/usr/lib64/R/library/mlbench/help/mlbench.rdx
/usr/lib64/R/library/mlbench/help/paths.rds
/usr/lib64/R/library/mlbench/html/00Index.html
/usr/lib64/R/library/mlbench/html/R.css
/usr/lib64/R/library/mlbench/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mlbench/libs/mlbench.so
/usr/lib64/R/library/mlbench/libs/mlbench.so.avx2
/usr/lib64/R/library/mlbench/libs/mlbench.so.avx512
