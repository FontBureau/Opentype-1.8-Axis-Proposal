## Introduction

Type users are familiar with the attributes of a typeface family.
Traditionally some of the most common attributes are available as named font instances (or styles) within font families, such as weight or width (e.g. Bold or Condensed.)
Some attributes are also already recorded in the font metadata fields of the OpenType v1.0 specification, such as values in the OS/2 table (e.g. x-height).
But these could not be altered by users, and this led to widespread misunderstandings about how typography is shaped by the attributes of typefaces.

The new variable fonts aspects of the OpenType v1.6 specification offers the potential to improve that situation.
It launched with some registered axes that pertain to these attributes, such as width and weight, and introduced new ones such as optical size.
This proposals contain axes pertaining to other attributes, such as grade and descender length.

An important aspect of this proposal is that it is for a set of axes that are inter-related.
Their inter-relation, and our focus on typography, led us to design a unified value system for them all.
The axis tag names were carefully chosen to convey their systematic nature.
Another benefit of this inter-relation is its implications for filesize;
we believe that these axes are useful today in released fonts (e.g. Amstelvar) and they can become even more efficient with future changes to the OpenType specification.
(But that is no reason to delay their registration.)

We also want to note that this proposal is limited to Latin, intentionally.
During the development of this proposal we were concerned with multi-script typography, where Latin and non-Latin scripts are used together on a page.
Since different scripts have different vertical proportion attributes, we see a need for more axes than are contained here.
We will make a second proposal with those, if this proposal is accepted.

We believe these axes allow type users, especially software developers and educators, to have a clearer picture of how typography is shaped by the attributes of typefaces.
These axes can be useful when controlled both by programs, or by changes input manually via user interfaces. 

By allowing type users to control these attributes in concert, and precisely, they enable a new kind of responsive typography.
