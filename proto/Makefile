build-go:
	protoc -I . calculations.proto --go_out=plugins=grpc:./go

build-python:
	python3 -m grpc_tools.protoc -I . calculations.proto --python_out=./python --grpc_python_out=./python