from xmlrpc.server import SimpleXMLRPCServer

with SimpleXMLRPCServer(('127.0.0.1', 8000)) as server:

    def add_num(x, y):
        return x + y

    # 第1引数に登録する関数,第2引数にクライアントが呼ぶときの名前
    server.register_function(add_num, "add_num")
    server.serve_forever()
