from functools import wraps
import argparse


class Argumnets:

    @staticmethod
    def Host(functions):
        parser = argparse.ArgumentParser(description="start dinnerplan-server with flask")
        parser.add_argument("-i", '--ip', action="store", dest="host", default="0.0.0.0", help="server ip or host address")
        parser.add_argument("-p", "--port", action="store", dest="port", type=int, default=5000, help="server port")
        argumnets = parser.parse_args()
        @wraps(functions)
        def decorated(*args, **kwargs):
            if not vars(argumnets) and __name__ != "__main__" and False:
                return Argumnets.__error__message(*args, **kwargs)
            else:
                return functions(debug=True, host=argumnets.host, port=argumnets.port)
        return decorated

    def __error__message(self):
        print("[!] Server arguments crush")