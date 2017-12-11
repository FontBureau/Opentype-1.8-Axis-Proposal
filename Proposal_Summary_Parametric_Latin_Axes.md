# Proposal: Parametric Latin Axes

## Administrative Information
**Proposers name:** Sam Berlow

**Vendor affiliation:** Type Network

**Proposal name:** Parametric Latin Axes

**Date of submission:** 12/11/2017

**New or revised proposal:** New

**Previous revision date:** N/A

## General Technical Information

**Overview**
This proposal provides a path to enable the upp
**Related axes:** YTUC, YTLC, YTDE, YTAS

**Similar axes:** None

**Axis type:** Parametric

## Proposed Axis Details: `ytlc`

**Tag:** ytlc

**Name:** y transparent lowercase

**Axis type:** Parametric

**Description:** assigns a “white” per mille value to each instance of the design space

**Valid numeric range:**  0 to 1000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may adjust the uppercase in coordination with another language or script, or adjust uppercase letters for a tv, vr, video setting to adjust to space, resolution or orientation.  

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Can be used for all scripts

**Related axes:**  wght, width, opsz

**Similar axes:** YTUC, YTDE, YTAS

**Additional information:** YTLC changes lowercase letters white space in the y direction. This axis contributes to opsz by raising the lowercase to increase legibility in small sizes. By allowing this axes to be used independently of opsz, the axis contributes to expanding the design space of a typeface.

## Justification

**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**Conventionality benefits:** The "x height" of lowercase Latin letters is an attribute that many users can point to, but rather than calling this axes "x height," we see conventionality benefits in a name that fits into the systematic structure of this overall proposal: Y dimension transparency of lower case letters. 

**Interoperability benefits:** height matching, design space

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-ytlc.gif)

## Proposed Axis Details: `ytuc`

**Tag:** ytuc

**Name:** y transparent uppercase

**Axis type:** Parametric

**Description:** a “white” per mille value for each Uppercase Height in the design space

**Valid numeric range:**  -1000 to 1000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may adjust the uppercase in coordination with another language or script, or adjust uppercase letters in a tv, vr, video setting to adjust to space, resolution or orientation.  

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Can be used for all scripts

**Related axes:** wght, width, opsz

**Similar axes:** YTLC, YTDE, YTAS

**Additional information:** YTUC changes the y direction or white space in uppercase letters. By itself, contributes to the design space when building of small, medium and tall capitals, or unicase. 

## Justification

**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**Conventionality benefits:** The height of the upper case Latin letters is an attribute that all users can easily point to, but rather than calling this axes "cap height," we see conventionality benefits in a name that fits into the systematic structure of this overall proposal: Y dimension transparency of upper case letters. 

**Interoperability benefits:** height matching, design space

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-ytuc.gif)

## Proposed Axis Details: `ytde`

**Tag:** ytde

**Name:** y transparent descender

**Axis type:** Parametric

**Description:** assigns a “white” per mille value to each instance of the design space

**Valid numeric range:**  -1000 to 0

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may adjust the descenders in coordination leading and column width to prevent letters from touching vertically.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Can be used for all scripts

**Related axes:** wght, width, opsz

**Similar axes:** YTUC, YTLC, YTAS

**Additional information:** YTDE changes the y or vertical descenders. Contributes to opsz in making small sizes fit better in text settings. Useful in adjusting letters when leading is reduced, in all sizes. Very useful in responsive design when headlines change from single lines to multiple lines of text.

## Justification

**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**Conventionality benefits:** The zone or general area that descenders live in is an attribute that all users can easily point to (along with collisions in this area suffered by fonts without it) but not an area they may know by name. This name fits into the systematic structure of this overall proposal: Y dimension transparency of descenders. 

**Interoperability benefits:** linespacing, design space

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-ytde.gif)

## Proposed Axis Details: `ytas`

**Tag:** ytas

**Name:** y transparent ascender 

**Axis type:** Parametric

**Description:** assigns a “white” per mille value to each instance of the design space

**Valid numeric range:**  0 to 1000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may adjust the ascenders in coordination leading and column width to prevent letters from touching vertically.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Can be used for all scripts

**Related axes:** wght, width, opsz 

**Similar axes:** YTUC, YTLC, YTDE

**Additional information:** YTAS changes the y or vertical ascenders. Contributes opsz in making type fit better when size is reduced.

## Justification

**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**Conventionality benefits:** The zone or general area that ascenders live in is an attribute that all users can easily point to (along with collisions in this area suffered by fonts without it) but not an area they may know by name. This name fits into the systematic structure of this overall proposal: Y dimension transparency of ascenders. 

**Interoperability benefits:** linespacing

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-ytas.gif)

