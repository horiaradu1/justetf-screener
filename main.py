from utils import make_request, write_csv
from typing import List, Dict

if __name__ == "__main__":
    
    out = List[Dict[str, str]]
    out = make_request()

    # print(out[0])
    print(len(out))

    write_csv(out, "test.csv")

    
