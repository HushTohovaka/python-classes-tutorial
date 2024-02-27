class Robot:

    # Creatuing a custom constructor inside the class
    def __init__(self, name, color, weight):
         self.name = name
         self.color = color
         self.weight = weight

    # Need to add self to every method given to this class 
    def introduceSelf(self):
        print("Hello " + self.name)

    def favoriteColor(self):
        print("Favorite Color " + self.color)

    def currentWeight(self):
        print("Your weight is " + self.weight)

    def goalWeight(self):
        goalWeight = float(self.weight) * .90 
        print("Your goal weight is " + str(goalWeight))
    
    def rename(self, newName):
        self.name = newName

    def reColor(self,newColor):
        self.color = newColor
    


# This is a simple way to do it that is not efficient
# r1 = Robot()
# r1.name = "Hush"
# r1.color = "red"
# r1.weight = 30

# r2 = Robot()
# r2.name = "Lily"
# r2.color = "Yellow"
# r2.weight = 10

# r1.introduceSelf()
# r2.introduceSelf()

r1 = Robot("Hush", "red", "30")
r2 = Robot("Lily", "Purple", "20")


r2.introduceSelf()
r2.rename("hushypooh")
r2.introduceSelf()

r2.favoriteColor()
r2.reColor("pink")
r2.favoriteColor()


r2.currentWeight()

r2.goalWeight()