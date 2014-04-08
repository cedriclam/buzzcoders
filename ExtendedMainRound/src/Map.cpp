#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

#include "Map.h"

Map::~Map() {
	int score = 0;
	for (auto street : _streets) {
		if (street->isVisited())
			score += street->getDistance();
		delete street;
	}
	std::cout << "Distance : " << score << std::endl;
}

void Map::loadMap(std::string const &filename) {
	std::ifstream infile(filename);

	std::string line;
	std::getline(infile, line);
	std::istringstream iss(line);
	int nbIntersects, nbStreets;
	iss >> nbIntersects >> nbStreets >> _duration >> _nbCars >> _positionStart;
	_intersections.resize(nbIntersects);
	_streets.resize(nbStreets);
	_moves.resize(_nbCars);

	//Read coordinates intersections
	for (int i = 0; i < nbIntersects; ++i)
		std::getline(infile, line); //position not use


	//Read streets
	for (int i = 0; i < nbStreets; ++i) {
		std::getline(infile, line);
		std::istringstream iss(line);
		int intersect1, intersect2, way, price, length;
		iss >> intersect1 >> intersect2 >> way >> price >> length;

		Street *street = new Street(intersect2);
		street->setDistance(length);
		street->setPrice(price);
		street->setIntersection1(intersect1);
		street->setIntersection2(intersect2);
		_streets[i] = street;

		//creation of intersections
		_intersections[intersect1].push_back(street);
		if (way == 2)
			_intersections[intersect2].push_back(street);
	}
}

std::vector<std::list<Street *> >  const &Map::getIntersection() const {
	return _intersections;
}

int Map::getDuration() const {
	return _duration;
}

int Map::getPositionStart() const {
	return _positionStart;
}

int Map::getNbCars() const {
	return _nbCars;
}

void Map::setCurrentCar(int currentCar) {
	_currentCar = currentCar;
}

void Map::move(int pos) {
	_moves[_currentCar].push_back(pos);
}

void Map::writeOutput() const {
	std::ofstream myfile;
	myfile.open("example.txt");

	myfile << _nbCars << std::endl;
	for (auto &cars : _moves) {
		myfile << cars.size() + 1 << std::endl;
		myfile << _positionStart << std::endl;
		for (auto move : cars)
			myfile << move << std::endl;
	}
	myfile.close();
}