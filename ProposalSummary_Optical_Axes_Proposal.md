# Proposal: Optical Axes Proposal

## General Technical Information

**Overview**
This proposal includes 3 “higher level” axes: ‘Weight Per Mille’ and ‘Width Per Mille’ and ‘Grade.’ 

The first 2 differ from the already existing registered axes ‘Weight’ and ‘Width’ in value systems. While those existing axes are useful with value systems designed for backwards compatibility (such as Regular at 400 and Bold at 700,) we think it is important to offer users the same per-mille-of-em user experience as the other axes in this proposal. These are formed by using “lower level” axes in concert.

Grade is a type attribute from refined typography, meaning that apparent weight changes occur without changes to glyph widths, so that line layouts remain constant – no reflow. It is formed mainly by increasing X Opaque while decreasing X Transparent (or vice versa.) However, other “lower level” axes will typically also be blended in, so changes are not only in the X dimension; for example, as grade gets very high and counterforms become narrow, a slight increase in Y Transparent and decrease in Y Opaque can open them up. 

**Related axes:** XTRA, YTRA, XOPQ, YOPQ, YTUC, YTLC, YTDE, YTAS, PWTH, PWGT

**Similar axes:** wght and wdth

**Axis type:** Optical

## Proposed Axis Details: `pwth`

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

**Script or language considerations:** Can be used for all scripts

**Related axes:** Always: xtra xopq. Sometimes: yopq ytos ytus

**Similar axes:** wdth

**Additional information:** This value range starts at 0 because if width is zero, counterforms are all closed in; if the XTRA value is negative, that doesn't matter in the blended axes. 

## Justification

**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**Conventionality benefits:** A secondary benefit is that it encourages people to reason about their typography in per-mille measurements, a conventionality benefit. 

**Interoperability benefits:** The primary benefit of this axis is that is makes optical width more consistent, compared to the existing wght axis, and this is especially important when switching between families – thus an interop benefit. 

## Proposed Axis Details: `pwht`

**Tag:** pwht

**Name:** Weight (Per Mille)

**Axis type:** Optical

**Description:** Used to vary stroke thicknesses or other design details to give variation from lighter to blacker; may be constructed by blending other primary axes, or via referenced instances of other
axes

**Valid numeric range:**  1 to 2000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may easily compute the appropriate weight to get a specific stem thickness.

**UI recommendations:** Primarily through end-user interfaces

**Script or language considerations:** Can be used for all scripts

**Related axes:** Always: xtra xopq. Sometime: yopq ytlc ytos (y overshoot at x height or above) ytus (y undershoot at baseline or below)

**Similar axes:** wght

**Additional information:** This value range starts at 1 because if it was zero, no ink would be drawn. 

## Justification

**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**Conventionality benefits:** A secondary benefit is that it encourages people to reason about their typography in per-mille measurements, a conventionality benefit. 

**Interoperability benefits:** The primary benefit of this axis is that is makes optical weight more consistent, compared to the existing wght axis, and this is especially important when switching between families – thus an interop benefit. 


## Proposed Axis Details: `grad`

**Tag:** grad

**Name:** Grade (Optical)

**Axis type:** Optical

**Description:** Used to vary stroke thicknesses or other design details to give variation from lighter to blacker without changing width; may be constructed by blending other primary axes, or via referenced instances of other
axes

**Valid numeric range:**  1 to 2000

**Scale interpretation:** Values should be interpreted as per-mille-of-em

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** Example: Program or script may easily compute the appropriate grade to bold or lighten text for affect. Program may easily set weight without changing width when trying to achieve consistency across platforms.

**UI recommendations:** Primarily through end-user interfaces

**Script or language considerations:** Can be used for all scripts

**Related axes:** Always: xtra xopq. Sometime: yopq ytlc ytos (y overshoot at x height or above) ytus (y undershoot at baseline or below)

**Similar axes:** wght, wdth

**Additional information:** This value range starts at 1 because if it was zero, no ink would be drawn. 

**Demonstration:**
![Demonstration](https:/Opentype-1.8-Axis-Proposal/proposal/images/grad.gif)

## Justification

**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**Conventionality benefits:** "Black space" or "Positive Shapes" are common concepts in visual arts, but many users don't think about the 'opaque' area of type deconstructed (or essentially isolated) to the Y dimension. This axes helps users to structure their thinking about positive shapes vertically, for the overall/total typeface.

**Interoperability benefits:** The primary benefit of this axis is that is makes create contrast in weight without changing width.



