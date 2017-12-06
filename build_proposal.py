# python III

from urllib.request import urlopen
import csv, re, os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

spreadsheet = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQDPjyUrfS27_vcTDjEnz8EznsfWOL5kFxCLDvphUV-9RgwU3o_gM71A1en58x6vrqOXs3-vHajGa1u/pub?gid=0&single=true&output=csv"

response = urlopen(spreadsheet)

csvlines = []
for line in response.readlines():
	line = line.decode('utf-8')
	if not csvlines and 'General Technical Information' in line:
		continue
	csvlines.append(line)

response.close()

reader = csv.DictReader(csvlines)

with open("README.md", 'r') as readme:
	introduction = readme.read().strip()
	introduction = re.sub(r'^\W*Introduction\W*\r?\n\s*', '', introduction)

with open("ProposalSummary.md", 'w') as proposal:
	proposal.write("""
# Proposal: Parametric and Optical Axes

## Administrative Information
**Proposers name:** Sam Berlow

**Vendor affiliation:** Type Network

**Proposal name:** Parametric Axes

**Date of submission:** 12/5/2017

**New or revised proposal:** New

**Previous revision date:** N/A

## General Technical Information
**Overview:** {introduction}

**Related axes:** See individual axis proposals

**Similar axes:** See individual axis proposals

**Axis type:** Parametric
""".format(introduction = introduction))

	for axis in reader:
# 		for k,v in axis.items():
# 			print(k, ':', v)

		imgurl = "https://axes-proposal.typenetwork.com/proposal/images/animation-{}.gif".format(axis['Tag'])
		try:
			img = urlopen(imgurl)
			imgurl = img.geturl()
			img.close()
		except:
			imgurl = None

		proposal.write("""
## Proposed Axis: `{axis[Tag]}`

**Tag:** {axis[Tag]}

**Name:** {axis[Name]}

**Axis type:** {axis[Axis Type]}

**Description:** {axis[Description]}

**Valid numeric range:** {axis[Valid numeric range]}

**Scale interpretation:** {axis[Scale interpretation]}

**Recommended or required “Regular” value:** N/A

**Suggested programmatic interactions:** {axis[Suggested programmatic interactions]}

**UI recommendations:** {axis[UI Recommendations]}

**Script or language considerations:** {axis[Script or Language considerations]}

**Related axes:** {axis[Related Axes]}

**Similar axes:** {axis[Similar Axes]}

**Additional information:** {axis[Additional information]}

**Conventionality benefits:** {axis[Conventionality benefits]}

**Interoperability benefits:** {axis[Interoperability benefits]}
""".format(axis=axis))

		if imgurl:
			proposal.write("""
**Demonstration:**
![Demonstration]({})
""".format(imgurl))

	proposal.write("""
## Justification
**Vendor commitments:** Google Fonts, Font Bureau, TYPETR

**More info and demonstrations:** https://axes-proposal.typenetwork.com/
""")

