## The Catalog Empire

Small repo where im thinking about how LLMs like llama2 are seeing course objects in course catalogs.

`courses.txt` contains the course objects annotated in the REA project (as of 2024-04-11; see Label-Studio for the people who know what im talking about). Each line is a course object. You don't know where they come from. You only have (noisy) texts of course catalogs.

`full_page.txt` is an exemplar of a page full of course catalogs.

The goals are the following:

1. Given a list of course objects, are there statistical regularities that would lead FMs to have a different representations of words in the course objects than same words used in non-course catalog contexts?
1. Given what we know from llama2's transformer architecture, is there a way it could easily learn to delineate course objects from one another?
1. `Noise`: How does noise might impact LLMs abilities to parse unstructured text into JSON format?
    - If we clean the training data, does the LLMs will be able to predict out-of-sample noisy data?
    - Are we better to put our effort upstream, trying to reduce noise by having better OCR? What what point does better OCR is just having an a llmOCR?
1. Amongst course objects, there are section headers indicating what is the department? Can LLMs extract department headers?
1. Is text enough to answer the previous questions? What would we gain by somehow introducing the layout that is present in the PDF, e.g. text size, font, overall configuration of the different blocks on the page, etc..

### Questions in more details

#### Question 1: text patterns in course objects

Consider the following exanmple:
```
C185A. Computational Linguistics I. (4) Requisites: courses 120B, C180, Program in Computing 10B. Recommended: course 165B or 200B, Program in Computing 60. Survey of recent work on natural language processing, including basic syntactic parsing strategies, with brief glimpses of semantic representation, reasoning, and response generation.
```
Is the bigram `Computational Linguistics` have a different representation from its use in, say, scientific papers? My gut feeling is that we don't know. In the current data, it sees this `Computational Linguistics` only once. So it doesn't have time to learn a subrepresentation of this bigram. What is perhaps constant is that such bigrams are surrounded by something like a `Course Number` and `Prequisites`. Again, that would mean llama2 needs to learn that something like `C185A` is a course number, and works as such. Can it really does that? It seems a bit different than predicting the next token in:
```
The dog was running in a _____
```
The usual insight here is that llama2 can do the previous example easily because it has an internal representation of `cats` and `dogs` in a house. In its training, it might have seen something about 'The cat walking in the bedroom' (example coming from [Bengio et al. 2003](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf). So it would predict something like `room`.

#### Question 2: working with full pages

In the [full page](https://github.com/jstonge/catempire/blob/main/single_full_page.txt) in the directory, what statistical patterns could separate one course from another, as well as one course from the following non-course?

#### Question 3: Noise

Consider the following examples:

<img width="570" alt="Screenshot 2024-04-11 at 6 18 33 PM" src="https://github.com/jstonge/catempire/assets/35715881/8fa448af-8f1d-4d8f-96d7-b431e17bfea2">

<img width="570" alt="Screenshot 2024-04-11 at 6 20 46 PM" src="https://github.com/jstonge/catempire/assets/35715881/19262f20-fd41-49c4-894a-c2cccdef20d0">

Counting words, the first example has something like 41 words, while the second is more around 50 words. But the token number for the first example is almost half of the second one because of bad parsing. Another different between noisy and clean text is what happens when you look at the number of unique encoded tokens. In the first example, there are 49 types for 59 tokens, while in the second example you get 71 types for 111 tokens. This make obvious sense in this case; single letters appear more often than well composed words, creating redudancy in the types. Is this a general pattern? Could we quantify a badly parsed text by looking at how bad is the ratio types/token ratio, given how [Byte-Pair Encoding](https://aclanthology.org/P16-1162/) works?

#### Question 5

Is text enough to solve questions 1, 2 and 4?

### Things we know from the literature

1. LLMs are able to do NER ([Zhou et al. 2023](https://universal-ner.github.io/)). Just by experimentatino, they can recognize entities such as organizations, places, persons, and so on. This should work well for distinguishing something like `Course Numbers` from boilerplate course pages. This is working less easily with longer Named Entities, such as `Course Description` (they can be a few sentences to few paragraphs long).

### Misc

1. Attention mechanism illustrated, from the [original paper](https://arxiv.org/pdf/1706.03762.pdf):

<img width="714" alt="Screenshot 2024-04-11 at 6 47 03 PM" src="https://github.com/jstonge/catempire/assets/35715881/f79790e2-eb34-4d46-b4ed-7958d56c3914">

