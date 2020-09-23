This is a demo project of [@ahmetb](https://www.youtube.com/watch?v=D2mP5vWtVL4&list=PLe1QWkyzVMv7cWTCfY4sdvWKTSm1uUYIQ&index=7&ab_channel=ahmetalpbalkan). I added some comment lines to remember the logic of program if I read the code afterward.


## Install Client (Python) Requirements

Install python dependencies by;

```
pip install -r requirements.txt
```

> I included all generated files to project but you can generate by yourself to learn process.

## Generate Client (Python) Implementation From Proto

Run the command below in client directory. It will generate 2 files (timeservice_pb2_grpc.py and timeservice_pb2.py)

```
python3 -m grpc.tools.protoc -I../ ../timeservice.proto --python_out=. --grpc_python_out=.
```


## Generate Server (Go) Implementation From Proto

Run the command below on project directory. It will generate a file named "timeservice.pb.go" under server/pb.

```
protoc -I . timeservice.proto --go_out=plugins=grpc:server/pb
```

## Run Server

```
go run .
```

## Run Client

```
python3 main.py
```
