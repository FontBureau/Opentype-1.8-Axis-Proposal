
# Proposal: Parametric and Optical Axes

## Administrative Information
**Proposers name:** Sam Berlow

**Vendor affiliation:** Type Network

**Proposal name:** Parametric Axes

**Date of submission:** 12/5/2017

**New or revised proposal:** New

**Previous revision date:** N/A

## General Technical Information
**Overview: Axes Proposal Part I**

Most type users are familiar with the weight, width and postural (slant), attributes of a typeface family, and many users are familiar with fonts mastered for different optical size ranges. Traditionally some of the most common attributes are available as named font instances (or styles) within font families. These attributes are recorded in the font metadata fields of the OpenType v1.0 specification, along with other values in the OS/2 table (e.g. cap height and x-height). But these could not be altered by users, and this led to widespread simplification about how typography is formed from the attributes of typefaces.

Increasing numbers of type users over the past quarter century of static type composition, as for print, with this meta data applied to Latin and other world scripts, have found difficulties with the limited metadata, and compositions mixing scripts in use can involve users wanting to manipulate more parameters than the format contains, or applications offer. In addition, and combinatorially, the development of digital publishing in PostScript or via http; has brought together the perfect need for a more in-depth and complete set of metadata contained in fonts.

The variable fonts specification, included in the recent OpenType v1.8 font format has been demonstrated capable of changing that situation by the creation and use of a collection of axes more powerfully suited to the tasks of responsive world typography. Variable fonts launched with some registered axes that pertain to these attributes, such as width and weight, and introduced new ones such as optical size. This proposal contains additional axes pertaining to Latin and universal attributes that many users are familiar with, such as x height, and some that are less obvious, such as the vertical depth of descenders.

This initial proposal is for the primary set of axes that are inter-related, and form a gestalt system for Latin, and beyond. For world scripts,  it offers the potential for any world’s script to be the default around which a variable is designed, or for a default to contain all of the world’s scripts, offering a multitude of options for many users. Following the pervious examples, it means a Latin Geometric Sans variable font with weight and width axes, meaning each instance in the variable space has width and weight meta data, it can now have an x-height parameter under separate control for better appearance at small sizes, and thus multiple possible styles for each width and weight. Or a Latin design with weight, width and optical size axes, in a font with Chinese glyphs offering the same, can have multiple descender lengths depending on whether Chinese or Latin is the primary script in a text run.

Instead of choosing common general terms and then dissecting such a meaning down to this purpose, we created axis tag names for all of our proposals to represent direction, color and alignments of glyph groups, creating it’s own language, (one that has become quite convenient internally as we discuss the details of all kinds of type design projects, variable or not) . We chose value ranges to form a unified programmable set, built on typographic tradition where measures of variation are reasoned about in per-mille-of-em, points and degrees, among other things. This allows the definition of values relative either to a variable font, or values absolute and shared among any other fonts so measured.

So, this proposal includes axes that change Latin type attributes, but includes some that are inherent to all writing systems, when represented in a single variable font. Beyond these and into the decentralization from Latin parameters, an important aspect of these proposed “lower level” axes is they can be used to define ‘higher level’ axes like weight, by blending, or specifying instance of the lower level axes as extremes of the registered axes. This allows both developers and users to control the low level parameters of high level type attributes with precision for a multitude of applications alluded to above. Part of this includes proposing ‘Parametric Weight’ and ‘Parametric Width’ axes that  offer the same per-mille-of-em user experience as our other axes, and thus differ from the registered axes, wght and wdth in value systems.

We believe these axes allow type users, especially software developers and educators, to have a clearer picture of how typography is shaped by the attributes of typefaces. A near-future proposal, will follow with an overview containing world script alignments, time-base axes and axes for glyph-referencing among instances.

(Maybe: Making the system interoperable via registration is not essential to realizing the full value of variations. But a network effect is at play: as the potential functionality for typographers increases when each attribute can be combined with the others, registered axes or not, the exponential possibilities not being interoperable will likely exacerbate issues of responsive design and world scripts, beyond public programability or user interface-ability beyond local levels. )

**Related axes:** See individual axis proposals

**Similar axes:** See individual axis proposals

**Axis type:** Parametric

## Proposed Axis: `xtra`

**Tag:** xtra

**Name:** x transparent

**Axis type:** Optical

**Description:** assigns a “white” per mille value to each instance of the design space

**Valid numeric range:**  -1000 to 2000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: by setting a maximum word space parameter, and adjusting the XTRA units to a min and max. A developer could adjust justified text without tracking letters. Maintaining the apparent weight and width. 

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Many languages and scripts 

**Related axes:** wght, width, opsz

**Similar axes:** spac

