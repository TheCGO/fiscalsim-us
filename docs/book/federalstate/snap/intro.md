(Chap_SNAP)=
# Supplemental Nutritional Assistance Program (SNAP)

(Chap_SNAPoverview)=
## Overview
The Supplemental Nutrition Assistance Program (SNAP) is the largest federal nutrition assistance program in the United States, and one of the largest poverty reduction programs in the United States. 68.5% of the 2019-2023 Farm Bill budget is allotted to SNAP [^FarmBill]. The 2021 Fiscal Year SNAP federal budget was $111 billion. [^SNAPFY2021] For comparison, similar welfare programs in FY 2021 - TANF: $30 billion;[^TANFFY2021] Medicaid: $521 billion; Medicare: $868 billion; Social Security: $1.1 trillion. [^MedSSFY2021]

The 2022 SNAP federal budget was $119 billion, aiding approximately 41 million low income beneficiaries per month [^SNAPstats].

Less formally known as food stamps, SNAP works to alleviate food insecurity by providing impoverished households with a monthly income support to purchase food. Eligibility for SNAP benefits are determined through a complex set of requirements that are established at the federal level, with several variations at the state level. The amount of SNAP benefit is allocated according to the number of members in the household, as well as the household's program-specific definition of net income (accounting for gross income, and removing several deductions, including utilities, transportation, and extenuating circumstances like disability or care for the elderly).

While state variations exist, the basic structure of SNAP allotment remains the same: disbursed SNAP monthly allottment varies according to household net income, number of household members, deductions, disability, and elderly household members. Interesting to note is that across states with various CPIs and standards of living, household quantity and determined household net income are associated with the same amount of SNAP allotment. For example, a family of 3 making \$18,000 per year in the Bay Area recieves as much SNAP benefits as a family of 3 in rural Utah with similar characteristics making \$18,000 per year, despite vast differences in the purchasing power of those SNAP dollars.[^cost_of_living]

Although a 4-year period from 1939 to 1943 marked the first use of a food stamp program, the first Food Stamp Pilot Program occurred in 1961 from an executive order from President Kennedy.[^1961ExecOrder] In 1964, the Food Stamp Act was passed to make the Food Stamp Program permanent.[^1964FoodStampAct] This orginal Food Stamp program, like the current iteration, was federally funded, with the states being responsible for certification and issuance of benefits. 

Since 1964, many legislative changes in the SNAP program have been passed, including its funding, changes to eligibility requirements, deduction specifics, and allotment amounts. Between 1988 and 2004, food stamp benefits began to be disbursed through an Electronic Benefit Transfer (EBT) card, as opposed to manual vouchers.[^EBT] In 2008, the program name was changed from "Food Stamp Program" to "Supplemental Nutrition Assistance Program" (SNAP).[^2008FarmBill] Under that same 2008 Farm Bill, a nutrition education component of the program was created and came to be known as SNAP-Ed. During the COVID-19 pandemic from 2020-2023, emergency allotments were added to increase SNAP benefits. These emergency allotments were terminated in March of 2023 with the end of the pandemic.[^COVIDSNAP] 

Much research exists investigating the effects of SNAP on various outcomes. Researchers monitor SNAP's economic effects (as a poverty reduction tool) [^SNAPpoverty], its nutritional effects (as a food security tool) [^foodsecurity], and even a growing amount of research investigates various other markers of well-being and development outcomes related to SNAP use (such as CPS and neglect events, child academic performance, and parental depression rates) [^SNAPCPS].

(Chap_SNAPfederal)=
## Federal SNAP policy characteristics

### Eligibility
Groups that may be eligible for SNAP benefits include those who work for low wages, are unemployed or work part time, recieve public assistance, have household members who are elderly or disabled, or are homeless.

Broad based categorical eligibility (BBCE) is a policy in which TANF-eligibile households automatically qualify for SNAP. For a complete list of states that implement BBCE, see the FiscalSim code.

Three eligibility requirements must be met to recieve SNAP benefits. 

1. Gross household income less than 130% FPL
2. Net household income (after deductions) less than 100% FPL
3. Household assets less than $2,750 in value

If a household meets these three requirements, then they are SNAP eligibile. More inclusive eligibility requirements (which vary state-by-state) exist for households that include elderly and disabled persons.

