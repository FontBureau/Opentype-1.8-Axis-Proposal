## Introduction

Type users are familiar with the attributes of a typeface family.
Traditionally some of the most common attributes are available as named font instances (or styles) within font families, such as weight or width (e.g. Bold or Condensed.)
Some attributes are also already recorded in the font metadata fields of the OpenType v1.0 specification, such as values in the OS/2 table (e.g. x-height).
But these could not be altered by users, and this led to widespread misunderstandings about how typography is shaped by the attributes of typefaces.

The new variable fonts aspects of the OpenType v1.8 specification offers the potential to improve that situation.
It launched with some registered axes that pertain to these attributes, such as width and weight, and introduced new ones such as optical size.
This proposal contains axes pertaining to other attributes that all users are familiar with, such as descender length, and some that are less common, such as grade.

This proposal is for a set of axes that are inter-related, and form a gestalt system.
We designed their numeric ranges as a unified set, built on typographic tradition where the sizes of shapes are reasoned about in per-mille-of-em.

The most important aspect of the system is that it can be used to compose ‘higher level’ axes by blending together ‘lower level’ axes, so that users can control the parameters of high level type attributes with precision.
While the OpenType v1.8.0 specification already has registered axes for weight and width, we are proposing ‘Parametric Weight’ and ‘Parametric Width’ axes that are free from backwards compatibily concerns, and offer the same per-mille-of-em user experience as our other axes. 

Such composition has implications for filesize;
we believe that these axes are useful today in released fonts (e.g. Amstelvar) and they can become even more efficient with future changes to the OpenType specification for composing axes. 
But that is no reason to delay their registration.
While it would be useful to register each axis to make it individually interopable, making the system interoperable is essential to realising its full value.
A network effect is at play:
The potential functionality for typographers increases as each attribute can be combined with the others, creating exponential possibilities.

We also want to note that this proposal is limited to Latin, intentionally.
During the development of this proposal we were concerned with multi-script typography, where Latin and non-Latin scripts are used together on a page.
Since different scripts have different vertical proportion attributes, we see a need for more axes than are contained here.
We will make a second proposal with those, if this proposal is accepted.

However, this proposal does include axes that change attributes inherent to all writing systems:
Controlling overall opaque or transparent area in X or Y dimensions (`xtra`, `ytra`, `xopq`, `yopq`)
This deconstruction of letterforms leads to the most expansive design spaces, and in turn those create the biggest potential for improvements to typography, especially enhancements that are achieved through responsive programming.
Conventionality is one of the benefits of registration, and we carefully chose these axis names and tags to convey their systematic nature.

We believe these axes allow type users, especially software developers and educators, to have a clearer picture of how typography is shaped by the attributes of typefaces.
These axes can be useful both when controlled by programs, or by changes input manually via user interfaces. 

By allowing type users to control these attributes in concert, and precisely, they enable a new kind of responsive typography.