**Additional information:** XTRA changes the white space in the x or horizontal direction. This useful in adjusting type horizontally without changing the opaque (black) Useful in VR, TV, and justification of text blocks.

**Conventionality benefits:** "White space" or "Negative Shapes" are common concepts in visual arts, but many users don't think about the transparent area of type deconstructed (or essentially isolated) to the X dimension. This axes helps users to structure their thinking about white space horizontally, for the overall/total typeface.

**Interoperability benefits:** justification, legibility

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-xtra.gif)

## Proposed Axis: `xopq`

**Tag:** xopq

**Name:** x opaque

**Axis type:** Optical

**Description:** assigns a “black” per mille value to each instance of the design space

**Valid numeric range:**  -1000 to 2000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Combined with YOPQ, a program or script can adjust each parameter to improve legibility at small sizes.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Many languages and scripts 

**Related axes:** wght, width, opsz

**Similar axes:** None

**Additional information:** XOPQ changes the black in the x or horizontal direction. By itself it expands the design space, by providing reverse contrast. Combined with YOPQ it can create more legible type at small sizes in platforms where hinting is not available.

**Conventionality benefits:** "Black space" or "Positive Shapes" are common concepts in visual arts, but many users don't think about the 'opaque' area of type deconstructed (or essentially isolated) to the X dimension. This axes helps users to structure their thinking about positive shapes horizontally, for the overall/total typeface.

**Interoperability benefits:** Weight matching, design space

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-xopq.gif)

## Proposed Axis: `ytra`

**Tag:** ytra

**Name:** y transparent

**Axis type:** Optical

**Description:** assigns an overall “white” per mille value to each instance

**Valid numeric range:**  0 to 2000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may choose to adjust YTRA in order to change the height of glyphs to emphasize text or headline, fit text to a space, stack and justify text.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Many languages and scripts 

**Related axes:** yopq 

**Similar axes:** hght

**Additional information:** YTRA changes the white space in the y or vertical direction. Combined with other axes it contributes to opsz, potentially HGHT among many options.

**Conventionality benefits:** "White space" is a common concept in visual arts, but many users don't think about the 'transparent' area of type deconstructed (or essentially isolated) to the Y dimension. This axes helps users to structure their thinking about white space vertically, for the overall/total typeface.

**Interoperability benefits:** linespacing, design space

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-ytra.gif)

## Proposed Axis: `yopq`

**Tag:** yopq

**Name:** y opaque

**Axis type:** Optical

**Description:** assigns a “black” per mille value to each instance of the design space

**Valid numeric range:**  -1000 to 2000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Combined with XOPQ, a program or script can adjust each parameter to improve legibility at small sizes.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Many languages and scripts 

**Related axes:** wght, width, opsz

**Similar axes:** None

**Additional information:** YOPQ changes the black in the y or vertical direction. By itself it expands the design space, by providing reverse contrast. Combined with XOPQ it can create more legible type at small sizes in platforms, and languages where hinting is not available.

**Conventionality benefits:** "Black space" or "Positive Shapes" are common concepts in visual arts, but many users don't think about the 'opaque' area of type deconstructed (or essentially isolated) to the Y dimension. This axes helps users to structure their thinking about positive shapes vertically, for the overall/total typeface.

**Interoperability benefits:** contrasting, design space, legibility

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-yopq.gif)

## Proposed Axis: `ytlc`

**Tag:** ytlc

**Name:** y transparent lowercase

**Axis type:** Optical

**Description:** assigns a “white” per mille value to each instance of the design space

**Valid numeric range:**  0 to 1000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may adjust the uppercase in coordination with another language or script, or adjust uppercase letters for a tv, vr, video setting to adjust to space, resolution or orientation.  

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Latin Primarily

**Related axes:** opsz, wght

**Similar axes:** None

**Additional information:** YTLC changes lowercase letters white space in the y direction. This axis contributes to opsz by raising the lowercase to increase legibility in small sizes. By allowing this axes to be used independently of opsz, the axis contributes to expanding the design space of a typeface.

**Conventionality benefits:** The "x height" of lowercase Latin letters is an attribute that many users can point to, but rather than calling this axes "x height," we see conventionality benefits in a name that fits into the systematic structure of this overall proposal: Y dimension transparency of lower case letters. 

**Interoperability benefits:** height matching, design space

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-ytlc.gif)

## Proposed Axis: `ytuc`

**Tag:** ytuc

**Name:** y transparent uppercase

**Axis type:** Optical

**Description:** a “white” per mille value for each Uppercase Height in the design space

**Valid numeric range:**  -1000 to 1000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may adjust the uppercase in coordination with another language or script, or adjust uppercase letters in a tv, vr, video setting to adjust to space, resolution or orientation.  

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Latin Primarily

