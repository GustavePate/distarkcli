PYTHON=`which python`
PROTOC=`which protoc`
NAME=`python setup.py --name`
PROTOPATH=./ressources/protos/

#PYTHON PATH MODIFICATION SHALL BE COPIED TO TRAVIS.YML !!! 
CLIENTSRCPATH=${PWD}/distarkcli/
PYTHONPATH := ${PYTHONPATH}:${$CLIENTSRCPATH}

PROTOC_PY_PATH=${PWD}/distarkcli/protos/
PYTHONPATH := ${PYTHONPATH}:$(PROTOC_PY_PATH)


##############################
#  my targets
##############################

clean:
	find .  -type f -name "*.pyc" -exec rm {} \;

buildclient:
	$(PYTHON) setup.py install

indent:
	$(PYTHON) -m reindent --nobackup *.py

protoc:
	$(PROTOC) --python_out=./distarkcli/protos/ --proto_path=$(PROTOPATH) ./ressources/protos/objects/*
	$(PROTOC) --python_out=./distarkcli/protos/ --proto_path=$(PROTOPATH) ./ressources/protos/services/*
	$(PROTOC) --python_out=./distarkcli/protos/ --proto_path=$(PROTOPATH) ./ressources/protos/generic_service.proto

main: clean mainlaunch

mainlaunch:
	echo $(PYTHONPATH)
	$(PYTHON) -m main $(PWD)/ressources/conf/configuration.yaml


test:
	py.test --maxfail=1 --showlocals  --duration=3 -v --clearcache  -s --confpath=${PWD}/ressources/conf/configuration.yaml 

test.travis:
	py.test --maxfail=1 --showlocals  --duration=3 -v --clearcache  -s --confpath=${PWD}/ressources/conf/configuration.MOCK.yaml 


