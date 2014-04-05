import parser

if __name__ == '__main__':
	G, nbCars, Totaltime, intersections, streets = parser.parseFile("paris_54000.txt")
	
	print "totaltime : ", str(Totaltime)
	print "nbCars : ", str(nbCars)
	print "streets nb : ", str(len(streets))
	print "intersections nb : ", str(len(intersections))
        