Additional eligibility requirements exist for Able Bodied Adults Without Dependents (ABAWD). Unless exempted for reasons of disability, adults ages 18-50 without children are limited to 3 months of SNAP benefits every three years. After the 3 months are up, individuals must be working or in a work training program for 20 hours per week to continue receiving SNAP benefits. 

### Benefit Amount

Once a household is deemed eligible for SNAP benefits, their benefit amount is calculated by the following equation:

SNAP benefit amount = Maximum eligible household benefit amount - (0.3)(net income) 

This calculation assumes that when SNAP households combine 30% of their net income with their allotted SNAP benefits, a household will have sufficient funds to purchase a nutritionally adequate diet according to the USDA's Thrifty Food Plan (TFP).

#### Maximum Eligible Household Benefit Amount

The SNAP maximum eligible household benefit amount for the fiscal year of 2023 is given in the following table:

| Household Size | Max Monthly Benefit |
| :---: | :---: |
| 1 | $281 |
| 2 | $516 |
| 3 | $740 |
| 4 | $939 |
| 5 | $1,116 |
| 6 | $1,339 |
| 7 | $1,480 |
| 8 | $1,691 |

#### Gross Income

The alloted SNAP benefit amount decreases as their calculated net income increases. Net income is calculated by subtracting relevant deductions from gross income. Gross income is the total household income before taxes, including the following sources: job, veteran's benefits, interest income, self employment, social security, disability, child support, worker's comp, unemployment income, pension income.

#### Deductions

Deductions from gross income to compute net income included the following:

- Standard deduction
- Earned income deduction 
- Dependent care 
- Child support
- Medical expenses
- Shelter expenses
- Standard, Limited or single utilities

Each of these deductions have different deduction caps that vary with the discretion of each state. See FiscalSim code for more details.


(SecSNAPstatepolicy)=
## State SNAP policy characteristics

While the basic structure of SNAP established by federal tax code ensures a fundamentally similar format across states, state-by-state variations make minor adjustments to SNAP eligibility and deductions that determine a household's net income. Below is a summary of the most prominent state variations--see the FiscalSim SNAP code for a complete list of state variations.

The most significant state variations exist with the asset test, varying gross income limits, and deduction caps. States that are more generous with SNAP may abolish the asset test and a gross income limit--no matter how many assets a household has, or what their gross income is, as long as their calculated deductions are great enough to bring them under 100% of the Federal Poverty Level, then they may qualify for SNAP. These states may also have larger deduction caps for various expenses, such as utilities. States that are more stringent with SNAP benefits may choose to establish tighter deduction caps, limiting the amount of income that can be deducted to calculate final household net income. These states may also choose to include the various eligibility hurdles--namely, an asset test and an income limit.


(SecSNAPfarmbill)=
## SNAP and the Farm Bill

The legislation, procedures, and funding for SNAP come from the Farm Bill. [^FarmBillProcess] Originally enacted in 1933 to support US food and agriculture producers affected by the Great Depression and the Dust Bowl, the current Farm Bill includes 12 titles that support various elements of agriculture and food production. Within the 12 titles, the 3 titles recieving the largest amounts of funding include Title I: Commodities (covers price and income support for farmers who produce widely-traded non-perishable crops); Title XI, Crop Insurance (subsidies to protect against losses in yield); and Title IV, Nutrition (90% of the funding for this Nutrition title goes to SNAP).

The Farm Bill legislation is passed every 5 years. For example, the Farm Bill that was passed in 2018 expires Septembeer 30th, 2023. A year before current legislation expires, lobbying for provisions begins by farm ogranizations, environmental groups, taxpayers, and other groups. [^FarmPrimer] After this public input, both the Senate and House Agriculture Committees draft, debate, and pass separate bill proposals. The Senate Agricultural Committee on Subsidies and Nutrition, and the House Agricultural Committee on Subsidies, Policy, and Oversight, are the two "Ag Committees" that draft these two bills. The two bills are sent to a Conference Committee where they are combined. The combined bill must then be approved by the entire House and Senate. This is the reauthorization process. 

The appropriations process determines funding for the various titles and programs in the Farm Bill. The 2018 Farm Bill received $428 billion. SNAP is an "entitlement program," where appropriatons will automatically be granted to fund their program. Other programs recieve "descretionary spending," where funds are granted at the discretion of the Appropriations Committees in Congress. This will be done before October 1st, 2023 for upcoming Farm Bill. 

