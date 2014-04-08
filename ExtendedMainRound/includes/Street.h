#ifndef STREET_HPP_
#define STREET_HPP_

#include <list>

class Street {
public:
	Street(int);

	int getId() const;
	
	void visit();
	bool isVisited() const;

	void setDistance(int);
	int getDistance() const;

	void setPrice(int);
	int getPrice() const;

	void addNeighbour(Street *);
	std::list<Street *> const &getNeighbours() const;

	void setIntersection1(int);
	void setIntersection2(int);
	int getIntersectionOpposite(int) const;

	float getRatio();

private:
	int _id;
	bool _visited;
	std::list<Street *> _neighbours;
	int _distance;
	int _price;

	int _intersection1;
	int _intersection2;

	float conf;
};

#endif