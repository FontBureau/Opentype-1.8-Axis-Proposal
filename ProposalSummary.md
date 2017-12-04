# Proposal: Parametric Axes

## Administrative Information
**Proposers name:** Sam Berlow

**Vendor affiliation:** Type Network

**Proposal name:** Parametric Axes

**Date of submission:** 12/4/2017

**New or revised proposal:** New

**Previous revision date:** N/A

## General Technical Information
**Overview:** Type users are familiar with the attributes of a typeface family that combine to make up its appearance. Traditionally, these attributes are available as named and instantiated styles in font families. Some of these attributes are already recorded in fonts conforming to the OpenType v1.0 specification, as values in the OS/2 table, and in other tables of the SFNT format in general.

Today's font families contain instances pertaining to attributes of registered axes of OpenType, like width, weight, and optical size. In addition, some existing font families contain instances pertaining to grades, descender length, multiscript font mixing for different vertical proportions, and font families contain instances made for specific output, or with specific data to suit particular platform requirements.

This proposal is for a new and more complete set of typographic axes, with a unified value system, concern for non-Latin, responsive typography, compression, and more. The registration of a full set of attributes allows type developers to combine the modern, potentially much larger font family into a single file; it allows software developers and educators to have a clearer picture of how typography is shaped by the basic attributes; and it allows type users to control the attributes more precisely, whether that control is programmatic or manual via a user interface.

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
