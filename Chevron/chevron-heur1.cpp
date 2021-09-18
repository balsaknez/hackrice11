#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

struct Facility{
	int id;
	double lat, lon;
	int maxOcc;
};

struct Worker{
	string name;
	vector<string> cert;
	double lat, lon;
};

struct Equipment{
	string name;
	double p;
};

map<int, Facility> facilities;

void init()
{
	freopen("facilities.txt","r",stdin);
	while(scanf("%d %lf %lf %d", &id, &lat, &lon, &maxop))
	{
		facilities[id] = {id, lat, lon, maxop};
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
		while ((pos = s.find(delimiter)) != std::string::npos) {
		    token = s.substr(0, pos);
		    std::cout << token << std::endl;
		    s.erase(0, pos + delimiter.length());
		}
		cout << s << std::endl;
	}
}

void add_workorder()
{

}

int main()
{
	init();


	while(1)
	{
		int type;
		scanf("%d",&type);
		switch(type)
		{
			case 0 : add_workorder();break;
			case 1 : add_workorder();break;
			case 2 : add_workorder();break;
		}
	}
}