#include <iostream>
#include "Street.h"

Street::Street(int id)
: _id(id), _visited(false)
{
	conf = 1;
}

int Street::getId() const {
	return _id;
}

void Street::visit() {
	_visited = true;
	conf += 100;
}

bool Street::isVisited() const {
	return _visited;
}

void Street::setDistance(int distance) {
	_distance = distance;
}

int Street::getDistance() const {
	return _distance;
}

void Street::setPrice(int price) {
	_price = price;
}

int Street::getPrice() const {
	return _price;
}

void Street::addNeighbour(Street *street) {
	_neighbours.push_back(street);
}

std::list<Street *> const &Street::getNeighbours() const {
	return _neighbours;
}

void Street::setIntersection1(int intersec) {
	_intersection1 = intersec;
}

void Street::setIntersection2(int intersec) {
	_intersection2 = intersec;
}

int Street::getIntersectionOpposite(int intersec) const {
	if (_intersection1 == intersec)
		return _intersection2;
	return _intersection1;
}

float Street::getRatio() {
	return (float)(((float)_distance) / ((float)_price)) * conf;
}