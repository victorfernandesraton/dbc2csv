# Makefile for dbc2csv python wheel

# PKG_NAME and VERSION should match what is in setup.py
PKG_NAME=dbc2csv
VERSION=0.1.0

# help
help:
    @echo "Usage: make <all|setup|build|install|uninstall|clean>"

# install packaging utilities (only run this once)
setup: 
	pip install wheel setuptools

# build the wheel
build: ${WHEEL_TARGET}
	git clone https://github.com/eaglebh/blast-dbf.git ./bin/blast-dbf
	cd ./bin/blast-dbf && make

# install to local python environment
install: ${WHEEL_TARGET}
	python setup.py install
	pip install -r requirements.txt

# uninstall from local python environment
uninstall:
	pip uninstall ${PKG_NAME}

# remove all build artifacts
clean:
	@rm -rf bin
	@rm -rf build dist ${PKG_NAME}.egg-info


# build the wheel
${WHEEL_TARGET}: setup.py ${PKG_NAME}/__init__.py ${PKG_NAME}/module1.py ${PKG_NAME}/module2.py ${PKG_NAME}/bin/binary_tool1 ${PKG_NAME}/bin/binary_tool2
	python setup.py bdist_wheel --universal

# execute all commands (setup, build, and install)
all: setup build install