**Related axes:** xtra, xopq 

**Similar axes:** hght

**Additional information:** YTUC changes the y direction or white space in uppercase letters. By itself, contributes to the design space when building of small, medium and tall capitals, or unicase. 

**Conventionality benefits:** The height of the upper case Latin letters is an attribute that all users can easily point to, but rather than calling this axes "cap height," we see conventionality benefits in a name that fits into the systematic structure of this overall proposal: Y dimension transparency of upper case letters. 

**Interoperability benefits:** height matching, design space

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-ytuc.gif)

## Proposed Axis: `ytde`

**Tag:** ytde

**Name:** y transparent descender

**Axis type:** Optical

**Description:** assigns a “white” per mille value to each instance of the design space

**Valid numeric range:**  -1000 to 0

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may adjust the descenders in coordination leading and column width to prevent letters from touching vertically.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Latin Primarily

**Related axes:** ytra, ytuc, ytlc

**Similar axes:** None

**Additional information:** YTDE changes the y or vertical descenders. Contributes to opsz in making small sizes fit better in text settings. Useful in adjusting letters when leading is reduced, in all sizes. Very useful in responsive design when headlines change from single lines to multiple lines of text.

**Conventionality benefits:** The zone or general area that descenders live in is an attribute that all users can easily point to (along with collisions in this area suffered by fonts without it) but not an area they may know by name. This name fits into the systematic structure of this overall proposal: Y dimension transparency of descenders. 

**Interoperability benefits:** linespacing, design space

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-ytde.gif)

## Proposed Axis: `ytas`

**Tag:** ytas

**Name:** y transparent ascender 

**Axis type:** Optical

**Description:** assigns a “white” per mille value to each instance of the design space

**Valid numeric range:**  0 to 1000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may adjust the ascenders in coordination leading and column width to prevent letters from touching vertically.

**UI recommendations:** Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface

**Script or language considerations:** Latin Primarily

**Related axes:** opsz, ytlc, ytde

**Similar axes:** None

**Additional information:** YTAS changes the y or vertical ascenders. Contributes opsz in making type fit better when size is reduced.

**Conventionality benefits:** The zone or general area that ascenders live in is an attribute that all users can easily point to (along with collisions in this area suffered by fonts without it) but not an area they may know by name. This name fits into the systematic structure of this overall proposal: Y dimension transparency of ascenders. 

**Interoperability benefits:** linespacing

**Demonstration:**
![Demonstration](https://axes-proposal.typenetwork.com/proposal/images/animation-ytas.gif)

## Proposed Axis: `pwth`

**Tag:** pwth

**Name:** Width (Parametric)

**Axis type:** Optical

**Description:** Used to vary width of text from narrower to wider; may be constructed by blending other primary axes, or via referenced instances of other
axes

**Valid numeric range:**  0 to 2000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may easily compute the appropriate weight to get a specific stem thickness.

**UI recommendations:** Primarily through end-user interfaces

**Script or language considerations:** Many languages and scripts 

**Related axes:** Always: xtra xopq. Sometimes: yopq ytos ytus

**Similar axes:** wdth

**Additional information:** This value range starts at 0 because if width is zero, counterforms are all closed in; if the XTRA value is negative, that doesn't matter in the blended axes. 

**Conventionality benefits:** A secondary benefit is that it encourages people to reason about their typography in per-mille measurements, a conventionality benefit. 

**Interoperability benefits:** The primary benefit of this axis is that is makes optical width more consistent, compared to the existing wght axis, and this is especially important when switching between families – thus an interop benefit. 

## Proposed Axis: `pwht`

**Tag:** pwht

**Name:** Weight (Parametric)

**Axis type:** Optical

**Description:** Used to vary stroke thicknesses or other design details to give variation from lighter to blacker; may be constructed by blending other primary axes, or via referenced instances of other
axes

**Valid numeric range:**  1 to 2000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may easily compute the appropriate weight to get a specific stem thickness.

**UI recommendations:** Primarily through end-user interfaces

**Script or language considerations:** Many languages and scripts 

**Related axes:** Always: xtra xopq. Sometime: yopq ytlc ytos (y overshoot at x height or above) ytus (y undershoot at baseline or below)

**Similar axes:** wght

**Additional information:** This value range starts at 1 because if it was zero, no ink would be drawn. 

**Conventionality benefits:** A secondary benefit is that it encourages people to reason about their typography in per-mille measurements, a conventionality benefit. 

**Interoperability benefits:** The primary benefit of this axis is that is makes optical weight more consistent, compared to the existing wght axis, and this is especially important when switching between families – thus an interop benefit. 

## Justification
**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**More info and demonstrations:** https://axes-proposal.typenetwork.com/
