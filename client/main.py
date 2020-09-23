import grpc


import timeservice_pb2
import timeservice_pb2_grpc


def now(stub):
    resp = stub.Now(timeservice_pb2.NowRequest())
    print(resp.time.value)


# streamTime tests server stream service.
def streamTime(stub, length):
    for msg in stub.Stream(timeservice_pb2.TimeStreamRequest(length=length)):
        print('msg={}'.format(msg.time.value))


def run():
    with grpc.insecure_channel('localhost:8080') as conn:
        stub = timeservice_pb2_grpc.TimeServiceStub(conn)
        now(stub)
        # streamTime(stub, 10)


if __name__ == '__main__':
    run()
