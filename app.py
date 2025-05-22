class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name

    def getLegs(self):
        return self._legs

    def speak(self):
        print(self.name + ' says bark!')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.getLegs())

class WordSet:
    def __init__(self):
        self.words = set()

    def addText(self, text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)

    def cleanText(self, text):
        text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '')
        return text.lower()

wordSet = WordSet()

wordSet.addText('Hi, I\'m Jake! Here is a sentence I want to add')
wordSet.addText('Here is another sentece I want to add.')

print(wordSet.words)

class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: Yap yap yap!')

    def wagTail(self):
        print('Vigorous wagging!')

chihuahuaDog = Chihuahua('Roxy')
chihuahuaDog.speak()
chihuahuaDog.wagTail()

class UniqueList(list):
    def append(self, item):
        if item in self:
            return
        super().append(item)

uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(2)
uniqueList.append(2)

print(uniqueList)