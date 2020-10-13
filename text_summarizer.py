import re

text = "That vote came after House Democrats moved in May to pass a sweeping bill to spend roughly $3 trillion on relief measures, a proposal that similarly generated opposition from Republicans, who dismissed the aid package as a liberal wish list. This story has been updated with additional developments Tuesday."

def sanitize_input(input):
    sentences = input.split('. ')
    tokenized_sentences = []
    
    for sentence in sentences:
        tokens = sentence.split(' ')
        tokenized_sentences.append(tokens)
    
    return tokenized_sentences

class Text_Summarizer:
    def __init__(self, text):
        self.word_counts = {}
        self.total_words = 0
        self.sentences = []
    
        # Tokenize Sentences
        sentences = text.split('. ')
        
        for sentence in sentences:
            self.sentences.append(sentence)

        for sentence in self.sentences:
            tokens = sentence.split(' ')
            for token in tokens:
                self.total_words += 1
                if token in self.word_counts:
                    self.word_counts[token] += 1
                else:
                    self.word_counts[token] = 1


tokenized_sentences = sanitize_input(text)

text_sum = Text_Summarizer(text)
print(text_sum.word_counts)
print(text_sum.total_words)