The President then signs the Bill, which has been reauthorized and appropriated, into public law.

The "rulemaking phase" then occurs. After reauthorization and appropriations are complete and the bill has become a law, the USDA establishes specific rules and regulations which are implemented into the Farm Bill programs.



(SecSNAPfootnotes)=
## Footnotes

[^FarmBill]: This {cite}`USDA:2023` USDA webpage outlines distribution of the 2018 Farm Bill (see https://www.ers.usda.gov/topics/farm-economy/farm-commodity-policy/farm-bill-spending/).

[^SNAPFY2021]: This {cite}`CBPP:2022` article on the Center for Budget and Policy Priorities website gives an outline of the SNAP program, including its
FY 2021 budget (see https://www.cbpp.org/research/food-assistance/the-supplemental-nutrition-assistance-program-snap).

[^TANFFY2021]: This {cite}`ACF:2022` article from the DHHS government website outlines TANF spending for FY 2021 (see https://www.acf.hhs.gov/ofa/data/tanf-and-moe-spending-and-transfers-activity-fy-2021).

[^MedSSFY2021]: This {cite}`CBO:2022` infographic from the Congressional Budget Office outlines spending for various government programs for Fiscal Year 2021, including Medicare, Medicaid, and Social Security (see https://www.cbo.gov/publication/58270). 

[^SNAPstats]: The {cite}`Peterson:2023` article gives an overview of the economic statistics of the SNAP program (see https://www.pgpf.org/blog/2023/05/what-is-snap)

[^cost_of_living]: The {cite}`GerstenPaal:2022` policy memo details the SNAP FY 2023 cost of living adjustments (see https://www.fns.usda.gov/snap/fy-2023-cola). The SNAP allotments only differ among the following three groups--(i) 48 States, DC, Guam, Virgin Islands, (ii) Alaska, and (iii) Hawaii. All of those values increase with inflation each year, but all recipients in the lower 48 states have no difference in benefit amounts and are not adjusted within that group for cost of living.

[^1961ExecOrder]: The {cite}`Woolley:2023` article from the American Presidency Project at UC Santa Barbara expounds on the 1961 Executive Order From President Kennedy that expanded the Food Stamp program (see https://www.presidency.ucsb.edu/documents/executive-order-10914-providing-for-expanded-program-food-distribution-needy-families).

[^1964FoodStampAct]: The {cite}`Shahin:2014` article from the USDA website gives an overview of the 1964 Food Stamp Act that made the program permanent (see https://www.usda.gov/media/blog/2014/10/15/commemorating-history-snap-looking-back-food-stamp-act-1964)

[^EBT]: This {cite}`USDA:1988` legislation outlines the Hunger Prevention Act of 1988, which allowed for the food stamp program to test the effectiveness of Electronic Benefit Transfer Cards (see https://www.fns.usda.gov/pl-100-435)

[^2008FarmBill]: This {cite}`USDA:2008` legislation presents the 2008 Farm Bill, which made many administrative changes to the Food Stamp Program, including changing its name to SNAP and the creation of SNAP-Ed (see https://www.fns.usda.gov/pl-110-234)

[^COVIDSNAP]: This {cite}`USDA:2023` article from the USDA website explains the termination of emergency allotment SNAP benefits (see https://www.fns.usda.gov/snap/changes-2023-benefit-amounts).

[^SNAPpoverty]: This {cite}`Canning:2019` research article seeks to quantify the impact of SNAP benefits on the US Economy (see https://www.ers.usda.gov/amber-waves/2019/july/quantifying-the-impact-of-snap-benefits-on-the-u-s-economy-and-jobs/).

[^foodsecurity]: This {cite}`Mande:2023` research article investigates the childhood health impacts of the SNAP program (see https://pubmed.ncbi.nlm.nih.gov/36354297/).

[^SNAPCPS]: This {cite}`Johnson-Motoyama:2022` research article investigates the relationship between state SNAP generostiy and statewide CPS events (see https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9280401/).

[^FarmBillProcess]: This {cite}`ERSUSDA:2023` USDA webpage outlines the policy process of the passing of the Farm Bill (see https://www.ers.usda.gov/topics/farm-economy/farm-commodity-policy/u-s-farm-policy-and-policy-process/).

[^FarmPrimer]: This `Frye:2023` Farm Bill primer was graciously provided by Jason Frye at Terrapin Strategy consulting. 