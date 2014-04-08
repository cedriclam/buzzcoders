#ifndef MAP_HPP_
#define MAP_HPP_

#include <vector>
#include <list>

#include "Street.h"

class Map {
	public:
		~Map();
		void loadMap(std::string const &);

		std::vector<std::list<Street *> >  const &getIntersection() const;
		int getDuration() const;
		int getPositionStart() const;
		int getNbCars() const;

		void setCurrentCar(int);
		void move(int);

		void writeOutput() const;
	private:
		std::vector<std::list<Street *> > _intersections;
		std::vector<Street *> _streets;
		std::vector<std::list<int > > _moves;

		int _duration;
		int _positionStart;
		int _nbCars;
		int _currentCar;
};

#endif