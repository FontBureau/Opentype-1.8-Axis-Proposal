---
layout: page
title: Introduction
---

## {{ page.title }}

Our goal is to reveal how our useful variations fonts are built from axes that enable optical sizes, variation through time and motion, and multi-script integration (Latin/CJK/Arabic/Hebrew.)

This guide will be presented to the OpenType Variations working group. 
It was first published in June 2017.

### A. Parametric Latin Axes (9)

Typographers are familiar with many attributes of typefaces that express the Latin writing system.
It is useful for them be available as variation axes so that typographers can control them precisely. 

Some attributes are already recorded in fonts conforming to the OpenType v1.0 specification, as values in the OS/2 table 
(e.g. uppercase cap-height, lowercase x-height, or ascender/descender values.)
This group proposes new axes for these values. 

It also includes axes for other aspects that are inherent to all writing systems and specific to Latin: 
Controlling opaque or transparent areas in the X or Y dimensions. 

The OpenType v1.8.0 specification already offers registered (interoperable) axes for weight, width, and optical size. 
These axes can be created by composing the axes proposed in this section. 
This technique of constructing those 'higher level' axes by blending together 'lower level' axes means that typographers can control them with high precision. 

This set of axes form an inter-related and gestalt system. 
While it is useful for each of attribute to be available as variation axis, there is even greater value in having them form a cohesive system. 
As a set, a [network effect](https://en.wikipedia.org/wiki/Network_effect) is at play. 
The functionality for typographers increases exponentially as each attribute can be combined with the others, creating myriad possibilities. 
Registration in the OpenType specification will mean that this system becomes interoperable. 

### B. Treatment Axes (7)

Typographers apply decoration effects to type to create different forms of (highly stylized) emphasis. 
In the early days of digital type, many families did not have 'true' italics or bold weights, and application developers wrote auto-bold and auto-slant features, along with drop shadows, underlines, and so on. 
Since the introduction of TrueType, it has become much more common for type to be distributed in families with 'real' Bold, Italic, and Bold Italic styles. 

The use of the auto features for bold and italic is now disdained by typographers. 
The use of a standard underline effect was famously rejected by Medium, and became a global phenomenon that even the New York Times has adopted. 
Variation axes can provide decoration effects that refine decoration effects for typographers and give them more precise control that is fine tuned within ranges provided by typeface designers specific to each face, and also simplify the problem for application developers. 

### C. Parametric Non-Latin Axes (2) 

This group is similar to the first group, and extends the gestalt system with additional axes for typographers to better work with multilingual texts. 
The ability to adjust different fonts made for different writing systems to be used together in harmony is very useful for typographers. 
Often typographers must compromise in their use of one font to accommodate the requirements of another font, depending on which script is most important to them. 

In practice, often the values of these axes will be the same or related to the equivalent Latin axis. 
There are no existing values in the OpenType v1.7 specification for these aspects. 

Each script has unique alignment zones in the Y dimension. 
These axes allow precise control because their values are related to the em square. 

### D. Motion Axes (4)

In 1992, Font Bureau developed Zycon ([demo](http://www.axis-praxis.org/specimens/zycon)) to demonstrate how Variable Fonts can be used for motion typography. 
The essence of motion is a simple equation:

Distance = Rate × Time

These axes enable motion graphics designers to solve this equation without trial-and-error on each glyph.

While some may wonder if Variable Fonts "should" be used in this way. 
But the fact is that they already are used this way. 
The question is not about if this might fly, since they are flying already, but if they will fly in a way that is interoperable. 

With registration, reliable UIs can be made for motion graphics applications. 

### E. Glyph Axes (2)

"Don't Repeat Yourself"

These axes are not inter-related as groups 1 and 2 are, but have something in common:
The idea that good engineering means seeking simplicity and elegance by reducing duplication. 

Many Unicode characters can be expressed by a single glyph with variation along some axis. 
Therefore it would be good to be able to ask for a given Unicode character and get a position within a glyph's variation space where that character can be found. 
Similarly, alternate glyphs accessed through OpenType features could also be returned as locations in a variation space instead of duplicate glyph data. 
And these could be nested, like TrueType components. 

This would provide filesize reductions even within ASCII: 
A single glyph could express the lowercase o, uppercase O, zero and its OpenType figure feature alternates, and the zeros within the percentage sign. 


## Source Material

The proposal source material is available in tabular form in [Google Sheets](https://docs.google.com/spreadsheets/d/1lZcLW7xo39zG3TTv6EK3iLs5t8OjWWPJv0lb9qEnsDE)

This website is hosted on Github at [github.com/TypeNetwork/Opentype-1.8-Axis-Proposal](https://github.com/TypeNetwork/Opentype-1.8-Axis-Proposal)
