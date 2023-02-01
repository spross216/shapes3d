import shapes3D
import csv

class Solver:
    def __init__(self, filename):
        self.shapes = [] #buffer
        self.total = 0 #running total
        with open(filename, 'r') as data:
            reader = csv.reader(data)
            for row in reader: # takes the first item in each line of the csv file, and runs the conditioinals to dertermine which class function to pass the values to
                if row[0] == "cube":
                    shape = shapes3D.Cube(float(row[1]))
                elif row[0] == "cuboid":
                    shape = shapes3D.Cuboid(float(row[1]), float(row[2]), float(row[3]))
                elif row[0] == "cylinder":
                    shape = shapes3D.Cylinder(float(row[1]), float(row[2]))
                elif row[0] == "sphere":
                    shape = shapes3D.Sphere(float(row[1]))
                elif row[0] == "prism":
                    shape = shapes3D.Prism(float(row[1]), float(row[2]), float(row[3]))
                elif row[0] == "area":
                    self.total += sum(calc.area() for calc in self.shapes) * float(row[1])
                    self.shapes = []
                elif row[0] == "volume":
                    self.total += sum(calc.volume() for calc in self.shapes) * float(row[1])
                    self.shapes = []
                else:
                    raise ValueError("Invalid shape name: {}".format(row[0]))
                self.shapes.append(shape)


if __name__ == "__main__": # will only execute the code in this block if it is exectued as a script
    solver = Solver("shapes.csv")
    print("The sum of measurements is " + str(solver.total))