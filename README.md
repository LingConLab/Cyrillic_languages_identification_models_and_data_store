# Cyrillic alphabet languages identification

## About

Our models aim to identify language of each graphical word in a string. These models can be useful for extracting code-switching or citations in the string containing several languages using Cyrillic alphabet.


## Project structure

This repo stores the cleaned data (*.zip* files) and the finalized models (*.pickle* files).

[The function implementing a given model can be found in different repo.](https://github.com/LingConLab/Cyrillic_languages_identification_user_function_store)

Scripts for the automatic download Wikipedia dumps using Cyrillic alphabets can be found [here]() (can be used for the future data gathering).

[This .ipynb notebook](https://github.com/LingConLab/Cyrillic_languages_identification_models_and_data_store/blob/main/Showing_models_performance.ipynb) illustrates methodology of model training and performance with the confusion matrices.


## Dataset

| Languages | Source  |
| :--------------|:-----------:|
|  Abaza, Yakut, Moksha, Komi, Kyrgyz, Kazakh, Erzya, Buryat, Ukrainian, Russian, Belarusian | [Universal Dependencies treebanks V.2.11](http://hdl.handle.net/11234/1-5150), **NOTE:** both Komi Permyak and Komi Zyria data are treated as "Komi"|
| Kumyk | custom corpus: news texts web-scraped from [yoldash](https://yoldash.ru/), "Тангчолпан" 2013 literature magazines  |
| Adyghe | dictionaries |
| Avar | [Avar wiki dump](https://dumps.wikimedia.org/avwiki/20231101/), processed with [this script](https://github.com/apertium/WikiExtractor)|

Due to some experiments we draw a conclusion that teh following procedures improtve accuracy metrics:

| Additional preprocessing | Languages |
| :----- | :-------:|
| *Infuse with palochka variants*: [Cyrillic Palochka](https://en.wikipedia.org/wiki/Palochka) appears to be written with "1" or Latin "I" in natural texts. For each word containing one of these variants we added identical words with two other variants of spelling to the dataset | Abaza,Adyghe,Avar |
| *Remove PROPN words*: remove words with "PROPN" pos-tag in the UD treebanks data subset |Abaza, Yakut, Moksha, Komi, Kyrgyz, Kazakh, Erzya, Buryat, Ukrainian, Russian, Belarusian|
|*Remove infrequent words appered to be Russian code-switching/unadapted borrowings*: we removed nouns with less than 10 occurences in the corpora which matched with entries in the morphological dictionary of Russian| Avar, Kumyk|

**More available languages** that can be added in the future: Bulgarian (is presented in the UD treebanks) + numerous languages of Wikipedia

The following map represents correspondances between the names of languages with Cyrillic alphabets and their tags in Wikipedia. Data for these languages can be downloaded and unpacked with the **.py scripts in this repo**.

``` json
{
   "Russian": "ru",
   "Ukrainian": "uk",
   "Serbian": "sr",
   "Chechen": "ce",
   "Tatar": "tt",
   "Serbo-Croatian": "sh",
   "Bulgarian": "bg",
   "Uzbek": "uz",
   "Belarusian": "be",
   "Kazakh": "kk",
   "Macedonian": "mk",
   "Tajik": "tg",
   "Belarusian (Tara\u0161kievica orthography)": "be-tarask",
   "Kyrgyz": "ky",
   "Bashkir": "ba",
   "Chuvash": "cv",
   "Mongolian": "mn",
   "Ossetic": "os",
   "Yakut": "sah",
   "Eastern Mari": "mhr",
   "Western Mari": "mrj",
   "Rusyn": "rue",
   "Erzya": "myv",
   "Abkhazian": "ab",
   "Udmurt": "udm",
   "Komi": "kv",
   "Lezghian": "lez",
   "Moksha": "mdf",
   "Tuvinian": "tyv",
   "Komi-Permyak": "koi",
   "Avaric": "av",
   "Russia Buriat": "bxr",
   "Ingush": "inh",
   "Karachay-Balkar": "krc",
   "Kalmyk": "xal",
   "Kabardian": "kbd",
   "Lak": "lbe",
   "Church Slavic": "cu",
   "Southern Altai": "alt",
   "Adyghe": "ady"
}
```