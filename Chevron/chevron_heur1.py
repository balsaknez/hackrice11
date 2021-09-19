from math import cos, asin, sqrt, pi
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyC3KO4bSvKS81aNgRAR4ysQXrHAfJp-Bw4')

class Facility:
    def __init__(self, id, lat, lon, maxOcc):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.maxOcc = maxOcc

    def __repr__(self) -> str:
        return str(self.__dict__)


class Worker:
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties

    def __repr__(self) -> str:
        return str(self.__dict__)


class Equipment:
    def __init__(self, name, prob):
        self.name = name
        self.prob = prob

    def __repr__(self) -> str:
        return str(self.__dict__)


class WorkOrder:
    ID = 0

    def __init__(self, fac_id, eqType, eqId, priority, time):
        self.id = WorkOrder.ID
        WorkOrder.ID += 1
        self.fac_id = fac_id
        self.eqType = eqType
        self.eqId = eqId
        self.priority = priority
        self.time = time
        self.isActive = True

    def __repr__(self) -> str:
        return str(self.__dict__)


facilities = {}
workers = {}
workOrders = {}
equipment = {}


def init():
    f = open("facilities.txt", "r")
    for line in f:
        line = line.strip().lower()
        id = int(line.split("\t")[0])
        lat = float(line.split("\t")[1])
        lon = float(line.split("\t")[2])
        maxOcc = int(line.split("\t")[3])

        fac = Facility(id, lat, lon, maxOcc)

        facilities[id] = fac

    f = open("workers.txt", "r")
    for line in f:
        line = line.strip().lower()
        name = line.split("\t")[0]
        properties = line.split("\t")[1].split(" ")
        worker = Worker(name, properties)
        workers[name] = worker

    f = open("equipment.txt", "r")
    for line in f:
        line = line.strip().lower()
        name = line.split("\t")[0]
        prob = float(line.split("\t")[1])
        equipment[name] = Equipment(name, prob)


def my_print():
    print(facilities)
    print(workers)
    print(equipment)
    print(workOrders)


def add_workorder(fac_id, eqType, eqId, priority, time):
    w = WorkOrder(fac_id, eqType, eqId, priority, time)
    workOrders[w.id] = w
    return w.id


def delete_workorder(id):
    try:
        workOrders.pop(id)
    except Exception:
        print("Key error workOrders")


def distance(lat1, lon1, lat2, lon2):
    p = pi / 180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

def between_lat_long_driving(lat1, lon1, lat2, lon2):
    reverse_geocode_result1 = gmaps.reverse_geocode((lat1, lon1))
    reverse_geocode_result2 = gmaps.reverse_geocode((lat2, lon2))
    matrix = gmaps.distance_matrix_test(reverse_geocode_result1, reverse_geocode_result2)
    print(matrix)


def heur1(id_worker, id_fac):
    sol_key = None
    max_dist = 100000000000

    for key, val in workOrders.items():
        if not val.isActive or val.eqType not in workers[id_worker].properties:
            continue
        if max_dist > distance(facilities[id_fac].lat, facilities[id_fac].lon, facilities[val.fac_id].lat,
                               facilities[val.fac_id].lon):
            max_dist = distance(facilities[id_fac].lat, facilities[id_fac].lon, facilities[val.fac_id].lat,
                                facilities[val.fac_id].lon)
            sol_key = key

    if sol_key == None:
        return None

    #print(max_dist)

    workOrders[sol_key].isActive = False
    return sol_key, workOrders[sol_key].fac_id

def heur2(id_worker, id_fac):
    sol_key = None
    max_dist = 100000000000

    time_weight = 1
    prior_weight = 1.5
    speed = 5


    for key, val in workOrders.items():
        if not val.isActive or val.eqType not in workers[id_worker].properties:
            continue
        travel = distance(facilities[id_fac].lat, facilities[id_fac].lon, facilities[val.fac_id].lat,
                               facilities[val.fac_id].lon) / speed
        total_time = travel + val.time

        if (total_time * time_weight + val.priority * prior_weight < max_dist):
            max_dist = total_time * time_weight + val.priority * prior_weight
            sol_key = key

    if sol_key == None:
        return None

    #print(max_dist)

    workOrders[sol_key].isActive = False
    return sol_key, workOrders[sol_key].fac_id


# returnign None if there is no workorder
def get_next_workorder(id_worker, id_fac):
    return heur2(id_worker, id_fac)


init()

add_workorder(1, "Pump", "P032", 5, 3)
add_workorder(3, "Conveyer", "Con391", 1, 9)
add_workorder(4, "Seperator", "Sep028", 2, 3)
add_workorder(5, "Sensor", "Sen826", 4, 1)
add_workorder(1, "Security", "Sec032", 1, 2)
add_workorder(5, "Electricity", "El087", 3, 2)
add_workorder(1, "Networking", "Net012", 3, 4)
#my_print()
