#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <sstream>

using namespace std;

struct Facility{
	int id;
	double lat, lon;
	int maxOcc;
};

struct Worker{
	vector<string> worker_properties;

	Worker(vector<string> &w){
		worker_properties = w;
	}

	double lat, lon;
};

struct Equipment{
	string name;
	double p;
};


struct WorkOrder{
	static int ID;
	int id = ID++;
	int fac_id;
	string eqType;
	int eqId;
	int priority;
	int time;
};

int WorkOrder :: ID = 0;


map<int, Facility> facilities;
vector<Worker> workers;
map<int, WorkOrder> workOrders;

void init()
{
	freopen("facilities.txt","r",stdin);
	int id, maxOcc;
	double lat, lon;

	while(scanf("%d %lf %lf %d", &id, &lat, &lon, &maxOcc) != EOF)
	{
		facilities[id] = {id, lat, lon, maxOcc};
	}
	
	freopen("workers.txt", "r", stdin);
	string s;
	while (getline(cin, s)) 
	{
		string name = "";
		int i;
		size_t pos = 0;
		string token;
		string delimiter = " ";

		vector<string> worker_properties;

		while ((pos = s.find(delimiter)) != std::string::npos) {
		    token = s.substr(0, pos);
		    worker_properties.push_back(token);
		    s.erase(0, pos + delimiter.length());
		}

		worker_properties.push_back(s);

		workers.push_back(Worker(worker_properties));
	}

	freopen(stdin, "r", stdin);
}



void print()
{

	cout << "----------------FACILITIES--------------" << endl;
	for (map<int, Facility>::iterator it = facilities.begin(); it != facilities.end(); it++)
	{
	    cout << it->second.id << " " << it -> second.lat << " " << it->second.lon << " " << it->second.maxOcc<<endl;
	}
	cout << "----------------------------------------" << endl;
	cout << "----------------WORKERS-----------------" << endl;
	for (auto w : workers)
	{
		for (auto s : w.worker_properties)
		{
			cout << s << " ";
		}

		cout << endl;
	}

	cout << "----------------------------------------" << endl;

	cout << "----------------WORK_ORDERS--------------" << endl;
	for (map<int, WorkOrder>::iterator it = workOrders.begin(); it != workOrders.end(); it++)
	{
	    cout << it->second.id << " " << it -> second.fac_id << " " << it->second.eqType << " " << it->second.eqId<< " " << it->second.priority << " "<<it->second.time<<endl;
	}
	cout << "----------------------------------------" << endl;
}

void add_workorder(int fac_id, string eqType, int eqId, int priority, int time)
{
	WorkOrder wo;
	wo.fac_id = fac_id;
	wo.eqType = eqType;
	wo.eqId = eqId;
	wo.priority = priority;
	wo.time = time;

	workOrders[wo.id] = wo;
}

void add_workorder_wrapper()
{
	int fac_id, eqId, priority, time;
	string eqType;
	cin >> fac_id; cout << fac_id << endl;
	cin >> eqType; cout << eqType << endl;
	cin >> eqId; cout << eqId << endl;
	cin >> priority; cout << priority << endl;
	cin >> time; cout << time << endl;

	add_workorder(fac_id, eqType, eqId, priority, time);
}



int main()
{
	init();
	print();


	while(1)
	{
		int type;
		scanf("\n%d",&type);
		switch(type)
		{
			case 0 : add_workorder_wrapper();break;
			case 1 : add_workorder_wrapper();break;
			case 2 : add_workorder_wrapper();break;
			case 3 : print();break;
		}
	}
}