import time

def optionToString(option):
    optionList = {
        "10": "Start",
        "11": "Click to start",
        "20": "Suspend",
        "21": "Click to spspend",
        "30": "Resume",
        "31": "Click to resume",
        "40": "Stop",
        "41": "Click to stop",
        "51": "Wait until Sensor input high",
        "52": "Wait until Source 2 is On",
        "52": "Wait until click button",
        "61": "Open Source ",
        "62": "Close Source "
    }
    if(option["type"] == "50"):
        return "Wait " + option["data"][0] + " seconds"
    else:
        return optionList[option["type"]] + option["data"][0]
    


class SimpiQ:
    queue = []
    idx = 0

    def __init__(self, data) -> None:
        self.queue = data

    def size(self) -> int:
        return len(self.queue)

    def hasNext(self) -> bool:
        return self.size() > self.idx

    def next(self):
        self.idx += 1
        return self.queue[self.idx - 1]

    def current(self) -> int:
        return self.idx + 1

    def waitUntil(self, signals, idx):
        signals[idx] = True
        while(signals[idx]):
            print(f"Simpi is waiting signal")
            time.sleep(1)

    def sleep(self, sec:int):
        time.sleep(sec)
    

def simpiProcess(data, signals):
    
    simpi = SimpiQ(data)

    while(simpi.hasNext()):
        print(f"{simpi.current()}: {optionToString(simpi.next())}")

    print("Simpi finished")

    # option.waitUntil(signals, 0)

    # for i in range(data):
    #     print(f"Simpi is running: {i}, Signals: {signals[0]}")
    #     option.sleep(1)


