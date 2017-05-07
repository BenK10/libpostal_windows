./bootstrap.sh
mkdir -p /c/libpostal//libpostal_data
./configure --datadir=/c/libpostal//libpostal_data
make
make install
