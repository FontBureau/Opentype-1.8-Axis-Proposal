# Proposal: Universal Parametric Axes

## Administrative Information
**Proposers name:** Sam Berlow

**Vendor affiliation:** Type Network

**Proposal name:** Parametric Axes

**Date of submission:** 12/11/2017

**New or revised proposal:** New

**Previous revision date:** N/A

## General Technical Information

**Overview**

**Related axes:** XTRA, YTRA, XOPQ, YOPQ

**Similar axes:** None

**Axis type:** Parametric

## Proposed Axis Details: `xtra`

**Tag:** xtra

**Name:** x transparent

**Axis type:** Parametric

**Description:** assigns a “white” per mille value to each instance of the design space

**Valid numeric range:**  -1000 to 2000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: by setting a maximum word space parameter, and adjusting the XTRA units to a min and max. A developer could adjust justified text without tracking letters. Maintaining the apparent weight and width. 

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Can be used for all scripts

**Related axes:** wght, width, opsz

**Similar axes:** YTRA, XOPQ, YOPQ

**Additional information:** XTRA changes the white space in the x or horizontal direction. This useful in adjusting type horizontally without changing the opaque (black) Useful in VR, TV, and justification of text blocks.

## Justification

**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**Conventionality benefits:** "White space" or "Negative Shapes" are common concepts in visual arts, but many users don't think about the transparent area of type deconstructed (or essentially isolated) to the X dimension. This axes helps users to structure their thinking about white space horizontally, for the overall/total typeface.

**Interoperability benefits:** justification, legibility

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-xtra.gif)

## Proposed Axis Details: `xopq`

**Tag:** xopq

**Name:** x opaque

**Axis type:** Parametric

**Description:** assigns a “black” per mille value to each instance of the design space

**Valid numeric range:**  -1000 to 2000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Combined with YOPQ, a program or script can adjust each parameter to improve legibility at small sizes.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Can be used for all scripts

**Related axes:** wght, width, opsz

**Similar axes:** XTRA, YTRA, YOPQ

**Additional information:** XOPQ changes the black in the x or horizontal direction. By itself it expands the design space, by providing reverse contrast. Combined with YOPQ it can create more legible type at small sizes in platforms where hinting is not available.

## Justification

**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**Conventionality benefits:** "Black space" or "Positive Shapes" are common concepts in visual arts, but many users don't think about the 'opaque' area of type deconstructed (or essentially isolated) to the X dimension. This axes helps users to structure their thinking about positive shapes horizontally, for the overall/total typeface.

**Interoperability benefits:** Weight matching, design space

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-xopq.gif)

## Proposed Axis Details: `ytra`

**Tag:** ytra

**Name:** y transparent

**Axis type:** Parametric

**Description:** assigns an overall “white” per mille value to each instance

**Valid numeric range:**  0 to 2000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may choose to adjust YTRA in order to change the height of glyphs to emphasize text or headline, fit text to a space, stack and justify text.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Can be used for all scripts

**Related axes:** yopq 

**Similar axes:** XTRA, XOPQ, YTRA

**Additional information:** YTRA changes the white space in the y or vertical direction. Combined with other axes it contributes to opsz, potentially HGHT among many options.

## Justification

**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**Conventionality benefits:** "White space" is a common concept in visual arts, but many users don't think about the 'transparent' area of type deconstructed (or essentially isolated) to the Y dimension. This axes helps users to structure their thinking about white space vertically, for the overall/total typeface.

**Interoperability benefits:** linespacing, design space

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-ytra.gif)

## Proposed Axis Details: `yopq`

**Tag:** yopq

**Name:** y opaque

**Axis type:** Parametric

**Description:** assigns a “black” per mille value to each instance of the design space

**Valid numeric range:**  -1000 to 2000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Combined with XOPQ, a program or script can adjust each parameter to improve legibility at small sizes.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Can be used for all scripts

**Related axes:** wght, width, opsz

**Similar axes:** XTRA, YTRA, XOPQ

**Additional information:** YOPQ changes the black in the y or vertical direction. By itself it expands the design space, by providing reverse contrast. Combined with XOPQ it can create more legible type at small sizes in platforms, and languages where hinting is not available.

## Justification

**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**Conventionality benefits:** "Black space" or "Positive Shapes" are common concepts in visual arts, but many users don't think about the 'opaque' area of type deconstructed (or essentially isolated) to the Y dimension. This axes helps users to structure their thinking about positive shapes vertically, for the overall/total typeface.

**Interoperability benefits:** contrasting, design space, legibility

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-yopq.gif)