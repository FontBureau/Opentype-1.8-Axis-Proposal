# Proposal Summary Form: Grade

## Administrative Information
**Proposers name:** David Berlow, Dave Crossland 

**Vendor affiliation:** Font Bureau, Google

**Proposal name:** Grade

**Date of submission:** 2020-01-09

**New or revised proposal:** New

## General Technical Information

**Overview:**

The Grade axis allows you to finesse how bold or light your type is, without changing the layout of the text, because letter widths and interletter spacing and kerning all remain fixed, so there are no changes to line breaks or page layout.

The term was coined at the Font Bureau foundry in the early 1990s, connoting motor oils and the way letterpress type leaves a bolder print with heavier inks.

In terms of parametric axes, Grade adjusts the transparent versus opaque forms, without changing widths or heights of glyphs. 

**Related axes:** Weight, though the change to weight in Grades is smaller, and change of weight typically changes width. 
Ideally a Grade axis is ranged for the entire design space, across all axes, and works optically well throughout. 

**Similar axes:** None proposed here. 

**Axis type:** Optical

## Proposed Axis Details

TODO: Double check [Guidance for Axis Details](GuidanceForAxisDetails.md) on this section.

**Tag:** `grad` (and `GRAD` until registered in the OT spec)

**Name:** Grade

**Description:** Finesse how bold or light your type is, without changing the layout of the text, because letter widths and inter letter spacing and kerning all remain fixed, so there are no changes to line breaks or page layout.

**Valid numeric range:** -1.0 to 1.0

**Scale interpretation:** A negative value represents a reduction in optical weight, while a positive value represents an increase in optical weight. 
The scale is relative only to itself, so 1.0 represents the maximum amount of positive graded weight and -1.0 the maximum negative graded weight.
In Amstelvar the Grade axis varies from -1.0, which is around 1/3 the weight of the Regular, to 1.0 which is around 2x.

**Required &ldquo;Regular&rdquo; value:** 0

**Recommended Use:**

In any output conditions where any weight is being distorted by the process, a corrective value can be employed to restore the weight to its intended appearance.
Grade can be used to correct for the distortions between; offset and gravure printing, light and dark mode interfaces, and lighter or darker than normal screen rendering.

**Suggested programmatic interactions:** 

In UX design, the primary use case is **more accessibility**, by adjusting type against background color changes to control contrast ratios, such as in Dark Mode.
Without it, Dark Mode can be stylistically limiting if the type is light overall, or contains particularly thin strokes in a high contrast design.

A secondary use case is **smooth interactivity**, adjusting type based on pointer position (eg on hover) without redrawing any layout (text or ui.)

Another UX use case is optimization for specific devices or platforms.
Lower screen resolutions or rendering software do not work well when representing any Weight lighter than 200.
Such optimization is also useful in print, when a spread will use different papers, inks and presses on each side, so the digital type has to be different to look the same on the finished document.

Finally, when pairing two or more different families - often for a typographic purpose, or perhaps for multilingual texts - Grade can be used for matching the weight of one family to another.

Each of these use cases can be done by eye, or programmatically.

**UI recommendations:** TODO: See the Guidance file for details on what information is expected.

**Script or language considerations:** Grade is applicable to all scripts or languages.
TODO: Describe any special considerations for applying the axis to specific scripts or languages.

**Additional information:** \[Provide any additional information that may be needed or helpful for
implementers to understand how the axis should be used.]

## Justification

**Vendor commitments:** Vendors that plan to use this axis, if registered, include Google, TypeNetwork, Font Bureau, Microsoft, Axis-Praxis, Fontsmith and many web design services vendors.

**Conventionality benefits:** Registering Grade is important because it is already adopted pre-otvar by a number of font vendors, so establishing a standard that encompasses all ways to implement Grade can reduce fragmentation of custom axes.

It is likely to become broadly adopted or familiar because the value of the use cases for digital product design is high. 

**Interoperability benefits:** The registration of this axis and values will allow content and device developers to automate the changes grad will enable for adjustment of static and streaming typography to background, script and device conditions.

## Other Supporting Information

TODO: Provide GIF to demonstrate the behaviour of Grade

#### Existing Examples

* https://github.com/TypeNetwork/Amstelvar
* https://github.com/TypeNetwork/Roboto-Flex
* https://github.com/agyeiarcher/Crispy-VF

#### Why is -1.0..1.0 with default 0 the best scale to define for this axis?

Zero is the best default value because when a value is set it immediately communicates whether the grade is positive or negative relative to the default, and always leaves a value that’s easy to undo by resetting back to zero (even if a specific implementation isn't equally positive and negative.)

-1.0..1.0 is the best defined range because it connotes the small increments typically needed for good results: 0 to 0.2 feels smaller than 0 to 20 or 200; because it is clearly relative only to itself, and it doesn't imply a family implementation has to be evenly +/- or cover the entire range. 

Here are a few reasons why other scales aren't as good: 

#### Why not -10..10, default 0, or -100..100 or -1000..1000?

This would be okay, but it isn't as good because as above it implies the differences are larger; grade is typically used in a subtle way, so a change from 0 to 2 to 10 feels bigger than a change from 0.0 to 0.2 to 10 – and 0 to 200 to 1000 even bigger still. (And -0.1..0.1 would be too far in the opposite direction, because the effect of grade isn't always subtle.)

#### Why not -100..100%, default 0%?

A percent is relative to some specific form, such as the stem width of `H`.

This would be actually bad because a percentage is different to a plain number in ways that aren't appropriate to Grade, by being more strongly associated with normalization. 

Family ranges will not always be the full extent of the defined range, and not always evenly balanced - as the amount of opacity a foundry may want to tackle may differ from family to family, and an underlying weight range may not be evenly balanced +/-. Some family's grade may go further than others, and go more positive than negative. But presenting grade as a percentage nudges foundries towards giving each family's grade the same range even though the amount of grade differs, and towards evenly balancing it. 

Any percentage inherently normalizes a range into a linear progression - which is unlikely to always be the case with a Grade axis. The difference between 0% to 20% and 20% to 40% and 80% to 100% should be similar, as the increments are equidistant and in a percentage normalized, but the visual effect may not be - perhaps due to avar warping, if not intermediate masters.

#### Why not -0%, +200%, default 100%, like msft Width; or 0..100%, default 50%?

In addition to the problem with the above % range, these make the important neutrality of the default less clear, inviting off-spec defaults that could make sense given an uneven balance or non linear progression, especially if the foundry wishes to present their grade as the whole range as defined. 

#### Why not 1-1000, default 400, like msft Weight?

This suggests the range can be equivalent to weight, which is misleading.

#### Why not per mille of em, like parametric axes?

Per mille of em is not -/+ from a neutral default; grade is not a parametric axis, and in avar2 it may be synthesized from changes to parametric axes XTRA, XOPQ, and YOPQ.
