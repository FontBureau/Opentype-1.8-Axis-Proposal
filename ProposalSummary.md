# Proposal: Parametric Axes

## Administrative Information
**Proposers name:** Sam Berlow

**Vendor affiliation:** Type Network

**Proposal name:** Parametric Axes

**Date of submission:** 12/4/2017

**New or revised proposal:** New

**Previous revision date:** N/A

## General Technical Information
**Overview:**

Type users are familiar with the attributes of a typeface family.
Traditionally some of the most common attributes are available as named font instances (or styles) within font families, such as weight or width (e.g. Bold or Condensed.)
Some attributes are also already recorded in the font metadata fields of the OpenType v1.0 specification, such as values in the OS/2 table (e.g. x-height).
But these could not be altered by users, and this led to widespread misunderstandings about how typography is shaped by the attributes of typefaces.

The new variable fonts aspects of the OpenType v1.8 specification offers the potential to improve that situation.
It launched with some registered axes that pertain to these attributes, such as width and weight, and introduced new ones such as optical size.
This proposal contains axes pertaining to other attributes that all users are familiar with, such as descender length, and some that are less common, such as grade.

This proposal is for a set of axes that are inter-related, and form a gestalt system.
We carefully chose their axis tag names to convey their systematic nature.
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

We believe these axes allow type users, especially software developers and educators, to have a clearer picture of how typography is shaped by the attributes of typefaces.
These axes can be useful both when controlled by programs, or by changes input manually via user interfaces. 

By allowing type users to control these attributes in concert, and precisely, they enable a new kind of responsive typography.

**Related axes:** See individual axis proposals

**Similar axes:** See individual axis proposals

**Axis type:** Parametric

## Proposed Axis: `xtra`

**Tag:** xtra

**Name:** x transparent

**Axis type:** Parametric

**Description:** assigns a “white” per mille value to each instance of the design space

**Valid numeric range:**  -1000 to 2000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Applications may choose to select a variant in connection to an input, or it might be programmatically used

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** 

**Related axes:** wght, width, opsz

**Similar axes:** N/A

**Additional information:** 

**Conventionality benefits:** justification

**Interoperability benefits:** 

## Proposed Axis: `xopq`

**Tag:** xopq

**Name:** x opaque

**Axis type:** Parametric

**Description:** assigns a “black” per mille value to each instance of the design space

**Valid numeric range:**  -1000 to 2000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Applications may choose to select a variant in connection to an input or it might be programmatically used

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** 

**Related axes:** wght, width, opsz

**Similar axes:** N/A

**Additional information:** 

**Conventionality benefits:** Weight matching

**Interoperability benefits:** 

## Proposed Axis: `ytra`

**Tag:** ytra

**Name:** y transparent

**Axis type:** Parametric

**Description:** assigns an overall “white” per mille value to each instance

**Valid numeric range:**  0 to 2000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Applications may choose to select a variant in connection to an inpu, or it might be programmatically used

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** 

**Related axes:** yopq 

**Similar axes:** N/A

**Additional information:** 

**Conventionality benefits:** linespacing

**Interoperability benefits:** 

## Proposed Axis: `yopq`

**Tag:** yopq

**Name:** y opaque

**Axis type:** Parametric

**Description:** assigns a “black” per mille value to each instance of the design space

**Valid numeric range:**  -1000 to 2000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Applications may choose to select a variant in connection to an input or it may be programmatically used.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** 

**Related axes:** wght, width, opsz

**Similar axes:** N/A

**Additional information:** 

**Conventionality benefits:** contrasting

**Interoperability benefits:** 

## Proposed Axis: `ytlc`

**Tag:** ytlc

**Name:** y transparent lowercase

**Axis type:** Parametric

**Description:** assigns a “white” per mille value to each instance of the design space

**Valid numeric range:**  0 to 1000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Applications may choose to select a variant in connection to an input, or it might be programmatically used.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** 

**Related axes:** opsz, wght

**Similar axes:** N/A

**Additional information:** 

**Conventionality benefits:** height matching

**Interoperability benefits:** 

## Proposed Axis: `ytuc`

**Tag:** ytuc

**Name:** y transparent uppercase

**Axis type:** Parametric

**Description:** a “white” per mille value for each Uppercase Height in the design space

**Valid numeric range:**  -1000 to 1000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Applications may choose to select a variant in connection to an input or it might be programmatically used.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** 

**Related axes:** xtra, xopq 

**Similar axes:** hght

**Additional information:** 

**Conventionality benefits:** height matching

**Interoperability benefits:** 

## Proposed Axis: `ytde`

**Tag:** ytde

**Name:** y transparent descender

**Axis type:** Parametric

**Description:** assigns a “white” per mille value to each instance of the design space

**Valid numeric range:**  -1000 to 0

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Applications may choose to select a variant in connection to input, or i the axis be programmatically used with input like line-spacing

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** 

**Related axes:** ytra, ytuc, ytlc

**Similar axes:** N/A

**Additional information:** 

**Conventionality benefits:** linespacing

**Interoperability benefits:** 

## Proposed Axis: `ytas`

**Tag:** ytas

**Name:** y transparent ascender 

**Axis type:** Parametric

**Description:** assigns a “white” per mille value to each instance of the design space

**Valid numeric range:**  0 to 1000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Applications may choose to select a variant in connection to an input, or it might be programmatically used

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** 

**Related axes:** opsz, ytlc, ytde

**Similar axes:** N/A

**Additional information:** 

**Conventionality benefits:** linespacing

**Interoperability benefits:** 

## Proposed Axis: `pwth`

**Tag:** pwth

**Name:** Width (Parametric)

**Axis type:** Composite

**Description:** Used to vary width of text from narrower to wider; may be constructed by blending other primary axes, or via referenced instances of other
axes

**Valid numeric range:**  0 to 2000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Applications may choose to select a variant in connection to an input, or it might be programmatically used

**UI recommendations:** Primarily through end-user interfaces

**Script or language considerations:** 

**Related axes:** Always: xtra xopq. Sometimes: yopq ytos ytus

**Similar axes:** 

**Additional information:** This value range starts at 0 because if width is zero, counterforms are all closed in; if the XTRA value is negative, that doesn't matter in the blended axes. 

**Conventionality benefits:** 

**Interoperability benefits:** 

## Proposed Axis: `pwht`

**Tag:** pwht

**Name:** Weight (Parametric)

**Axis type:** Composite

**Description:** Used to vary stroke thicknesses or other design details to give variation from lighter to blacker; may be constructed by blending other primary axes, or via referenced instances of other
axes

**Valid numeric range:**  1 to 2000

**Scale interpretation:** Values can be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Applications may choose to select a variant in connection to an input, or it might be programmatically used

**UI recommendations:** Primarily through end-user interfaces

**Script or language considerations:** 

**Related axes:** Always: xtra xopq. Sometime: yopq ytlc ytos (y overshoot at xheight or above) ytus (y undershoot at baseline or below)

**Similar axes:** 

**Additional information:** This value range starts at 1 because if it was zero, no ink would be drawn. 

**Conventionality benefits:** 

**Interoperability benefits:** 

## Justification
**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**More info and demonstrations:** https://axes-proposal.typenetwork.com/
