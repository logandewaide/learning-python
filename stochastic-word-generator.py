import re
import random

class StochasticWordGenerator:
    def __init__(self) :
        self.word_chain = dict()

    # takes list of words and assigns to word_chain
    def fit(self, text) :
        text = self._clean(text)

        for i in range(0, len(text) - 1):
            current_word = text[i]
            next_word = text[i+1]

            if current_word not in self.word_chain.keys():
                self.word_chain[current_word] = [next_word]
            
            else:
                self.word_chain[current_word].append(next_word)

    # cleans initial text and return list of words
    def _clean(self, text) :
        text = text.lower()
        
        text = re.findall(r"[\w'-]+|[.?!,;]", text)

        return text

    # returns prediction of words at specified length and starting word
    def predict(self, seed, length) :
        result = [seed]

        for i in range(length): 
            current_word = result[i]

            if current_word in self.word_chain:
                choices = self.word_chain[current_word]
                
                next_word = random.choice(choices)

                result.append(next_word)
            else:
                break

        return " ".join(result)

if __name__ == "__main__":
    sampleText1 = "In order to bake a proper loaf of bread, patience is just as important as precision. The dough must be kneaded thoroughly, then left to rise in a warm, undisturbed environment. Rushing the process can result in a dense texture, while careful timing produces a light and airy crumb. Baking, in many ways, is a quiet exercise in discipline."
    sampleText2 = "The early morning light filtered through the blinds, casting long stripes across the wooden floor. Somewhere outside, a dog barked, followed by the distant rumble of a passing bus. She sat at the kitchen table, coffee growing cold in her hands, replaying the conversation from the night before. It wasn’t what had been said that bothered her, but what had been left unsaid."
    sampleText3 = "Broccoli is a nutrient-dense vegetable belonging to the cruciferous family, known for its numerous health benefits. It is rich in vitamins C and K, fiber, and various antioxidants, making it a valuable addition to a balanced diet. Regular consumption of broccoli has been linked to improved digestion, enhanced immune function, and potential cancer-fighting properties. In addition to its health benefits, broccoli is versatile in culinary applications. It can be enjoyed raw in salads, steamed as a side dish, or incorporated into stir-fries and casseroles. Its mild flavor allows it to pair well with a variety of ingredients, making it a popular choice among home cooks and professional chefs alike. Furthermore, broccoli is easy to grow, making it accessible for home gardening enthusiasts. It thrives in cooler climates and can be harvested multiple times throughout its growing season. This combination of health benefits, culinary versatility, and ease of cultivation contributes to broccoli's status as a staple vegetable in many households."
    model = StochasticWordGenerator()
    model.fit(sampleText3)
    model.fit(sampleText2)
    model.fit(sampleText1)
    
    print(model.predict(random.choice(list(model.word_chain.keys())), 100))