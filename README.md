## The Catalog Empire

Small repo where im thinking about how LLMs like llama2 are seeing course objects in course catalogs.

`courses.txt` contains the course objects annotated in the REA project (as of 2024-04-11; see Label-Studio for the people who know what im talking about). Each line is a course object. You don't know where they come from. You only have (noisy) texts of course catalogs.

`full_page.txt` is an exemplar of a page full of course catalogs.

The goals are the following:

1. Given a list of course objects, are there statistical regularities that would lead FMs to have a different representations of words in the course objects than same words used in non-course catalog contexts?
1. Given what we know from llama2's transformer architecture, is there a way it could easily learn to delineate course objects from one another?
1. Is text enough to answer the previous questions? What would we gain by somehow introducing the layout that is present in the PDF, e.g. text size, font, overall configuration of the different blocks on the page, etc..

### Questions in more details

#### Question 1

Consider the following exanmple:
```
C185A. Computational Linguistics I. (4) Requisites: courses 120B, C180, Program in Computing 10B. Recommended: course 165B or 200B, Program in Computing 60. Survey of recent work on natural language processing, including basic syntactic parsing strategies, with brief glimpses of semantic representation, reasoning, and response generation.
```
Is the bigram `computational linguistics` have a different representation than how people talk about that in papers? My gut feeling is that we don't know. In the current annotated data, it sees that bigram only once. So it doesn't have time to learn a subrepresentation for those words. What is perhaps constant is that those bigrams are surrounded by something like a `Course Number` and `Prequisites`.

#### Question 2

In the [full page](https://github.com/jstonge/catempire/blob/main/single_full_page.txt) in the directory, what statistical patterns could separate one course from another, as well as one course from the following non-course?

#### Question 3

Is text enough to solve questions 1 and 2?