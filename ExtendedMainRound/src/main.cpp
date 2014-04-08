#include <iostream>
#include "Map.h"
#include "Street.h"

float getBest(Street **fbest, std::vector<std::list<Street *> >  const &intersections, int positionStart, int deep = 15) {
	if (deep == 0)
		return 0;
	
	Street *best = NULL;
	float previousScore = -1;
	
	for (auto street : intersections[positionStart]) {
		float tmp = street->getRatio() + getBest(fbest, intersections, street->getIntersectionOpposite(positionStart), deep - 1);
		if (tmp < previousScore || previousScore == -1) {
			best = street;
			previousScore = tmp;
		}
	}


	*fbest = best;
	return previousScore;
}

int main() {
	Map map;
	map.loadMap("paris_54000.txt");

	std::vector<std::list<Street *> > const &intersections = map.getIntersection();
	//ALGO
	for (int i = 0; i < map.getNbCars() ; ++i) {
		int duration = map.getDuration();
		int positionStart = map.getPositionStart();

		map.setCurrentCar(i);

		bool timeIsOver = false;
		while (!timeIsOver)  {
			Street *best = NULL;
			getBest(&best, intersections, positionStart);

			if (duration - best->getPrice() > 0) {
				best->visit();
				duration -= best->getPrice();
				positionStart = best->getIntersectionOpposite(positionStart);
				map.move(positionStart);
			}
			else
				timeIsOver = true;

		}

	}
	system("pause");
	map.writeOutput();

	return 0;
}