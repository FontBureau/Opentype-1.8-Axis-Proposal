# Font Bureau OpenType 1.8 Variations Axes Proposals

[Source Spreadsheet](https://docs.google.com/spreadsheets/d/13QZl_mnEyV4IgJWO_ysGEClQAoX500tdxEsAlJPF_TQ/edit#gid=0)


Primary Axes Proposal

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

The functionality for typographers increases exponentially as each attribute can be combined with the others, creating myriad possibilities. 

Registration in the OpenType specification will mean that this system becomes interoperable. 
