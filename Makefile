PYTHON=`which python`
PROTOC=`which protoc`
NAME=`python setup.py --name`
PROTOPATH=./ressources/protos/

#PYTHON PATH MODIFICATION SHALL BE COPIED TO TRAVIS.YML !!! 
CLIENTPATH=${PWD}/distarkcli/
PROTOC_PY_PATH=${PWD}/distarkcli/protos/
PYTHONPATH := ${PYTHONPATH}:$(PROTOC_PY_PATH)
PYTHONPATH := ${PYTHONPATH}:${$CLIENTPATH}


##############################
#  my targets
##############################

buildclient:
	$(PYTHON) $(CLIENTPATH)/setup.py install

indent:
	$(PYTHON) -m reindent --nobackup *.py

protoc:
	$(PROTOC) --python_out=./distarkcli/protos/ --proto_path=$(PROTOPATH) ./ressources/protos/objects/*
	$(PROTOC) --python_out=./distarkcli/protos/ --proto_path=$(PROTOPATH) ./ressources/protos/services/*
	$(PROTOC) --python_out=./distarkcli/protos/ --proto_path=$(PROTOPATH) ./ressources/protos/generic_service.proto

main:
	echo $(PYTHONPATH)
	$(PYTHON) -m main2 $(CLIENTPATH)/ressources/conf/configuration.yaml


test:
	py.test --maxfail=1 --showlocals  --duration=3 -v --clearcache  -s 
