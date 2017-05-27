# Font Bureau OpenType 1.8 Variations Axes Proposals

This guide will be presented to the OpenType Variations working group. 

Our goal is to reveal how our useful variations fonts are built from axes that enable optical sizes, variation through time and motion, and multi-script integration (Latin/CJK/Arabic/Hebrew.)

## Summary

This axes list contains several different kinds of axes. Nearly every value found in an otf 1.0 to the present, referring to a typographic value in the font, is susceptible to the need for a registered axis to identify that which can be defined as a variation in a font (ytlc and xtab are examples of those). Variations add the possibilities of motion, space and time, and inter-script adjustment, and thus the need for axes to be added for interoperable programmability among variations fonts dealing with animation and parameters specific to non-latin scripts.
(This seems a lot to register compared to the registration rate so far, which would have left us enough axes to last around 440,000 years. But here are 25 axes, proposed, if the community so chooses to adopt them as standards.)

## Overview

Our proposal contains several groups for axes registration including: 

1. Existing Latin values (e.g. [y transparent uc] = OT cap height, ), and those Latin values surrounded by these newly registered axis, (e.g. [y opaque]). there are 11 of those.

2. Non-existing, often-shared-with-Latin y values, that require script-specific values for interoperable programmability of inter-script variations, (e.g. [y transparent Kanji]. There are seven of those.

3. Non-existing motion-based axes for interoperable programability of variations in motion.

4. Non-existing axes allowing the recoding of morph locations from one glyph to another.

## Details

On each group

1. Universal values for weight [wght], width [wdth], and optical size [opsz], are already present in the specification, representing blends of lower level parameters that make weights, widths, and optical sizes, by standard definition and practice, in fonts of most scripts. Latin uppercase height, lowercase x-height, and several forms of descender and descender values also exist in the otf and so need to be recordable in variations. The proposed x opaque and x transparent axes are more variable OS/2 weight and width values, and y opaque is new. Via all of their registration, interoperability and programability.

2. This is a short list of script specific values for non-Latin designs that function best on different y proportions of the same em square in the productization phase of fonts, while still being able to share the em square in compromise or in favor of one script in the composition phase of typography via interoperable programatic access to these proposed axes.

3. These are fairly self-explanatory, if a use making animations is to solve the Distance = Rate x Time equation without trial-and-error on each glyph.

4. There is a need with animatable icons and glyphs, for the identity of unicodes that may vary along an axis to be definable. There is also great interest in supplying the glyphs of one instance from other instance locations in a variation space for glyphs of different features.
