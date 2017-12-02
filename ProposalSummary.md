# Proposal: Parametric Axes

## Administrative Information
**Proposers name:** Sam Berlow

**Vendor affiliation:** Type Network

**Proposal name:** Parametric Axes

**Date of submission:** 12/1/2017

**New or revised proposal:** New

**Previous revision date:** N/A

## General Technical Information
**Overview:** Typographers are familiar with many attributes of typefaces that express the Latin writing system. It is useful for them be available as variation axes so that typographers can control them precisely.

Some attributes are already recorded in fonts conforming to the OpenType v1.0 specification, as values in the OS/2 table (e.g. uppercase cap-height, lowercase x-height, or ascender/descender values.) This group proposes new axes for these values: **ytlc, ytuc, ytde, ytas**

It also includes axes for other aspects that are inherent to all writing systems and specific to Latin: Controlling opaque or transparent areas in the X or Y dimensions: **xtra, xopq, ytra, yopq**

The OpenType v1.8.0 specification already offers registered (interoperable) axes for weight, width, and optical size. These axes can be created by composing the axes proposed in this section. This technique of constructing those ‘higher level’ axes by blending together ‘lower level’ axes means that typographers can control them with high precision.

This set of axes form an interrelated and gestalt system. While it is useful for each of these attributes to be available as variation axis, there is even greater value in having them form a cohesive system. As a set, a network effect is at play. The functionality for typographers increases exponentially as each attribute can be combined with the others, creating myriad possibilities. Registration in the OpenType specification will mean that this system becomes interoperable.

**Related axes:** ytlc, ytuc, ytde, ytas, xtra, xopq, ytra, yopq

**Similar axes:** none

**Axis type:** Parametric

## Proposed Axis Details

### Axis: x Transparent ('xtra')

**Tag:** xtra

**Name:** x Transparent

**Description:** Assigns a “white” per mille value to each instance of the design space

**Valid numeric range:** -1000 to 2000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required &ldquo;Regular&rdquo; value:** N/A

**Suggested programmatic interactions:** justification of text, Replace Horizontal Scale

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** N/A

**Additional information:** See demonstrations in `demonstrations/index.hml`

### Axis: y Transparent ('ytra')

**Tag:** ytra

**Name:** y Transparent

**Description:** Assigns an overall “white” per mille value to each instance

**Valid numeric range:** 0 to 2000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required &ldquo;Regular&rdquo; value:** N/A

**Suggested programmatic interactions:** linespacing

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** N/A

**Additional information:** See demonstrations in `demonstrations/index.hml`

### Axis: x Opaque ('xopq')

**Tag:** xopq

**Name:** x Opaque

**Description:** Assigns a “black” per mille value to each instance of the design space

**Valid numeric range:** -1000 to 2000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required &ldquo;Regular&rdquo; value:** N/A

**Suggested programmatic interactions:** weight matching

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** N/A

**Additional information:** See demonstrations in `demonstrations/index.hml`

### Axis: y Opaque ('yopq')

**Tag:** yopq

**Name:** y Opaque

**Description:** Assigns a “black” per mille value to each instance of the design space

**Valid numeric range:** -1000 to 2000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required &ldquo;Regular&rdquo; value:** N/A

**Suggested programmatic interactions:** contrasting, screen legibility

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** N/A

**Additional information:** See demonstrations in `demonstrations/index.hml`

### Axis: y Transparent Lowercase ('ytlc')

**Tag:** ytlc

**Name:** y Transparent Lowercase

**Description:** Assigns a “white” per mille value to lowercase glyphs

**Valid numeric range:** 0 to 1000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required &ldquo;Regular&rdquo; value:** N/A

**Suggested programmatic interactions:** height matching

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** N/A

**Additional information:** See demonstrations in `demonstrations/index.hml`

### Axis: y Transparent Uppercase ('ytuc')

**Tag:** ytuc

**Name:** y Transparent Uppercase

**Description:** Assigns a “white” per mille value to uppercase glyphs

**Valid numeric range:** -1000 to 1000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required &ldquo;Regular&rdquo; value:** N/A

**Suggested programmatic interactions:** height matching

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** N/A

**Additional information:** See demonstrations in `demonstrations/index.hml`

### Axis: y Transparent Ascenders ('ytas')

**Tag:** ytas

**Name:** y Transparent Ascenders

**Description:** Assigns a “white” per mille value to each instance of the design space

**Valid numeric range:** 0 to 1000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required &ldquo;Regular&rdquo; value:** N/A

**Suggested programmatic interactions:** linespacing

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** N/A

**Additional information:** See demonstrations in `demonstrations/index.hml`

### Axis: y Transparent Descenders ('ytde')

**Tag:** ytde

**Name:** y Transparent Descenders

**Description:** Assigns a “white” per mille value to each instance of the design space

**Valid numeric range:** -1000 to 0

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required &ldquo;Regular&rdquo; value:** N/A

**Suggested programmatic interactions:** linespacing

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** N/A

**Additional information:** See demonstrations in `demonstrations/index.hml`

## Justification
**Vendor commitments:** Font Bureau, TYPETR, Google Fonts

**Conventionality benefits:** This proposal does not seek to classify the designs of typefaces parametrically, only what the values of the parameters are. Furthermore, it is offered as a beginning, suggesting the need for—but not containing—suggestions for many important attributes of non-Latin fonts.

The registration of the axes here is also intended to be used as part of a system including the registration of what function an axis performs for programs and/or users along the existing path from script selection to the rendered glyph in a document, aka the Mantra. Documentation of that part of the system, including the registration of what function an axis provides, is still in development and will follow soon.

Type users are familiar with the attributes of a typeface family that combine to make up its appearance. Traditionally, these attributes are available as named and instantiated styles in font families. Some of these attributes are already recorded in fonts conforming to the OpenType v1.0 specification, as values in the OS/2 table, and in other tables of the SFNT format in general.

Today's font families contain instances pertaining to attributes of registered axes of OpenType, like width, weight, and optical size. In addition, some existing font families contain instances pertaining to grades, descender length, multi-script font mixing for different vertical proportions, and font families contain instances made for specific output, or with specific data to suite particular platform requirements.

**Interoperability benefits:** TK
