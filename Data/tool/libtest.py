from Data.tool.vt1000 import ForeGround as text, FormatCode as code
import importlib
import sys
import os


referense = {
    "flask" : ["Flask",],
    "sqlalchemy" : ["SQLAlchemy", "flask-SQLAlchemy"],
    "MySQLdb": ["mysqlclient",]
}


def __test__library(lib: str) -> bool:
    isFounded = importlib.util.find_spec(lib) is not None
    if(isFounded):
        os.popen("pip install {}".format(" ".join(referense[lib])), mode="r").read()
        if (importlib.util.find_spec(lib) is not None):
            print("[{color}Ok{reset}] library '{lib}' was installed".format(
                color=text.green,
                reset=code.reset,
                lib=lib
            ))
            return True
        else:
            print("[{color}Fail{reset}] Library '{lib}' error ".format(
                color=text.red,
                reset=code.reset,
                lib=lib
            ))
            return False
    else:
        print("[{color}Ok{reset}] library '{lib}' alredy isset on system".format(
            color=text.green,
            reset=code.reset,
            lib=lib
        ))
        return True


for library in referense.keys():
    if not __test__library(library):
        sys.exit(1)

