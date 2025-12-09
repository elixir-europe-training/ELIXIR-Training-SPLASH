---
title: Style guide
---

In general, we follow the European Commission's [Web Writing Style Guide](https://wikis.ec.europa.eu/display/WEBGUIDE/02.+Web+writing+guidelines) and the more detailed [English Style Guide](https://commission.europa.eu/system/files/2023-01/styleguide_english_dgt_en.pdf). Below are the points that you might find most useful, though, and that relate particularly to the Training SPLASH.

## General style and tone
  * Keep the tone friendly rather than formal, and use "you". Imagine you were explaining something verbally to someone - how would you say it?
  * Use short, active sentences and short paragraphs (3-4 sentences).
  * Make use of headings and bullet points to break text up so it is easy to scan.
  * Remember that the site is there to help people, so make it clear to the readers how the information can benefit them.
  * Use the words your readers would use. Think of the terms they would use when searching for their problem, and use those terms.

## Text
  * **Acronyms:** use the [glossary file](_data/glossary.yml) and [these instructions](https://github.com/erikw/jekyll-glossary_tooltip#usage) to spell out acronyms in an accessible way.
  * **Ampersands:** do not use these in the main text or headings. It is fine to use them in menus, if you need to save space.
  * **Capitals:** do not use all capitals for emphasis or in headings.
  * **Data:** treat as singular ("Data is..."). (Whether "data" is singular or plural is contentious - see the [Wikipedia article](https://en.wikipedia.org/wiki/Data_(word)) and this [Guardian article](https://www.theguardian.com/news/datablog/2010/jul/16/data-plural-singular).)
  * **Dates:** use Wednesday 7 July 2021 (not Wednesday 7th July 2021, or other variations).
  * **Datasets:** not "data sets".
  * **Email:** not "e-mail".
  * **Email addresses:** spell these out and make the email address the link e.g. [training-splash@elixir-europe.org](training-splash@elixir-europe.org). Do not hide the email address behind a word or phrase like "contact us".
  * **Etc.** should be avoided. Try using ‘for example’ or ‘such as’ or ‘including’ at the start of a listing. If etc. is used, put a comma before it if it is in a list, like "A, B, etc.". 
  * **Gender:** avoid using gender-specific words like "he" or "she".
  * **Headings:**
    * Only the first word is capitalised, unless other words are proper nouns.
    * Headings must be hierarchical. They must go down in order (level one, level two, level three), and not skip a level. It is fine to skip levels when moving back up e.g. you can skip from level four to level two.
  * **-ise/-ize:** use the "-ise" form.
  * **Lifecycle:** a single word.
  * **Links:** make the link text say where the link goes e.g. "the Contribute page", not "click here". Avoid using the url as the link text.
  * **Lists:** 
    * _A list of short items_: introduce with a colon, start each bullet point with a capital and don't use punctuation at the end of each bullet point:
      * Item 1
      * Item 2
    * _A list of longer items following an incomplete introductory sentence (e.g. a sentence ending in a colon)_: each item ends with a semi colon and the final item ends with a full stop. Do not capitalise the first letter of each item e.g. This is the first part of a sentence that includes:
      * a longer item 1;
      * a longer item 2;
      * a longer item 3.
    * _A list following a complete sentence (with a full stop)_: each item ends with a full stop and each point begins with a capital letter e.g. This a complete sentence.
      * This is item 1 of the list.
      * This is item 2 of the list.
      * This is item 3 of the list.
  * **Numbers:** spell the numbers one to ten out. After that, write the numbers (11, 12, 13, etc.).
  * **Quotations:** use double quotes for quotations, and single quotes for quotes within quotes.
  * **References:** use the [Nature Author instructions](https://www.nature.com/srep/author-instructions/submission-guidelines#references) for books and papers. Use "*et al.*" for more than five authors.
    * Bellin, D. L. *et al.* Electrochemical camera chip for simultaneous imaging of multiple metabolites in biofilms. Nat. Commun. 7, 10535; [10.1038/ncomms10535](http://www.nature.com/articles/ncomms10535) (2016).
    * Lam, J. <cite>Data Management</cite>. (John Wiley & Sons, Inc., 2019).
  * **That/which:** use "that" when you are defining something and "which" when you are adding extra information about it e.g.:
    * "The cat that was on the table suddenly got up" is telling us which cat it was. It is important to the meaning of the sentence because you are not talking about any cat, just the cat on the table.
    * "The cat, which was sitting on the table, suddenly got up" is giving us extra information about the cat. The information is not necessary to understand the sentence. You can remove the clause and the sentence will still be clear. Clauses starting with "which" usually begin with a comma.
  * **Titles (the "title" in the front matter of pages):** only the first word, proper nouns and acronyms are capitalised.
  * **Tool assembly:** there are multiple tools in **one** assembly. The plural is "tool assemblies".
  * **Training:** training is an uncountable noun and cannot have a plural. You can write "training courses" and "training materials" but not "trainings".

## Graphic design
  * **White space:** make sure there is plenty of space so that the main elements stand out and the text does not appear overwhelming.
  * **Colours:**
    * The headings, links and text will automatically appear in the right colour if you use the site page templates.
    * Use only the following colours in the design, text and illustrations of the site:
    
    | Color Sample | Hex Code | Name | Usage |
    |--------------|----------|------|-------|
    | <span style="display: inline-block; width: 20px; height: 20px; background: #4F1C46;"></span> | #4F1C46 | Aubergine | Primary theme color, buttons, highlights |
    | <span style="display: inline-block; width: 20px; height: 20px; background: #005472;"></span> | #005472 | Blue | Links, secondary accents |
    | <span style="display: inline-block; width: 20px; height: 20px; background: #CA1551;"></span> | #CA1551 | Red | Alerts, important notices |
    | <span style="display: inline-block; width: 20px; height: 20px; background: #03CEA4;"></span> | #03CEA4 | Green | Success messages, positive actions |
    | <span style="display: inline-block; width: 20px; height: 20px; background: #FF7900;"></span> | #FF7900 | Orange | Warnings, highlights |
    | <span style="display: inline-block; width: 20px; height: 20px; background: #4D4848;"></span> | #4D4848 | Dark gray | Secondary text, subtle elements |
    | <span style="display: inline-block; width: 20px; height: 20px; background: #212529;"></span> | #212529 | Dark | Body text, headings |
    
  * **Fonts:** Lato is used for both headings and body text across the site.
  * **Icons:** Icons on this site come from [Font Awesome](https://fontawesome.com/).
  * **Templates:** keep the structure of the pages consistent by using the site templates (see the [contributing guide](contributing_via_github)).
  * **Illustrations:** use the colours listed above. If you need help with illustrations, [open a new issue](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/issues) on GitHub or email [training-splash@elixir-europe.org](mailto:training-splash@elixir-europe.org).
  * **Images:**
    * Do not use images to display text.
    * Include an 'alt' attribute in images for accessibility.

## Naming of files, tags, keywords, and navigation titles

* **Markdown file names:**
  * Do not contain spaces or special characters like &, %, #, (, ), è, é, ê, ë, ...
  * Are unique among the website.
  * Are lowercase, except for acronyms.
* **Tags for tools, resources and pages:**
  * Do not contain special characters like &, %, #, (, ), è, é, ê, ë, ...
  * Are lowercase, except for acronyms.
  * Are short if possible, but distinguishable from existing tags.
  * Can contain spaces.
* **Keywords:**
  * Are lowercase.
  * Can contain spaces.
* **Titles in the navigation side panel:**
  * First word and acronyms capitalised.
  * Should contain the same words as the filename where this title points to.


## How to suggest amendments or additions to this style guide:
[Open a new issue](https://github.com/elixir-europe-training/ELIXIR-Training-SPLASH/issues) on GitHub or email [training-splash@elixir-europe.org](mailto:training-splash@elixir-europe.org). See also the [contribute page](how_to_contribute).
