## Text preprocess
Preprocess text, transfer them into format used by language model.

## Get started
- The main entry is at `text_preprocess_main.py`.
- Maybe you should uncomment the code in the `text_preprocess_main.py`.

## 步骤
1. Conversion coding.
2. Convert marked text to XML documents.
3. Get the text inside the elements of 'content' and 'contenttitle'.
4. Turn full-width characters into half-width.
5. Remove the comma within the number.
6. Cut words according to pause symbos and spaces.
7. Continue to clean the text (remove text like "福彩", remove spaces that should not appear, remove lines that do not contain Chinese).
8. Convert the encoding format to GBK.
9. Using Baidu lexical analysis to segment text.
10. Replace named entities and numbers with corresponding identifiers.
