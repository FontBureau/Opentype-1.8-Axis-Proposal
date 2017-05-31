# Font Bureau OpenType 1.8 Variations Axes Proposals

This guide will be presented to the OpenType Variations working group. 

Our goal is to reveal how our useful variations fonts are built from axes that enable optical sizes, variation through time and motion, and multi-script integration (Latin/CJK/Arabic/Hebrew.)

## Summary

This axes list contains several different kinds of axes. Nearly every value found in an otf 1.0 to the present, referring to a typographic value in the font, is susceptible to the need for a registered axis to identify that which can be defined as a variation in a font (ytlc and xtab are examples of those). Variations add the possibilities of motion, space and time, and inter-script adjustment, and thus the need for axes to be added for interoperable programmability among variations fonts dealing with animation and parameters specific to non-latin scripts.
(This seems a lot to register compared to the registration rate so far, which would have left us enough axes to last around 440,000 years. But here are 25 axes, proposed, if the community so chooses to adopt them as standards.)

## Overview

Our proposal contains several groups for axes registration including: 

### 1. Latin Axes (11)

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
Registration in the OpenType specification will mean this system becomes interoperable. 

### 2. Non-Latin Axes (7) 

This group is similar to the first group, and extends the gestalt system with additional axes for typographers to better work with multilingual texts. 
The ability to adjust different fonts made for different writing systems to be used together in harmony is very useful for typographers. 
Often typographers must compromise in their use of one font to accomodate the requirements of another font, depending on which script is most important to them. 

In practice, often the values of these axes will be the same or related to the equivalent Latin axis. 
There are no existing values in the OpenType v1.7 specification for these aspects. 

Each script has unique alignment zones in the Y dimension. 
These axes allow precise control because their values are related to the em square. 

### 3. Motion Axes (4)

In 1992, Font Bureau developed Zycon ([demo](http://www.axis-praxis.org/specimens/zycon)) to demonstrate how Variable Fonts can be used for motion typography. 
The essense of motion is a simple equation:

Distance = Rate × Time

These axes enable motion graphics designers to solve this equation without trial-and-error on each glyph.

While some may wonder if Variable Fonts "should" be used in this way. 
But the fact is that they already are used this way. 
The question is not about if this might fly, since they are flying already, but if they will fly in a way that is interoperable. 

With registration, reliable UIs can be made for motion graphics applications. 

### 4. Don't Repeat Yourself (2)

These axes are not inter-related as groups 1 and 2 are, but have something in common:
The idea that good engineering means seeking simplicity and elegance by reducing duplication. 

Many Unicode characters can be expressed by a single glyph with variation along some axis. 
Therefore it would be good to be able to ask for a given Unicode character and get a position within a glyph's variation space where that character can be found. 
Similarly, alternate glyphs accessed through OpenType features could also be returned as locations in a variation space instead of duplicate glyph data. 

And these could be nested, like TrueType components. Then for an example within the ASCII glyph set, this would mean a single round glyph's variation space could express the lowercase o, uppercase O, various forms of zero associated with OpenType figures, and the zeros within the percentage sign. 
